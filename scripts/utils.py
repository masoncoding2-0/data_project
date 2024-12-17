import matplotlib.pyplot as plt
import seaborn as sns

def plot_distribution(data, column):
    sns.histplot(data[column], kde=True)
    plt.title(f"Distribución de {column}")
    plt.show()

def plot_correlation_matrix(data):
    correlation_matrix = data.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
    plt.title("Matriz de Correlación")
    plt.show()
