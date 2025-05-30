import tkinter as tk
from tkinter import messagebox
import numpy as np
import os
import joblib
import tensorflow as tf

# Ruta de los artefactos (ajusta si es necesario)
MODEL_DIR = os.path.join(os.path.dirname(__file__), 'models')

# Cargar artefactos para vino tinto
model_red = tf.keras.models.load_model(os.path.join(MODEL_DIR, 'red_wine_model.keras'))
imp_red = joblib.load(os.path.join(MODEL_DIR, 'red_imputer.pkl'))
scaler_red = joblib.load(os.path.join(MODEL_DIR, 'red_scaler.pkl'))

# Cargar artefactos para vino blanco
model_white = tf.keras.models.load_model(os.path.join(MODEL_DIR, 'white_wine_model.keras'))
imp_white = joblib.load(os.path.join(MODEL_DIR, 'white_imputer.pkl'))
scaler_white = joblib.load(os.path.join(MODEL_DIR, 'white_scaler.pkl'))

# Lista de características en orden
FEATURES = [
    'fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
    'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density',
    'pH', 'sulphates', 'alcohol'
]

# Función para convertir entrada a float o NaN
def float_or_nan(x):
    try:
        return float(x)
    except Exception:
        return np.nan

# Función de predicción
def predict_quality(values, wine_type):
    # Convertir y preparar array
    arr = np.array([float_or_nan(v) for v in values]).reshape(1, -1)
    if wine_type == 'red':
        arr_imp = imp_red.transform(arr)
        arr_sc = scaler_red.transform(arr_imp)
        pred = model_red.predict(arr_sc)[0][0]
    else:
        arr_imp = imp_white.transform(arr)
        arr_sc = scaler_white.transform(arr_imp)
        pred = model_white.predict(arr_sc)[0][0]
    # Categorizar
    if pred < 5:
        cat = 'Malo'
    elif pred < 7:
        cat = 'Regular'
    else:
        cat = 'Bueno'
    return pred, cat

# Crear GUI
root = tk.Tk()
root.title('Predicción de Calidad de Vino')

# Tipo de vino
wine_type = tk.StringVar(value='red')

tk.Label(root, text='Seleccione tipo de vino:').grid(row=0, column=0, columnspan=2, pady=(10,0))
tk.Radiobutton(root, text='Tinto', variable=wine_type, value='red').grid(row=1, column=0)
tk.Radiobutton(root, text='Blanco', variable=wine_type, value='white').grid(row=1, column=1)

# Entradas para características
entries = {}
for idx, feat in enumerate(FEATURES):
    tk.Label(root, text=feat).grid(row=idx+2, column=0, sticky='e', padx=5, pady=2)
    ent = tk.Entry(root)
    ent.grid(row=idx+2, column=1, padx=5, pady=2)
    entries[feat] = ent

# Resultado
resultado_var = tk.StringVar()
result_label = tk.Label(root, textvariable=resultado_var, fg='blue', font=('Arial', 12))
result_label.grid(row=len(FEATURES)+3, column=0, columnspan=2, pady=10)

# Botón de predicción
def on_predict():
    values = [entries[feat].get() for feat in FEATURES]
    pred, cat = predict_quality(values, wine_type.get())
    resultado_var.set(f'Puntaje: {pred:.2f}   Categoría: {cat}')

predict_btn = tk.Button(root, text='Predecir Calidad', command=on_predict)
predict_btn.grid(row=len(FEATURES)+2, column=0, columnspan=2, pady=5)

# Ejecución de la app
root.mainloop()