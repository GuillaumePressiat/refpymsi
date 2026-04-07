# refpymsi Streamlit Explorer

Application Streamlit pour explorer localement les référentiels PMSI.

## Installation

```bash
pip install -r requirements.txt
```

## Utilisation

```bash
streamlit run streamlit_app.py
```

L'application s'ouvre à l'adresse http://localhost:8501

## Fonctionnalités

3 onglets pour explorer les données PMSI :
- **Tables** : 55 tables de référence avec export CSV
- **Listes** : 184 listes thématiques avec export JSON
- **Recherche** : Moteur de recherche unifié par mot-clé

## Dépendances

- Python 3.8+
- Streamlit 1.20+
- Pandas 1.3+
- Polars 0.16+

## Notes

- Toutes les données sont chargées localement depuis votre installation refpymsi
- Pas de connexion internet requise après installation
- Cache activé pour de meilleures performances
