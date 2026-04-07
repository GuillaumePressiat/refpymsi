import os


def get_data_path() -> str:
    """Récupère le chemin du répertoire data"""

    folder = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(folder, "data")
    return path


def list_available_tables() -> list:
    """Liste toutes les tables disponibles"""
    import glob
    tables_path = os.path.join(get_data_path(), "tables")
    # Enlever l'extension .json.gz et le chemin
    tables = [os.path.basename(f).replace('.json.gz', '') 
              for f in glob.glob(os.path.join(tables_path, "*.json.gz"))]
    return sorted(tables)


def list_available_listes() -> list:
    """Liste toutes les listes disponibles"""
    import glob
    listes_path = os.path.join(get_data_path(), "listes")
    # Enlever l'extension .json et le chemin
    listes = [os.path.basename(f).replace('.json', '') 
               for f in glob.glob(os.path.join(listes_path, "*.json"))]
    return sorted(listes)