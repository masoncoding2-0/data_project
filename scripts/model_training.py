import pandas as pd
from sklearn.linear_model import Ridge, LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import joblib
import os

# Cargar los datos
data = pd.read_csv("../data/sales_data_cleaned.csv")

# Preprocesar los datos
X = data.drop(columns=["Total_Sales", "Date"])  # Asegúrate de eliminar la columna Target
y = data["Total_Sales"]

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalización de las características numéricas
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Definir los modelos
models = {
    "Ridge Regression": Ridge(),
    "Linear Regression": LinearRegression(),
    "Decision Tree Regressor": DecisionTreeRegressor(random_state=42)
}

# Definir los hiperparámetros para el GridSearch
param_grid = {
    'Ridge Regression': {
        'alpha': [0.1, 1.0, 10.0, 100.0],  # Valores para el parámetro de regularización
        'fit_intercept': [True, False]  # Incluir o no el intercepto en el modelo
    },
    'Linear Regression': {
        'fit_intercept': [True, False]  # Ajuste del intercepto
    },
    'Decision Tree Regressor': {
        'max_depth': [5, 10, 15, 20],
        'min_samples_split': [2, 5, 10]
    }
}

# Usar GridSearchCV para encontrar el mejor modelo para cada uno
best_models = {}
for model_name, model in models.items():
    print(f"[INFO] Entrenando {model_name}...")
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid[model_name], cv=5, scoring='neg_mean_squared_error')
    grid_search.fit(X_train, y_train)

    # Guardar el mejor modelo
    best_models[model_name] = grid_search.best_estimator_
    print(f"[INFO] Mejores parámetros para {model_name}: {grid_search.best_params_}")

    # Evaluación del modelo
    y_pred = grid_search.best_estimator_.predict(X_test)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"[INFO] {model_name} - RMSE: {rmse:.2f}, MAE: {mae:.2f}, R²: {r2:.2f}")

# Selección del mejor modelo basado en el RMSE (puedes ajustarlo a otros criterios)
best_model_name = min(best_models, key=lambda model: mean_squared_error(y_test, best_models[model].predict(X_test), squared=False))
best_model = best_models[best_model_name]

# Evaluación final del mejor modelo
y_pred_best = best_model.predict(X_test)
rmse_best = mean_squared_error(y_test, y_pred_best, squared=False)
mae_best = mean_absolute_error(y_test, y_pred_best)
r2_best = r2_score(y_test, y_pred_best)

print(f"[INFO] Mejor modelo: {best_model_name}")
print(f"[INFO] Evaluación final del mejor modelo - RMSE: {rmse_best:.2f}, MAE: {mae_best:.2f}, R²: {r2_best:.2f}")

# Guardar el modelo entrenado optimizado para su reutilización
model_filename = '../models/sales_predictor_model_best.pkl'
joblib.dump(best_model, model_filename)
print(f"[INFO] El modelo entrenado ha sido guardado en: {model_filename}")

# Verificación de la carga del modelo
loaded_model = joblib.load(model_filename)

