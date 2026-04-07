# refpymsi

Lire les référentiels et accéder à des listes de requêtes pour le PMSI avec python

## Installation

```bash
# Installation depuis GitHub
pip install https://github.com/GuillaumePressiat/refpymsi/releases/download/2026.0.0/refpymsi-2026.0.0-py3-none-any.whl
```

## Résumé des données disponibles

### Tables de référence (55)

| Catégorie | Nombre | Exemples |
|-----------|--------|----------|
| CCAM (y compris tarifs CCAM) | 16 | ccam_actes, ccam_descri, ccam_hierarchie_actes |
| CIM-10 | 2 | cim, cim_hierarchie_code |
| CSARR | 9 | csarr_acte_ref, csarr_code, csarr_hier |
| Tarifs (hors CCAM) | 5 | tarifs_mco_ghs, tarifs_had_ght, tarifs_mco_supplements |
| GHS/GHM | 3 | ghm_dms_nationales, ghm_ghm_regroupement |
| Géographie | 1 | codes_geo_com_ts_corresp |
| Libellés SSR | 6 | lib_ssr_autoum, lib_ssr_cm, lib_ssr_gme |
| Médicaments | 6 | lpp_fiche, mco_aturef_atih_indications |
| Autres | 7 | orpha, dictionnaire_tables, lib_mco_um, ... |

### Listes thématiques (184)

| Thématique | Nombre | Exemples |
|------------|--------|----------|
| Recours exceptionnels | 59 | CANCERO_EXH_APP_ORG_01, chip, cathe_cardiaque_interv_pediatrique_cardiopathie_congenitales |
| Pathologies (hors recours) | 2 | bpco_exacerbee, chir_oesophage_hors_cancer |
| Réanimation | 2 | arec_rea_nnat, rea_nnat_moins_700g |
| Pédiatrie | 2 | ... |
| Autres | 119 | ... |

> **Note** : Certaines listes comme `CANCERO_EXH_APP_ORG_*` sont à la fois des recours exceptionnels et des pathologies. Elles sont comptabilisées dans la catégorie "Recours exceptionnels" pour éviter les doublons.

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

## Tables de référence

La bibliothèque donne accès à **55 tables de référence** incluant :

- **CCAM** : Classification Commune des Actes Médicaux
- **CIM-10** : Classification Internationale des Maladies
- **Tarifs** : GHS, GHM, et autres tarifications
- **Géographie** : Codes géographiques et correspondances
- **Spécialités** : Référentiels médicaux spécialisés

### Exemples d'utilisation

```python
import refpymsi as rp

# Récupérer une table (format Polars par défaut)
df_ccam = rp.get_table('ccam_actes')
print(df_ccam.shape)  # (8542, 7)

# Récupérer au format Pandas
df_orpha = rp.get_table('orpha', plrs=False)
print(type(df_orpha))  # <class 'pandas.core.frame.DataFrame'>

# Accéder aux tarifs MCO
df_tarifs = rp.get_table('tarifs_mco_ghs')
print(df_tarifs.columns)
# ['ghs', 'ghm', 'libelle_ghm', 'borne_basse', ..., 'time_i']
```

### Tables populaires

| Nom de la table | Description | Lignes | Colonnes |
|----------------|-------------|--------|----------|
| `ccam_actes` | Actes CCAM | 8,542 | 7 |
| `orpha` | Maladies rares (Orphanet) | 9,546 | 12 |
| `tarifs_mco_ghs` | Tarifs MCO par GHS | 44,055 | 12 |
| `cim` | Classification CIM-10 | ~14,000 | 5 |
| `ccam_tarifs` | Tarifs des actes CCAM | ~8,500 | 8 |

## Listes de requêtes

**184 listes thématiques** pour des requêtes PMSI spécifiques, organisées par :

- Recours exceptionnels
- Pathologies spécifiques
- Actes médicaux spécialisés
- Populations particulières

### Exemples d'utilisation

```python
import refpymsi as rp

# Récupérer une liste spécifique
data_chip = rp.get_liste('chip')
print(data_chip['nom'][0])  # "Chimiothérapie hyperthermique intra-péritonéale (CHIP)"

# Liste complexe avec critères
data_cardiologie = rp.get_liste('cathe_cardiaque_interv_pediatrique_cardiopathie_congenitales')
print(f"Actes: {data_cardiologie['actes'][:3]}")  # ['DAAF001', 'DAAF002', 'DAGF001', ...]

# Rechercher des listes par thème
listes_recours = [l for l in rp.list_available_listes() if 'recours' in l.lower()]
```

### Listes populaires

| Nom de la liste | Thématique | Description |
|-----------------|------------|-------------|
| `chip` | Recours Exceptionnel | Chimiothérapie hyperthermique intra-péritonéale |
| `cathe_cardiaque_interv_pediatrique_cardiopathie_congenitales` | Recours Exceptionnel | Cathétérisme cardiaque interventionnel pédiatrique |
| `arec_rea_nnat` | Réanimation | Réanimation néonatale |
| `bpco_exacerbee` | Pathologie | BPCO exacerbée |

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

### `get_table(nom_table, plrs=True)`

- `nom_table` (str) : Nom de la table à récupérer (voir `list_available_tables()`)
- `plrs` (bool) : Si True, retourne un DataFrame Polars (défaut). Si False, retourne un DataFrame Pandas.

### `get_liste(nom_liste)`

- `nom_liste` (str) : Nom de la liste à récupérer (voir `list_available_listes()`)
- Retourne un dictionnaire avec les métadonnées et critères de la liste

### `list_available_tables()`

- Retourne une liste de toutes les tables disponibles
- Chaque élément est le nom exact à utiliser avec `get_table()`

### `list_available_listes()`

- Retourne une liste de toutes les listes disponibles
- Chaque élément est le nom exact à utiliser avec `get_liste()`

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

## Contribution

Voir [CONTRIBUTING.md](CONTRIBUTING.md) pour savoir comment contribuer au projet.

## Licence

AGPL - Voir [LICENSE](LICENSE) pour plus de détails.