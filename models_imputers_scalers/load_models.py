import joblib
from tensorflow.keras.models import load_model

MODELS = {}

def load_all_models():
    # Carga vino rojo
    model_red = load_model("models_imputers_scalers/red_wine_model.keras")
    imp_red = joblib.load("models_imputers_scalers/red_imputer.pkl")
    scl_red = joblib.load("models_imputers_scalers/red_scaler.pkl")
    
    # Carga vino blanco
    model_white = load_model("models_imputers_scalers/white_wine_model.keras")
    imp_white = joblib.load("models_imputers_scalers/white_imputer.pkl")
    scl_white = joblib.load("models_imputers_scalers/white_scaler.pkl")
    
    MODELS['red'] = (model_red, imp_red, scl_red)
    MODELS['white'] = (model_white, imp_white, scl_white)
    return MODELS

