# refpymsi

Lire les référentiels et accéder à des listes de requêtes pour le PMSI avec python




## Tables de références

```python
# Exemples
import refpymsi as rp

[rp.get_table('ccam_actes'), 
 
 rp.get_table('orpha'),

 rp.get_table('tarifs_mco_ghs')
]
````


````
[shape: (8_542, 7)
 ┌─────────┬─────────────────┬───────────┬─────────────────┬────────────┬────────────────┬──────────┐
 │ code    ┆ libelle_court   ┆ type_acte ┆ compatibilite_s ┆ date_debut ┆ libelle_long   ┆ date_fin │
 │ ---     ┆ ---             ┆ ---       ┆ exe             ┆ ---        ┆ ---            ┆ ---      │
 │ str     ┆ str             ┆ str       ┆ ---             ┆ str        ┆ str            ┆ str      │
 │         ┆                 ┆           ┆ str             ┆            ┆                ┆          │
 ╞═════════╪═════════════════╪═══════════╪═════════════════╪════════════╪════════════════╪══════════╡
 │ AAFA001 ┆ exérèse T.      ┆ 0         ┆ 0               ┆ 2005-03-01 ┆ Exérèse de     ┆ null     │
 │         ┆ intraparench    ┆           ┆                 ┆            ┆ tumeur intrapa ┆          │
 │         ┆ cervelet…       ┆           ┆                 ┆            ┆ renchym…       ┆          │
 │ AAFA002 ┆ exérèse T.      ┆ 0         ┆ 0               ┆ 2005-03-01 ┆ Exérèse de     ┆ null     │
 │         ┆ intraparench    ┆           ┆                 ┆            ┆ tumeur intrapa ┆          │
 │         ┆ cerveau …       ┆           ┆                 ┆            ┆ renchym…       ┆          │
 │ AAFA003 ┆ exérèse lés.    ┆ 0         ┆ 0               ┆ 2005-03-01 ┆ Exérèse de     ┆ null     │
 │         ┆ tr. céréb.      ┆           ┆                 ┆            ┆ lésion du      ┆          │
 │         ┆ craniot.        ┆           ┆                 ┆            ┆ tronc céréb…   ┆          │
 │ AAFA004 ┆ hémisphérectomi ┆ 0         ┆ 0               ┆ 2005-03-01 ┆ Hémisphérectom ┆ null     │
 │         ┆ e fct craniot.  ┆           ┆                 ┆            ┆ ie             ┆          │
 │         ┆                 ┆           ┆                 ┆            ┆ fonctionnelle, ┆          │
 │         ┆                 ┆           ┆                 ┆            ┆ …              ┆          │
 │ …       ┆ …               ┆ …         ┆ …               ┆ …          ┆ …              ┆ …        │
 │ ZZQX200 ┆ EXAM HISTOPATH  ┆ 0         ┆ 0               ┆ 2014-04-14 ┆ Examen histopa ┆ null     │
 │         ┆ BIOPSIES ÉTAGÉS ┆           ┆                 ┆            ┆ thologique de  ┆          │
 │         ┆ 2…              ┆           ┆                 ┆            ┆ biop…          ┆          │
 │ ZZQX217 ┆ EXAM HISTOPATH  ┆ 0         ┆ 0               ┆ 2014-04-14 ┆ Examen histopa ┆ null     │
 │         ┆ BIOPSIES 1      ┆           ┆                 ┆            ┆ thologique de  ┆          │
 │         ┆ STRUCT…         ┆           ┆                 ┆            ┆ biop…          ┆          │
 │ ZZQX603 ┆ TEST DETECT     ┆ 0         ┆ 0               ┆ 2020-02-18 ┆ Test de        ┆ null     │
 │         ┆ GENOME          ┆           ┆                 ┆            ┆ détection du   ┆          │
 │         ┆ PAPILLOMAVIRU…  ┆           ┆                 ┆            ┆ génome des …   ┆          │
 │ ZZQX628 ┆ TEST DETECT     ┆ 0         ┆ 0               ┆ 2020-02-18 ┆ Test de        ┆ null     │
 │         ┆ GENOME          ┆           ┆                 ┆            ┆ détection du   ┆          │
 │         ┆ PAPILLOMAVIRU…  ┆           ┆                 ┆            ┆ génome des …   ┆          │
 └─────────┴─────────────────┴───────────┴─────────────────┴────────────┴────────────────┴──────────┘,
 shape: (9_546, 12)
 ┌───────┬────────────┬────────────┬────────────┬───┬────────────┬───────────┬───────────┬──────────┐
 │ id    ┆ orphanumbe ┆ expertlink ┆ name       ┆ … ┆ omim       ┆ umls      ┆ mesh      ┆ meddra   │
 │ ---   ┆ r          ┆ ---        ┆ ---        ┆   ┆ ---        ┆ ---       ┆ ---       ┆ ---      │
 │ str   ┆ ---        ┆ str        ┆ str        ┆   ┆ str        ┆ str       ┆ str       ┆ str      │
 │       ┆ str        ┆            ┆            ┆   ┆            ┆           ┆           ┆          │
 ╞═══════╪════════════╪════════════╪════════════╪═══╪════════════╪═══════════╪═══════════╪══════════╡
 │ 3555  ┆ 5          ┆ http://www ┆ Déficit en ┆ … ┆ 609016     ┆ C0342786  ┆ null      ┆ null     │
 │       ┆            ┆ .orpha.net ┆ 3-hydroxya ┆   ┆            ┆ ;         ┆           ┆          │
 │       ┆            ┆ /consor/cg ┆ cyl-CoA    ┆   ┆            ┆ C1969443  ┆           ┆          │
 │       ┆            ┆ i-…        ┆ dés…       ┆   ┆            ┆           ┆           ┆          │
 │ 3297  ┆ 6          ┆ http://www ┆ Déficit en ┆ … ┆ 210200 ;   ┆ C0268600  ┆ C535308   ┆ null     │
 │       ┆            ┆ .orpha.net ┆ 3-méthylcr ┆   ┆ 210210     ┆           ┆           ┆          │
 │       ┆            ┆ /consor/cg ┆ otonyl-CoA ┆   ┆            ┆           ┆           ┆          │
 │       ┆            ┆ i-…        ┆ …          ┆   ┆            ┆           ┆           ┆          │
 │ 1242  ┆ 7          ┆ http://www ┆ Syndrome   ┆ … ┆ 220210 ;   ┆ C0796137  ┆ C535313   ┆ null     │
 │       ┆            ┆ .orpha.net ┆ 3C         ┆   ┆ 300963     ┆           ┆           ┆          │
 │       ┆            ┆ /consor/cg ┆            ┆   ┆            ┆           ┆           ┆          │
 │       ┆            ┆ i-…        ┆            ┆   ┆            ┆           ┆           ┆          │
 │ 335   ┆ 8          ┆ http://www ┆ Syndrome   ┆ … ┆ null       ┆ C3266843  ┆ C535317 ; ┆ 10056894 │
 │       ┆            ┆ .orpha.net ┆ 47,XYY     ┆   ┆            ┆ ;         ┆ D014997   ┆          │
 │       ┆            ┆ /consor/cg ┆            ┆   ┆            ┆ C0043379  ┆           ┆          │
 │       ┆            ┆ i-…        ┆            ┆   ┆            ┆           ┆           ┆          │
 │ …     ┆ …          ┆ …          ┆ …          ┆ … ┆ …          ┆ …         ┆ …         ┆ …        │
 │ 26574 ┆ 508523     ┆ http://www ┆ Hyperphény ┆ … ┆ null       ┆ null      ┆ null      ┆ null     │
 │       ┆            ┆ .orpha.net ┆ lalaninémi ┆   ┆            ┆           ┆           ┆          │
 │       ┆            ┆ /consor/cg ┆ e due à un ┆   ┆            ┆           ┆           ┆          │
 │       ┆            ┆ i-…        ┆ d…         ┆   ┆            ┆           ┆           ┆          │
 │ 26575 ┆ 508529     ┆ http://www ┆ Epidermoly ┆ … ┆ null       ┆ null      ┆ null      ┆ null     │
 │       ┆            ┆ .orpha.net ┆ se         ┆   ┆            ┆           ┆           ┆          │
 │       ┆            ┆ /consor/cg ┆ bulleuse   ┆   ┆            ┆           ┆           ┆          │
 │       ┆            ┆ i-…        ┆ simple     ┆   ┆            ┆           ┆           ┆          │
 │       ┆            ┆            ┆ bas…       ┆   ┆            ┆           ┆           ┆          │
 │ 26576 ┆ 508533     ┆ http://www ┆ Syndrome   ┆ … ┆ null       ┆ null      ┆ null      ┆ null     │
 │       ┆            ┆ .orpha.net ┆ de         ┆   ┆            ┆           ┆           ┆          │
 │       ┆            ┆ /consor/cg ┆ dysplasie  ┆   ┆            ┆           ┆           ┆          │
 │       ┆            ┆ i-…        ┆ squelettiq ┆   ┆            ┆           ┆           ┆          │
 │       ┆            ┆            ┆ …          ┆   ┆            ┆           ┆           ┆          │
 │ 26578 ┆ 508542     ┆ http://www ┆ Syndrome   ┆ … ┆ null       ┆ null      ┆ null      ┆ null     │
 │       ┆            ┆ .orpha.net ┆ de pancyto ┆   ┆            ┆           ┆           ┆          │
 │       ┆            ┆ /consor/cg ┆ pénie      ┆   ┆            ┆           ┆           ┆          │
 │       ┆            ┆ i-…        ┆ progres…   ┆   ┆            ┆           ┆           ┆          │
 └───────┴────────────┴────────────┴────────────┴───┴────────────┴───────────┴───────────┴──────────┘,
 shape: (44_055, 12)
 ┌──────┬────────┬────────────────────┬─────────────┬───┬───────────┬────────────┬─────────┬────────┐
 │ ghs  ┆ ghm    ┆ libelle_ghm        ┆ borne_basse ┆ … ┆ tarif_exh ┆ date_effet ┆ anseqta ┆ time_i │
 │ ---  ┆ ---    ┆ ---                ┆ ---         ┆   ┆ ---       ┆ ---        ┆ ---     ┆ ---    │
 │ str  ┆ str    ┆ str                ┆ i64         ┆   ┆ f64       ┆ str        ┆ str     ┆ str    │
 ╞══════╪════════╪════════════════════╪═════════════╪═══╪═══════════╪════════════╪═════════╪════════╡
 │ 0022 ┆ 01C031 ┆ Craniotomies pour  ┆ 4           ┆ … ┆ 116.2     ┆ 01/03/2010 ┆ 2010    ┆ 2010   │
 │      ┆        ┆ traumatisme, â…    ┆             ┆   ┆           ┆            ┆         ┆        │
 │ 0023 ┆ 01C032 ┆ Craniotomies pour  ┆ 7           ┆ … ┆ 87.53     ┆ 01/03/2010 ┆ 2010    ┆ 2010   │
 │      ┆        ┆ traumatisme, â…    ┆             ┆   ┆           ┆            ┆         ┆        │
 │ 0024 ┆ 01C033 ┆ Craniotomies pour  ┆ 7           ┆ … ┆ 69.99     ┆ 01/03/2010 ┆ 2010    ┆ 2010   │
 │      ┆        ┆ traumatisme, â…    ┆             ┆   ┆           ┆            ┆         ┆        │
 │ 0025 ┆ 01C034 ┆ Craniotomies pour  ┆ 12          ┆ … ┆ 241.16    ┆ 01/03/2010 ┆ 2010    ┆ 2010   │
 │      ┆        ┆ traumatisme, â…    ┆             ┆   ┆           ┆            ┆         ┆        │
 │ …    ┆ …      ┆ …                  ┆ …           ┆ … ┆ …         ┆ …          ┆ …       ┆ …      │
 │ 9631 ┆ 28Z23Z ┆ Techniques         ┆ 0           ┆ … ┆ 0.0       ┆ 01/03/2023 ┆ 2023    ┆ 2023   │
 │      ┆        ┆ complexes          ┆             ┆   ┆           ┆            ┆         ┆        │
 │      ┆        ┆ d'irradiati…       ┆             ┆   ┆           ┆            ┆         ┆        │
 │ 9632 ┆ 28Z24Z ┆ Techniques         ┆ 0           ┆ … ┆ 0.0       ┆ 01/03/2023 ┆ 2023    ┆ 2023   │
 │      ┆        ┆ complexes          ┆             ┆   ┆           ┆            ┆         ┆        │
 │      ┆        ┆ d'irradiati…       ┆             ┆   ┆           ┆            ┆         ┆        │
 │ 9633 ┆ 28Z25Z ┆ Autres techniques  ┆ 0           ┆ … ┆ 0.0       ┆ 01/03/2023 ┆ 2023    ┆ 2023   │
 │      ┆        ┆ d'irradiation …    ┆             ┆   ┆           ┆            ┆         ┆        │
 │ 9639 ┆ 28Z11Z ┆ Techniques         ┆ 0           ┆ … ┆ 0.0       ┆ 01/03/2023 ┆ 2023    ┆ 2023   │
 │      ┆        ┆ spéciales          ┆             ┆   ┆           ┆            ┆         ┆        │
 │      ┆        ┆ d'irradiati…       ┆             ┆   ┆           ┆            ┆         ┆        │
└───────┴────────────┴────────────┴────────────┴───┴────────────┴───────────┴───────────┴──────────-┘ 
```

