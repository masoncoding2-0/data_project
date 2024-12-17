## **Proyecto de Pipeline de Datos de Ventas**  
Este proyecto procesa y analiza datos de ventas de tiendas, realizando limpieza, transformación y exploración de relaciones entre las variables.  

---

### 📋 **Configuración del Entorno Virtual**  
Antes de ejecutar el proyecto, asegúrate de configurar tu entorno virtual y las dependencias necesarias.

1. **Crear el entorno virtual**  
   ```bash
   python -m venv env
   ```

2. **Activar el entorno virtual**  
   - En Linux/Mac:  
     ```bash
     source env/bin/activate
     ```
   - En Windows:  
     ```bash
     env\Scripts\activate
     ```

3. **Instalar las dependencias**  
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn jupyter
   ```

4. **Guardar dependencias**  
   ```bash
   pip freeze > requirements.txt
   ```
5. **Instalar dependencia openpyxl si es necesario hacerlos de forma independiente.**  
   ```bash
   pip install openpyxl
   ```
---

### 📂 **Estructura del Proyecto**  
La estructura de carpetas y archivos está organizada de la siguiente manera:

```bash
/data_pipeline_project
├── data/
│   └── sales_data.xlsx  # Archivo de datos de ventas.
├── notebooks/
│   └── eda.ipynb        # Análisis exploratorio de datos.
├── scripts/
│   ├── data_preprocessing.py  # Limpieza y transformación.
│   ├── model_training.py      # Entrenamiento del modelo.
│   └── utils.py               # Funciones reutilizables.
├── reports/
│   └── eda_report.pdf         # Reporte en formato PDF.
├── main.py                    # Script principal del pipeline.
└── requirements.txt           # Dependencias del proyecto.
```

---

### 📜 **Descripción del Conjunto de Datos**  
El archivo `sales_data.xlsx` contiene información sobre ventas con las siguientes características:

| **Columna**     | **Descripción**                                                                 |
|------------------|-------------------------------------------------------------------------------|
| **Date**        | Fecha de venta (almacenada como texto, debe convertirse a `datetime`).        |
| **Store**       | Identificador de la tienda (variable categórica).                             |
| **Category**    | Categoría del producto (Electronics, Clothing, Home Goods).                   |
| **Units_Sold**  | Número de unidades vendidas (almacenada como texto, convertir a numérico).    |
| **Unit_Price**  | Precio por unidad (almacenado como texto, convertir a numérico).              |

---

### 📊 **Patrones y Observaciones Principales**  

#### Fase 1:

1. **Estructura de los Datos**  
   - **Fechas**: 19 fechas únicas, siendo **2024-01-03** la más frecuente (9 repeticiones).  
   - **Tiendas**: 3 tiendas únicas, con la tienda **103** siendo la más frecuente (38 registros).  
   - **Categorías**: 3 categorías ("Electronics", "Clothing", "Home Goods"). La más repetida: **Home Goods** (38 registros).  
   - **Valores Numéricos**:  
     - **Units_Sold**: Mínimos valores de venta (~20 unidades), con 25 unidades siendo el valor más frecuente.  
     - **Unit_Price**: Solo **3 precios diferentes**, siendo **19.99** el más frecuente.  

2. **Duplicados**  
   - Existen **55 filas duplicadas**. Se requiere decidir si eliminarlas o validarlas.  

3. **Valores Faltantes**  
   - No hay valores faltantes en ninguna columna.  

4. **Observaciones de Visualización**  
   - La distribución de **Units_Sold** tiene ligera concentración en valores bajos.  
   - **Unit_Price** muestra únicamente 3 precios, sugiriendo baja variación.  

5. **Posibles Relaciones**  
   - **Precio vs. Ventas**: Los productos más caros parecen tener menos unidades vendidas (requiere confirmación).  
   - **Tendencia Temporal**: Se analizarán patrones estacionales en ventas durante la fase de modelado.  

# Fase 2: Explicación del Código

### Código en `data_preprocessing.py`
#### 1. Eliminar duplicados
- **`data.drop_duplicates()`**:
  - Elimina las filas duplicadas del DataFrame.
  - Se imprime la cantidad de filas duplicadas eliminadas.

#### 2. Manejo de valores nulos
- Las columnas `Units_Sold` y `Unit_Price` se convierten a tipo numérico con:
  ```python
  pd.to_numeric
  ```
- Los valores nulos se rellenan con la **mediana** de cada columna usando:
  ```python
  .fillna()
  ```

#### 3. Conversión de fechas
- La columna `Date` se convierte al tipo `datetime` con:
  ```python
  pd.to_datetime
  ```

#### 4. Codificación de variables categóricas
- Se utiliza **`pd.get_dummies()`** para convertir las columnas `Store` y `Category` en variables binarias.
- El parámetro `drop_first=True` evita la multicolinealidad eliminando la categoría de referencia.

#### 5. Generación de nuevas características
- Se crea una nueva columna `Total_Sales` calculada como:
  ```python
  Units_Sold * Unit_Price
  ```

---

### Código en `eda.ipynb`
#### 1. Configuración del entorno
- Importación de bibliotecas esenciales:
  ```python
  import pandas as pd
  import seaborn as sns
  import matplotlib.pyplot as plt
  ```
- Configuración de gráficos:
  ```python
  sns.set_theme()
  plt.rcParams['figure.figsize'] = (10, 6)
  ```

#### 2. Cargar los datos
- Se utiliza **`pd.read_csv()`** para cargar el archivo CSV:
  ```python
  data = pd.read_csv('data/sales_data.csv')
  ```
- Si las columnas no se separan correctamente, se ajustan usando:
  ```python
  .str.split()
  ```

#### 3. Importar y aplicar `preprocess_data`
- Se importa la función `preprocess_data` desde el script `data_preprocessing.py`:
  ```python
  from scripts.data_preprocessing import preprocess_data
  ```
- Se aplica la función a los datos:
  ```python
  clean_data = preprocess_data(data)
  ```

#### 4. Visualización
- Se genera un histograma de la nueva columna `Total_Sales`:
  ```python
  sns.histplot(clean_data['Total_Sales'], bins=30)
  plt.title('Distribución de Ventas Totales')
  plt.show()
  ```
---


### 🚀 **Ejecución del Proyecto**  
1. Asegúrate de tener activado el entorno virtual.  
2. Coloca el archivo `sales_data.xlsx` en la carpeta **data**.  
3. Ejecuta el script principal:  
   ```bash
   python main.py
   ```

---

### 📈 **Análisis Exploratorio de Datos (EDA)**  
El archivo `notebooks/eda.ipynb` contiene el análisis exploratorio detallado, que incluye:  
- Limpieza de datos.  
- Visualización de distribuciones.  
- Análisis de duplicados y valores faltantes.  
- Gráficos para observar tendencias y correlaciones.  

---

### 🛠 **Scripts Principales**  
- **data_preprocessing.py**: Limpieza y transformación de los datos.  
- **model_training.py**: Entrenamiento del modelo de predicción.  
- **utils.py**: Funciones auxiliares reutilizables.  

---

### 🛪 **Notas Finales**  
- Este pipeline es una base que puede extenderse hacia la implementación de modelos predictivos o dashboards interactivos.  
- Asegúrate de tener todas las dependencias instaladas correctamente.  

---
