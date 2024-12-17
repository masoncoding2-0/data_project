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
│   ├── sales_data_cleaned.csv # Archivo de datos de ventas limpio de duplicados
│   └── sales_data.xlsx  # Archivo de datos de ventas.
├── notebooks/
│   ├── eda.ipynb        # Análisis exploratorio de datos.
│   ├── date_preproc.ipynb        # Preprocesamiento de Datos
│   ├── informe_final.ipynb        # Informe de Interpretación de Resultados y Recomendaciones.
│   └── model.ipynb        #  Modelo Predictivo y Evaluación.
├── scripts/
│   ├── data_preprocessing.py  # Limpieza y transformación.
│   ├── eda.py          # Análisis Exploratorio de Datos (EDA)
│   ├── model_training.py      # Entrenamiento del modelo.
│   └── utils.py               # Funciones reutilizables.
├── reports/
│   ├── graficos
│   │  ├── eda          # Gráficos del Análisis exploratorio de Datos. 
│   │  ├── mpe          # Gráficos del modelo predictivo
│   │  └── preprocessing        # Gráficos de preprocesamiento de datos
│   └── PDF
│   │  ├── eda         # Informe del EDA en HTML y PDF.
│   │  ├── mpe         # Informe del Modelo predictivo y evaluación en HTML y PDF.
│   │  └── resrec      # Informe Final de Interpretación de Resultados y Recomendaciones
├── models/
│   └── sales_predictor_model_best.pkl # Modelo predictor entrenado con el mejor modelo.
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
