import pandas as pd

def preprocess_data(data_path):
    print("[INFO] Cargando datos...")
    data = pd.read_excel(data_path)

    print("[INFO] Preprocesando datos...")
    # Limpieza y manejo de valores nulos
    data = data.drop_duplicates()
    data = data.fillna(data.median())

    # Retorna los datos limpios
    return data
