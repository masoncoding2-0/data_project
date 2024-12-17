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

    # i. Manejo de valores duplicados
    print("[INFO] Eliminando filas duplicadas...")
    initial_rows = data.shape[0]
    data = data.drop_duplicates()  # Eliminar duplicados
    print(f"[INFO] Filas duplicadas eliminadas. Filas antes: {initial_rows}, después: {data.shape[0]}.")

    # ii. Manejo de valores nulos y faltantes
    print("[INFO] Manejo de valores nulos...")
    # Rellenamos los valores nulos con la mediana en las columnas numéricas
    for col in ["Units_Sold", "Unit_Price"]:
        if data[col].isnull().sum() > 0:
            median_value = data[col].median()
            data[col].fillna(median_value, inplace=True)
            print(f"[INFO] Columna '{col}': valores nulos rellenados con la mediana ({median_value}).")
    
    # Asegurarnos de que las columnas 'Units_Sold' y 'Unit_Price' sean numéricas
    print("[INFO] Convirtiendo 'Units_Sold' y 'Unit_Price' a valores numéricos...")
    data["Units_Sold"] = pd.to_numeric(data["Units_Sold"], errors="coerce")
    data["Unit_Price"] = pd.to_numeric(data["Unit_Price"], errors="coerce")

    # Si después de la conversión hay NaN, rellenarlos con la mediana
    data["Units_Sold"].fillna(data["Units_Sold"].median(), inplace=True)
    data["Unit_Price"].fillna(data["Unit_Price"].median(), inplace=True)
    
    # iii. Codificación de variables categóricas
    print("[INFO] Codificando variables categóricas (One-Hot Encoding)...")
    # Utilizamos One-Hot Encoding para las variables 'Store' y 'Category'
    data = pd.get_dummies(data, columns=["Store", "Category"], drop_first=True)
    print("[INFO] Variables categóricas codificadas. Se eliminaron las categorías base.")

    # iv. Generación de nueva columna Total_Sales
    print("[INFO] Generando la columna 'Total_Sales'...")
    data["Total_Sales"] = data["Units_Sold"] * data["Unit_Price"]
    print("[INFO] Columna 'Total_Sales' generada correctamente.")

    # v. Normalización de las características numéricas
    print("[INFO] Normalizando las características numéricas...")
    # Selección de columnas a normalizar
    numeric_cols = ["Units_Sold", "Unit_Price", "Total_Sales"]
    scaler = StandardScaler()
    data[numeric_cols] = scaler.fit_transform(data[numeric_cols])
    print("[INFO] Normalización completada.")

    # Mostrar estadísticas descriptivas
    print("[INFO] Estadísticas descriptivas de los datos preprocesados:")
    print(data.describe())

    # Visualización de la distribución de 'Total_Sales'
    print("\n### Visualización: Distribución de Total_Sales")
    sns.histplot(data["Total_Sales"], kde=True, bins=30)
    plt.title("Distribución de Ventas Totales (Normalización)")
    plt.xlabel("Total Sales")
    plt.ylabel("Frecuencia")
    plt.savefig(os.path.join(output_dir, "distribucion_total_sales.png"))  # Guardamos el gráfico
    plt.show()

    # Heatmap de correlación
    print("\n### Visualización: Correlación entre Variables")
    numeric_data = data.apply(pd.to_numeric, errors="coerce")
    sns.heatmap(numeric_data.corr(), annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Heatmap de Correlación")
    plt.savefig(os.path.join(output_dir, "heatmap_correlacion.png"))  # Guardamos el gráfico
    plt.show()

    # Boxplot de valores atípicos en 'Units_Sold'
    print("\n### Visualización: Boxplot de Valores Atípicos")
    sns.boxplot(y=data["Units_Sold"], color="skyblue")
    plt.title("Boxplot de Units_Sold")
    plt.savefig(os.path.join(output_dir, "boxplot_units_sold.png"))  # Guardamos el gráfico
    plt.show()

    print("[INFO] Preprocesamiento completado con éxito.")
    return data
