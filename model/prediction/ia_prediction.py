from models_imputers_scalers import load_models
from dto import wine_features_dto as dto
import numpy as np


def predict(values: list, wine_type: str):

    #* Se cargan los 2 modelos y se decide cual usar
    MODELS = load_models.load_all_models()
    model, imp, scaler = MODELS[wine_type]

    arr = np.array(values).reshape(1, -1)

    #* ISe imputan los datos faltantes, colocandoles la mediana
    arr_imp = imp.transform(arr)
    
    #* Se escalan los valores
    arr_sc = scaler.transform(arr_imp)

    #* Se hace la prediccion
    pred = model.predict(arr_sc)[0][0]

    #* Clasificación de la calidad del vino
    if pred < 5:
        cat = "Malo"
    elif pred < 7:
        cat = "Regular"
    else:
        cat = "Bueno"

    return pred, cat
