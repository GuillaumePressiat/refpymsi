# refpymsi

Lire les référentiels et accéder à des listes de requêtes pour le PMSI avec python

## Installation

```bash
# Installation depuis GitHub
pip install https://github.com/GuillaumePressiat/refpymsi/releases/download/2026.0.0/refpymsi-2026.0.0-py3-none-any.whl
```

## Exploration des données

Pour explorer les 55 tables de référence et 184 listes thématiques PMSI :

```bash
# Installer les dépendances
pip install -r requirements.txt

# Lancer l'application Streamlit
streamlit run streamlit_app.py
```

L'application propose :
- **Tables** : Exploration et export des 55 tables de référence
- **Listes** : Navigation dans les 184 listes thématiques
- **Recherche** : Moteur de recherche unifié

Voir [README_STREAMLIT.md](README_STREAMLIT.md) pour plus de détails.

## Démarrage rapide

```python
import refpymsi as rp

# Liste toutes les tables disponibles
tables_disponibles = rp.list_available_tables()
print(f"{len(tables_disponibles)} tables disponibles")

# Liste toutes les listes disponibles  
listes_disponibles = rp.list_available_listes()
print(f"{len(listes_disponibles)} listes disponibles")
```



## Fonctions de découverte

```python
import refpymsi as rp

# Lister toutes les tables disponibles
tables = rp.list_available_tables()
print(f"Tables disponibles: {', '.join(tables[:5])}...")

# Lister toutes les listes disponibles
listes = rp.list_available_listes()
print(f"Listes disponibles: {', '.join(listes[:5])}...")

# Rechercher des tables par mot-clé
tables_ccam = [t for t in rp.list_available_tables() if 'ccam' in t.lower()]
print(f"Tables CCAM: {tables_ccam}")

# Rechercher des listes par thème
listes_recours = [l for l in rp.list_available_listes() if 'recours' in l.lower()]
```

## Documentation des paramètres

| Fonction | Description | Paramètres |
|----------|-------------|------------|
| `get_table(nom_table, plrs=True)` | Récupère une table de référence | `nom_table` (str) : Nom de la table<br>`plrs` (bool) : Format Polars (True) ou Pandas (False) |
| `get_liste(nom_liste)` | Récupère une liste thématique | `nom_liste` (str) : Nom de la liste<br>Retourne un dictionnaire |
| `list_available_tables()` | Liste toutes les tables disponibles | Aucun paramètre |
| `list_available_listes()` | Liste toutes les listes disponibles | Aucun paramètre |

## Bonnes pratiques

```python
import refpymsi as rp

# Toujours vérifier que la table/liste existe
tables = rp.list_available_tables()
if 'ma_table' in tables:
    df = rp.get_table('ma_table')

# Pour les grandes tables, préférer Polars (défaut) pour la performance
df_grand = rp.get_table('tarifs_mco_ghs')  # Polars - rapide

# Pour l'interopérabilité avec d'autres bibliothèques
df_pandas = rp.get_table('ccam_actes', plrs=False)  # Pandas

# Explorer la structure avant utilisation
print(rp.get_table('orpha').columns)
```

## Licence

AGPL - Voir [LICENSE](LICENSE) pour plus de détails.