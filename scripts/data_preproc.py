import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de gráficos
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# Crear carpeta para guardar los gráficos si no existe
output_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "../reports/graficos/preprocessing")
os.makedirs(output_dir, exist_ok=True)

def preprocess_data(data):
    """
    Limpia y transforma el conjunto de datos.
    Args:
        data (pd.DataFrame): Datos originales.
    Returns:
        pd.DataFrame: Datos preprocesados.
    """
    print("[INFO] Iniciando preprocesamiento...")

    # 1. Manejo de valores duplicados
    print("[INFO] Eliminando filas duplicadas...")
    initial_rows = data.shape[0]
    data = data.drop_duplicates()
    print(f"[INFO] Filas duplicadas eliminadas. Filas antes: {initial_rows}, después: {data.shape[0]}.")

    # 2. Manejo de valores nulos y faltantes
    print("[INFO] Manejo de valores nulos...")
    for col in ["Units_Sold", "Unit_Price"]:
        if data[col].isnull().sum() > 0:
            median_value = data[col].median()
            data[col].fillna(median_value, inplace=True)
            print(f"[INFO] Columna '{col}': valores nulos rellenados con la mediana ({median_value}).")

    # 3. Conversión a tipo numérico
    print("[INFO] Convirtiendo 'Units_Sold' y 'Unit_Price' a valores numéricos...")
    data["Units_Sold"] = pd.to_numeric(data["Units_Sold"], errors="coerce")
    data["Unit_Price"] = pd.to_numeric(data["Unit_Price"], errors="coerce")

    # 4. Codificación de variables categóricas
    print("[INFO] Codificando variables categóricas (One-Hot Encoding)...")
    data = pd.get_dummies(data, columns=["Store", "Category"], drop_first=True)
    print("[INFO] Variables categóricas codificadas correctamente.")

    # 5. Generación de columna Total_Sales
    print("[INFO] Generando la columna 'Total_Sales'...")
    data["Total_Sales"] = data["Units_Sold"] * data["Unit_Price"]
    print("[INFO] Columna 'Total_Sales' generada correctamente.")

    # 6. Normalización de características numéricas
    print("[INFO] Normalizando características numéricas...")
    numeric_cols = ["Units_Sold", "Unit_Price", "Total_Sales"]
    scaler = StandardScaler()
    data[numeric_cols] = scaler.fit_transform(data[numeric_cols])
    print("[INFO] Normalización completada.")

    # 7. Guardar el DataFrame limpio en un archivo CSV
    output_file_path = "../data/sales_data_cleaned.csv"
    data.to_csv(output_file_path, index=False)
    print(f"[INFO] Archivo con datos preprocesados guardado en: {output_file_path}")

    # 8. Visualizaciones
    print("[INFO] Generando visualizaciones...")

    # Distribución de 'Total_Sales'
    sns.histplot(data["Total_Sales"], kde=True, bins=30)
    plt.title("Distribución de Ventas Totales (Normalización)")
    plt.xlabel("Total Sales")
    plt.ylabel("Frecuencia")
    plt.savefig(os.path.join(output_dir, "distribucion_total_sales.png"))
    plt.show()

    # Heatmap de correlación
    numeric_data = data.apply(pd.to_numeric, errors="coerce")
    sns.heatmap(numeric_data.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Heatmap de Correlación")
    plt.savefig(os.path.join(output_dir, "heatmap_correlacion.png"))
    plt.show()

    # Boxplot de 'Units_Sold'
    sns.boxplot(y=data["Units_Sold"], color="skyblue")
    plt.title("Boxplot de Units_Sold")
    plt.savefig(os.path.join(output_dir, "boxplot_units_sold.png"))
    plt.show()

    print("[INFO] Preprocesamiento completado con éxito.")
    return data


# Punto de entrada principal para ejecutar el preprocesamiento
if __name__ == "__main__":
    # Ruta al archivo original
    input_file_path = "../data/sales_data.csv"

    # Verificar si el archivo existe
    if not os.path.exists(input_file_path):
        print(f"[ERROR] El archivo '{input_file_path}' no existe.")
    else:
        print(f"[INFO] Cargando datos desde: {input_file_path}")
        raw_data = pd.read_csv(input_file_path, delimiter=",", encoding="latin1", quotechar='"')

        # Llamar a la función de preprocesamiento
        cleaned_data = preprocess_data(raw_data)
        print("[INFO] Script de preprocesamiento finalizado.")
