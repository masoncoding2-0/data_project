from scripts.data_preproc import preprocess_data
from scripts.model_training import train_model, evaluate_model

class DataPipeline:
    def __init__(self, data_path):
        self.data_path = data_path
        self.data = None
        self.model = None

    def run(self):
        # Paso 1: Preprocesamiento de datos
        self.data = preprocess_data(self.data_path)

        # Paso 2: Entrenamiento del modelo
        self.model = train_model(self.data)

        # Paso 3: Evaluación del modelo
        evaluate_model(self.model, self.data)

if __name__ == "__main__":
    pipeline = DataPipeline(data_path="data/sales_data.xlsx")
    pipeline.run()
