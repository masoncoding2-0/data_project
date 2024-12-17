import pandas as pd

def preprocess_data(data):
    """
    Función para limpiar y preparar los datos.
    Args:
        data (pd.DataFrame): DataFrame original.
    Returns:
        pd.DataFrame: DataFrame limpio y preprocesado.
    """
    print("[INFO] Iniciando preprocesamiento de datos...")

    # 1. Eliminar filas duplicadas
    data_cleaned = data.drop_duplicates()
    print(f"[INFO] Filas duplicadas eliminadas: {data.shape[0] - data_cleaned.shape[0]}")

    # 2. Manejo de valores nulos
    # Para columnas numéricas: rellenar con la mediana
    for col in ["Units_Sold", "Unit_Price"]:
        data_cleaned[col] = pd.to_numeric(data_cleaned[col], errors="coerce")  # Asegurar numérico
        median_value = data_cleaned[col].median()
        data_cleaned[col].fillna(median_value, inplace=True)
        print(f"[INFO] Valores nulos en '{col}' rellenados con la mediana: {median_value}")

    # 3. Convertir fechas a datetime
    data_cleaned["Date"] = pd.to_datetime(data_cleaned["Date"], errors="coerce")
    print("[INFO] Columna 'Date' convertida a formato datetime.")

    # 4. Codificación de variables categóricas
    data_encoded = pd.get_dummies(data_cleaned, columns=["Store", "Category"], drop_first=True)
    print("[INFO] Variables categóricas codificadas con One-Hot Encoding.")

    # 5. Generación de nuevas características
    data_encoded["Total_Sales"] = data_encoded["Units_Sold"] * data_encoded["Unit_Price"]
    print("[INFO] Nueva columna 'Total_Sales' generada.")

    print("[INFO] Preprocesamiento completado con éxito.")
    return data_encoded

