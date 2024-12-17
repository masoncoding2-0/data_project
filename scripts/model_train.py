from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error

def train_model(data):
    print("[INFO] Entrenando modelo...")
    # Separar características y variable objetivo
    X = data.drop(columns=["Units_Sold"])
    y = data["Units_Sold"]

    # Dividir en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Entrenar un modelo de regresión lineal
    model = LinearRegression()
    model.fit(X_train, y_train)

    return model

def evaluate_model(model, data):
    print("[INFO] Evaluando modelo...")
    X = data.drop(columns=["Units_Sold"])
    y = data["Units_Sold"]

    y_pred = model.predict(X)
    rmse = mean_squared_error(y, y_pred, squared=False)
    mae = mean_absolute_error(y, y_pred)

    print(f"RMSE: {rmse}")
    print(f"MAE: {mae}")
