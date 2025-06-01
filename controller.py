from fastapi import FastAPI, HTTPException, Body, Query
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
from model import wine_quality_model as wqm
from dto import wine_features_dto as dto
from model.prediction import ia_prediction as ia_pred

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Permitir peticiones desde el frontend
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todas las cabeceras
)

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
            "alcohol": 9.4,
            "wine_type": "red"
        }
    )):

    try:
        FEATURES = [
        "fixed_acidity", "volatile_acidity", "citric_acid", "residual_sugar",
        "chlorides", "free_sulfur_dioxide", "total_sulfur_dioxide",
        "density", "pH", "sulphates", "alcohol"]

        if data.wine_type not in ['red', 'white']:
            raise HTTPException(status_code=400, detail="Tipo de vino no válido. Debe ser 'red' o 'white'.")
    
        values = []
        for feat in FEATURES:
            val = getattr(data, feat)
            if val is None:
                values.append(np.nan)
            else:
                values.append(val)

        pred, cat = ia_pred.predict(values, data.wine_type)
    
    except Exception as e:
        raise HTTPException(
            status_code=400, 
            detail=f"{str(e)}")

    return {
        "message": f"La predicción es {pred:.2f} y la categoría es '{cat}'.",
        "prediction": float(pred),
        "category": cat
        }