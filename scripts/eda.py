import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def perform_eda(file_path):
    """
    Realiza el análisis exploratorio de datos (EDA).
    Args:
        file_path (str): Ruta al archivo CSV.
    """
    # Cargar los datos
    data = pd.read_csv(file_path, delimiter=",", encoding="latin1", quotechar='"')

    # Estadísticas descriptivas
    print("[INFO] Estadísticas descriptivas:")
    stats = data.describe()
    print(stats)

    # Crear la carpeta para guardar los gráficos si no existe
    output_dir = '../reports/graficos/eda'
    os.makedirs(output_dir, exist_ok=True)

    # Visualización de la distribución de Unidades Vendidas
    sns.histplot(data["Units_Sold"], kde=True, bins=30)
    plt.title("Distribución de Unidades Vendidas")
    plt.xlabel("Units Sold")
    plt.ylabel("Frecuencia")
    plt.savefig(os.path.join(output_dir, 'distribucion_units_sold.png'))  # Guardamos la gráfica
    plt.show()

    # Análisis de correlaciones
    print("[INFO] Correlaciones entre las variables numéricas:")
    
    # Seleccionar solo columnas numéricas
    numeric_data = data.select_dtypes(include=['number'])

    # Lidiar con valores NaN: rellenarlos con la mediana
    numeric_data = numeric_data.fillna(numeric_data.median())

    # Calcular la matriz de correlación
    correlation_matrix = numeric_data.corr()

    # Visualización del heatmap de correlación
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Heatmap de Correlación entre Variables")
    plt.savefig(os.path.join(output_dir, 'heatmap_correlacion.png'))  # Guardamos la gráfica
    plt.show()

    # Boxplot de valores atípicos en 'Units_Sold'
    sns.boxplot(y=data["Units_Sold"], color="skyblue")
    plt.title("Boxplot de Units_Sold")
    plt.savefig(os.path.join(output_dir, 'boxplot_units_sold.png'))  # Guardamos la gráfica
    plt.show()

    print("[INFO] EDA completado con éxito.")

# Ejecutar el EDA
file_path = "../data/sales_data.csv"
perform_eda(file_path)
