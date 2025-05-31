from models_imputers_scalers import load_models
from dto import wine_features_dto as dto
import numpy as np


def predict(values: list, wine_type: str):

    MODELS = load_models.load_all_models()

    model, imp, scaler = MODELS[wine_type]

    arr = np.array(values).reshape(1, -1)

    # Imputar datos faltantes (np.nan)
    arr_imp = imp.transform(arr)
    # Escalar
    arr_sc = scaler.transform(arr_imp)

    # Predecir y desescalar
    pred = model.predict(arr_sc)[0][0]

    # Limitar rango
    pred = np.clip(pred, 0, 10)

    # Categorizar
    if pred < 5:
        cat = "Malo"
    elif pred < 7:
        cat = "Regular"
    else:
        cat = "Bueno"

    return pred, cat



'''
{
  "fixed_acidity": 7,
  "volatile_acidity": 0.7,
  "citric_acid": 0.06,
  "residual_sugar": 2.6,
  "chlorides": 0.096,
  "free_sulfur_dioxide": 11,
  "total_sulfur_dioxide": 25,
  "density": 0.9965,
  "pH": 3.2,
  "sulphates": 0.65,
  "alcohol": 9.8
}
'''