# Trajectoire eSAF dans le TYNDP 2026 — dépôt pédagogique (master)

[![Ouvrir dans Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Silake-prog/students-usaf/blob/main/notebooks/esaf_trajectoire.ipynb)

## Objectif
Étudier la trajectoire des **carburants de synthèse (e-fuels, dont l'eSAF)** dans les scénarios **TYNDP 2026** (ENTSO-E / ENTSOG) et ce qu'elle implique : quel volume d'eSAF, quels besoins amont (hydrogène, électricité, CO₂, eau), quel écart avec l'obligation européenne **ReFuelEU Aviation**. Le carnet est guidé pas à pas (pandas, matplotlib, numpy expliqués) et se termine par des exercices ouverts.

## Contenu
| Partie | Contenu |
|---|---|
| 1 | Carburants de l'aviation (internationale + domestique) par vecteur, par pays et pour l'UE-27, 2030/2035/2040/2050 |
| 2 | Besoins amont d'un volume d'eSAF donné, avec rendements sourcés, fourchettes et sensibilité ; comparaison avec « H2 to E-Liquids » de TYNDP |
| 3 | Comparaison NT+ / HEV / LEV, UE-27 contre un pays au choix (variable `PAYS` en tête de carnet) |
| 4 | Exercices ouverts |

Pas de partie « impact climatique » (hors périmètre voulu).

## Ce que les données contiennent… et ne contiennent pas
- **TYNDP ne sépare pas le kérosène fossile, le biokérosène et l'e-kérosène** : l'aviation n'a qu'un vecteur `Liquids`. Le volume d'eSAF est donc **dérivé** à partir des lignes « e-liquides » du tableau KPI (hydrogène vers e-liquides, importations), par une méthode explicite dans le carnet (section 4), avec deux règles d'affectation à l'aviation (prorata / aviation d'abord).
- Les lignes e-fuels sont à l'échelle **UE-27** (importations, demande) ; seules quelques pays ont une production nationale de e-liquides.
- HEV et LEV ne sont publiés que pour **2035 et 2040** ; NT+ pour 2030, 2035, 2040, 2050.
- Éléments marqués **[À VÉRIFIER]** dans le carnet : unité du CO₂ des e-fuels (libellé « kt », ordre de grandeur Mt), base énergie/volume de l'obligation pour les liquides, eau (plancher stœchiométrique), rendement de méthanation 0,8 utilisé pour un contrôle.

## Lancer le carnet
**Local (Jupyter)**
```bash
git clone https://github.com/Silake-prog/students-usaf.git
cd students-usaf
python -m venv .venv && source .venv/bin/activate   # Windows : .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook notebooks/esaf_trajectoire.ipynb
```
**Google Colab** : le dépôt est **privé**. Il faut un compte GitHub avec accès au dépôt. Cliquez sur le badge ci-dessus (Colab demande d'autoriser GitHub), puis exécutez la première cellule : elle propose soit de coller un **jeton d'accès personnel GitHub** (lecture) pour cloner le dépôt, soit de **téléverser à la main** les 5 CSV du dossier `data/`. L'alternative sans Colab est le lancement local ci-dessus.

## Structure
```
README.md   LICENSE   requirements.txt   .gitignore
data/        CSV ordonnés + README.md (colonnes, unités, provenance) + SOURCES.md
notebooks/   esaf_trajectoire.ipynb (parties guidées exécutées avec leurs sorties ; exercices vides)
scripts/     extract_tyndp_tables.py (traçabilité de l'extraction, non nécessaire aux étudiants)
```

## Licences et attribution
- **Code** (carnet, scripts) : licence MIT (`LICENSE`).
- **Données** : *TYNDP 2026 Scenarios*, ENTSO-E / ENTSOG, sous licence **Creative Commons Attribution 4.0 International (CC BY 4.0)**. Attribution : « TYNDP 2026 Scenarios ». Les fichiers de `data/` sont des extraits remis en forme (agrégation, filtrage, renommage) ; ils ne sont ni approuvés ni endossés par ENTSO-E ou ENTSOG. Détail dans `data/SOURCES.md`.
- Texte réglementaire : Règlement (UE) 2023/2405, annexe I (EUR-Lex).
