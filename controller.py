from fastapi import FastAPI, HTTPException, Body, Query
import numpy as np
from model import wine_quality_model as wqm
from dto import wine_features_dto as dto
from model.prediction import ia_prediction as ia_pred

app = FastAPI()

MODELS = {}


@app.post("/train_models")
def train():
    result = wqm.train_models()
    if result["status"] == "success":
        return {"detail": result["message"]}
    else:
        # Aquí puedes lanzar un HTTPException con código 500 o similar
        from fastapi import HTTPException
        raise HTTPException(status_code=500, detail=result["message"])

@app.post("/predict")
def predict(data: dto.WineFeaturesDict = Body(
        ...,
        example={
            "fixed_acidity": 7.4,
            "volatile_acidity": 0.7,
            "citric_acid": 0.0,
            "residual_sugar": 1.9,
            "chlorides": 0.076,
            "free_sulfur_dioxide": 11,
            "total_sulfur_dioxide": 34,
            "density": 0.9978,
            "pH": 3.51,
            "sulphates": 0.56,
            "alcohol": 9.4
        }
    ),
    wine_type: str = Query(..., description="Tipo de vino: 'red' o 'white'")):

    try:
        FEATURES = [
        "fixed_acidity", "volatile_acidity", "citric_acid", "residual_sugar",
        "chlorides", "free_sulfur_dioxide", "total_sulfur_dioxide",
        "density", "pH", "sulphates", "alcohol"]

        #* Se convierten los datos que llegan en el DTO a una lista de valores
        if wine_type not in ['red', 'white']:
            raise HTTPException(status_code=400, detail="Tipo de vino no válido. Debe ser 'red' o 'white'.")
    
        values = []
        for feat in FEATURES:
            val = getattr(data, feat)
            if val is None:
                values.append(np.nan)
            else:
                values.append(val)

        pred, cat = ia_pred.predict(values, wine_type)
    
    except Exception as e:
        raise HTTPException(
            status_code=400, 
            detail=f"{str(e)}")

    return {
        "message": f"La predicción es {pred:.2f} y la categoría es '{cat}'.",
        "prediction": float(pred),
        "category": cat
        }