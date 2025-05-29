from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.model_selection import train_test_split
import pandas as pd
from tensorflow.keras import models, layers

def prepara_modelo(path_csv):
    # 1) Cargar
    df = pd.read_csv(path_csv, sep=';')
    X = df.drop('quality', axis=1)
    y = df['quality']
    
    # 2) Split
    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # 3) Imputar + escalar
    imp = SimpleImputer(strategy='mean')
    scl = StandardScaler()
    X_train = scl.fit_transform(imp.fit_transform(X_train))
    X_val   = scl.transform(imp.transform(X_val))
    
    # 4) Definir y entrenar modelo Keras
    model = models.Sequential([
        layers.Input(shape=(X_train.shape[1],)),
        layers.Dense(64, activation='relu'),
        layers.Dense(32, activation='relu'),
        layers.Dense(1, activation='linear'),
    ])
    model.compile('adam', 'mse', metrics=['mae'])
    model.fit(X_train, y_train, epochs=50, validation_data=(X_val, y_val),
            )
    
    print(f"Modelo entrenado para {path_csv} con {X_train.shape[0]} muestras de entrenamiento y {X_val.shape[0]} de validación.")
    # 5) Devolver modelo, imputador y escalador
    
    return model, imp, scl

# Entrenas cada uno:
model_red, imp_red, scl_red     = prepara_modelo("data\winequality-red.csv")
model_white, imp_white, scl_white = prepara_modelo("data\winequality-white.csv")

