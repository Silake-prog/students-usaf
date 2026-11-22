"""Extraction (fournie pour la traçabilité, non nécessaire aux étudiants) des petits CSV de data/.

Lancé le 2026-11-22 sur le serveur de recherche, à partir de tables TYNDP 2026 déjà ordonnées :
  - tyndp_etm_fec.csv (tableau de bord ETM du TYNDP 2026, demande finale par secteur, scénarios NT+/HEV/LEV)
  - {NT+,HEV,LEV}_KPI_Dashboard.xlsx (tableaux de bord KPI : une feuille par pays + EU27), lus ligne à ligne par un lecteur
    openpyxl (`read_rows` de supplyforge.process.tyndp.kpi), colonne « Weighted WS » (moyenne pondérée des années météo).
Usage : python extract_tyndp_tables.py <dossier tyndp> <dossier de sortie>
"""
import sys
from pathlib import Path
import pandas as pd

src, out = Path(sys.argv[1]), Path(sys.argv[2])
sys.path.insert(0, str(Path(sys.argv[3])))  # dossier qui contient kpi.py
import kpi

EU27 = "AT BE BG CY CZ DE DK EE ES FI FR GR HR HU IE IT LT LU LV MT NL PL PT RO SE SI SK".split()
KEEP = EU27 + ["CH"]

fec = pd.read_csv(src / "tyndp_etm_fec.csv")
fec = fec[fec.country.isin(KEEP)]
av = fec[fec.subsector.isin(["International aviation", "Planes"])]
av = av.groupby(["variant", "country", "year", "subsector", "carrier"], as_index=False).twh.sum()
av = av[av.groupby("carrier").twh.transform(lambda s: s.abs().sum()) > 0]  # carriers jamais utilisés : retirés
av.to_csv(out / "aviation_fuel_by_carrier.csv", index=False)

liq = fec[fec.carrier == "Liquids"][["variant", "country", "year", "sector", "subsector", "energy_type", "fec", "twh"]]
liq.to_csv(out / "liquids_all_sectors.csv", index=False)

rows = [("H2 to E-Liquids", None), ("H2 to SNG", None), ("E-Fuel Demand [TWh H2]", None), ("E-Fuel Shortage [TWh H2]", None),
        ("CO2 to E-Fuels [kt]", None), ("E-Liquids Capacity (from H2)", None), ("SNG Capacity (from H2)", None),
        ("E-Liquid Imports [TWh H2]", None), ("SNG Imports [TWh H2]", None), ("H2 to eFuels", None)]
recs = []
for v in ["NT+", "HEV", "LEV"]:
    recs += kpi.read_rows(src / "raw" / "dashboards" / f"{v}_KPI_Dashboard.xlsx", rows, variant=v, sheets=KEEP + ["EU27"])
d = pd.DataFrame(recs)
d = d[d.ws == "Weighted WS"].copy()
d["country"] = d.country.replace({"EU27": "EU27"})
d = d[~((d.section.str.startswith("FLH")) & (d.country != "EU27"))]  # les heures équivalentes pays ne sont pas additives
num = pd.to_numeric(d.value, errors="coerce")
d["note"] = ""
d.loc[num.isna() & d.value.notna(), "note"] = d.value.astype(str)
d["value"] = num
d = d[d.value.notna() | (d.note != "")]
d["section"] = d.section.str.replace(r"\s*\[.*\]", "", regex=True)
d["unit"] = d.label.map(lambda s: "kt" if "[kt]" in s else ("GW" if "Capacity" in s else ("TWh H2" if "H2" in s else "TWh")))
d.loc[d.section == "FLH", "unit"] = "h"
d.loc[d.section == "Installed Capacity", "unit"] = "GW"
d[["variant", "country", "year", "section", "block", "label", "flag", "unit", "value", "note"]].sort_values(
    ["variant", "section", "label", "country", "year"]).to_csv(out / "tyndp_efuels_kpi.csv", index=False)
print("ok")
