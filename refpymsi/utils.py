import os



def get_data_path() -> str:
    """Récupère le chemin du répertoire data"""

    folder = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(folder, "data")
    return path


