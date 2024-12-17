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
