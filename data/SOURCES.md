# Sources et licences

- **TYNDP 2026 Scenarios**, ENTSO-E et ENTSOG. Licence **CC BY 4.0** : la page de téléchargement (2026.entsos-tyndp-scenarios.eu/download/) indique que les données sont publiées sous « Creative Commons Attribution 4.0 International License » et demande l'attribution « TYNDP 2026 Scenarios » (consultée le 2026-11-22). Fichiers utilisés : tableau de bord ETM de demande finale (`TYNDP2026_ETM_DASHBOARD.xlsx`) et tableaux de bord KPI (`NT+`, `HEV`, `LEV`). Les CSV de ce dossier sont des extraits remis en forme ; ENTSO-E et ENTSOG ne les endossent pas.
- **Règlement (UE) 2023/2405** du 18 octobre 2023 (ReFuelEU Aviation), annexe I, EUR-Lex (CELEX 32023R2405), lu le 2026-11-22.
- **Concawe (2024)**, *E-Fuels: A techno-economic assessment of European domestic production and imports towards 2050 — Update*, Report 4/24 (rendements électrolyse, électricité→e-kérosène FT, CO₂ lié au carburant).
- **Ueckerdt, F. et al. (2021)**, *Potential and risks of hydrogen-based e-fuels in climate change mitigation*, Nature Climate Change 11, 384–393 (pertes électricité→carburant d'environ 40 %).

## Vérification de la version (2026-11-23)
Les fichiers TYNDP utilisés pour l'extraction sont identiques, octet pour octet, à ceux publiés aujourd'hui sur la page officielle (https://2026.entsos-tyndp-scenarios.eu/download/, version finale de juin 2026) :

| Fichier | Mise en ligne (en-tête Last-Modified) | sha256 |
|---|---|---|
| `TYNDP2026_ETM_DASHBOARD.xlsx` | 2026-06-11 | `ddc07d38c1f47ad4a23669c8830367b98706c7b839ae94e1260b528f8ea7f12b` |
| `NT+_KPI_Dashboard.xlsx` | 2026-06-08 | `019592da14626c8452e16f452e98c1e3afc880a4a6e4913f498dba6df70cda6e` |
| `HEV_KPI_Dashboard.xlsx` | 2026-06-08 | `18f332f5c2bbb7896026a8ff664284e9f2cf3c8d280dc0b45bbfe9f71a5e08db` |
| `LEV_KPI_Dashboard.xlsx` | 2026-06-08 | `e33886e15554751c355b8dd1a73ecc6b11726b6789030a0ed5d01a7c2adba379` |
