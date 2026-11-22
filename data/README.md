# Données du carnet

Extraction du 2026-11-22. Source : *TYNDP 2026 Scenarios* (ENTSO-E / ENTSOG, CC BY 4.0), tableaux ETM (demande finale) et tableaux de bord KPI. Script : `../scripts/extract_tyndp_tables.py`. Scénarios : NT+ (2030, 2035, 2040, 2050), HEV et LEV (2035, 2040). Pays : UE-27 + Suisse (CH, hors agrégat UE-27). Énergie en TWh (PCI).

| Fichier | Lignes | Contenu |
|---|---|---|
| `aviation_fuel_by_carrier.csv` | 1 344 | `variant, country, year, subsector, carrier, twh` : énergie finale de l'aviation (sous-secteurs `International aviation` et `Planes`) par vecteur. Seuls les vecteurs non nuls sont gardés : `Liquids`, `Hydrogen`, `Electricity`. **Pas de séparation fossile / bio / synthétique dans la source.** |
| `liquids_all_sectors.csv` | 8 064 | `variant, country, year, sector, subsector, energy_type, fec, twh` : vecteur `Liquids` de **tous** les secteurs (dénominateur de la part de e-liquides). `fec` = `FEC` ou `not_included_in_FEC` (non-énergétique, raffineries, soutes maritimes). |
| `tyndp_efuels_kpi.csv` | 1 507 | `variant, country, year, section, block, label, flag, unit, value, note` : lignes e-fuels des tableaux KPI, colonne « Weighted WS » (moyenne pondérée des années météo). `flag` : I = entrée du scénario, R = résultat du dispatch. `note` = `EU27 level specific` quand la valeur n'existe qu'à l'échelle UE-27 (`value` vide). |
| `countries.csv` | 28 | Code TYNDP, nom français, appartenance UE-27. |
| `refueleu_annex1.csv` | 7 | Parts minimales de SAF et de carburants synthétiques, saisies à la main d'après l'annexe I du Règlement (UE) 2023/2405 (EUR-Lex, texte du JO du 31.10.2023). |

## Lignes KPI exactes utilisées (feuilles pays + `EU27` de `{NT+,HEV,LEV}_KPI_Dashboard.xlsx`)
`H2 to E-Liquids` (Consumption/H2, ligne ≈154 ; FLH/H2 ≈128, UE-27 seulement), `H2 to SNG` (≈153), `E-Fuel Demand [TWh H2]` (≈157), `E-Fuel Shortage [TWh H2]` (≈158), `CO2 to E-Fuels [kt]` (≈156), `E-Liquids Capacity (from H2)` (≈47, GW), `SNG Capacity (from H2)` (≈46), `E-Liquid Imports [TWh H2]` (≈137), `SNG Imports [TWh H2]` (≈136), `H2 to eFuels` (Energy Balance, ≈189). Numéros de ligne indicatifs (feuille UE-27).

## Points d'attention
- `H2 to E-Liquids` etc. sont en **TWh d'hydrogène**, pas en TWh de carburant.
- `CO2 to E-Fuels [kt]` : le libellé source est « kt », mais l'ordre de grandeur (≈80 en 2050 pour ≈976 TWh H₂ de e-fuels) évoque des Mt. **[À VÉRIFIER]** ; non corrigé dans les données.
- Les sommes des pays (hors CH) retrouvent la ligne `EU27` pour `H2 to E-Liquids`, `H2 to SNG` et `Installed Capacity` ; les heures équivalentes (`FLH`) ne sont donc gardées qu'au niveau `EU27`.
- Le bilan UE-27 boucle : H₂ vers e-liquides + imports e-liquides + H₂ vers SNG + imports SNG = `E-Fuel Demand` (vérifié dans le carnet).