## Listes de requêtes / méthodes

```python
rp.get_liste('chip')
````

```
{'nom': ['Chimiothérapie hyperthermique intra-péritonéale (CHIP)'],
 'abrege': ['chip'],
 'thematique': ['Recours Exceptionnel'],
 'actes': ['HPLB003'],
 'date_saisie': ['2017-04-23T22:00:00Z'],
 'auteur': ['DGOS - ATIH'],
 'timestamp': [1493282250]}
```


```python
rp.get_liste('cathe_cardiaque_interv_pediatrique_cardiopathie_congenitales')
```

```
{'nom': ['Cathétérisme cardiaque interventionnel pédiatrique pour cardiopathies congénitales'],
 'abrege': ['cathe_cardiaque_interv_pediatrique_cardiopathie_congenitales'],
 'thematique': ['Recours Exceptionnel'],
 'agemax': [15],
 'diags': ['Q20', 'Q21', 'Q22', 'Q23', 'Q24', 'Q25', 'Q26'],
 'positions_diags': ['toutes'],
 'actes': ['DAAF001',
  'DAAF002',
  'DAGF001',
  'DAHF001',
  'DAMF001',
  'DASF003',
  'DBAF001',
  'DBAF002',
  'DBAF003',
  'DBAF004',
  'DBAF005',
  'DBLF009',
  'DGAF001',
  'DGAF003',
  'DGAF004',
  'DGAF006',
  'DGAF007',
  'DGLF003',
  'EZGF001'],
 'date_saisie': ['2017-04-23T22:00:00Z'],
 'commentaire': ["Catégories d'âge suivantes : { [0 - 28 jours] ; [29 jours ; 1 an[ ; [1 an ; 5 ans] ; [6 ans ; 15 ans ] }"],
 'auteur': ['DGOS - ATIH'],
 'timestamp': [1493282163]}
```

