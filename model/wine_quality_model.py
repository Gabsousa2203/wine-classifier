from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd
from sklearn.model_selection import train_test_split
import pandas as pd
from tensorflow.keras import models, layers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, InputLayer
from keras_tuner.tuners import RandomSearch
import joblib
import os

def model_prepare(path_csv):
    #* Se carga el CVS y se dividen en X e y
    df = pd.read_csv(path_csv, sep=';')
    X = df.drop('quality', axis=1)
    y = df['quality']  # Aseguramos que y sea un array 2D
    
    #* Dividimos en train y test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    #* Imputamos para que cuando falte un valor el modelo pueda sustituirlo por la media y escalamos los datos
    imp = SimpleImputer(strategy='mean')
    scl = StandardScaler()
    X_train = scl.fit_transform(imp.fit_transform(X_train))
    X_test   = scl.transform(imp.transform(X_test))

    def build_model(hp):
        model = Sequential()
    
        #* Se define la capa de entrada
        model.add(InputLayer(input_shape=(X_train.shape[1],)))
    
        #* Se añade las capas ocultas y dropout según el hiperparámetro
        for i in range(hp.Int('num_dense_layers', 1, 3, step=1)):
            units = hp.Int(f'units_{i}', 32, 256, step=32)
            drop  = hp.Float(f'dropout_{i}', 0.0, 0.5, step=0.1)

            model.add(Dense(units, activation='relu'))
            model.add(Dropout(drop))
    
        #* Capa de salida
        model.add(Dense(1, activation='linear'))

        model.compile(
            optimizer=hp.Choice('optimizer', ['adam','rmsprop']),
            loss='mse',
            metrics=['mae']
        )

        return model

    
    #* Entrenar modelo Keras
    tuner = RandomSearch(
    build_model,
    objective='val_mae',
    max_trials=10,
    executions_per_trial=3,
    directory='my_dir',
    project_name='wine_quality_tuning')

    tuner.search(X_train, y_train, epochs=50, validation_split=0.2)

    best_hps = tuner.get_best_hyperparameters(num_trials=1)[0]
    print(f"Best hyperparameters: {best_hps.values}")

    best_model = tuner.hypermodel.build(best_hps)
    best_model.fit(X_train, y_train, epochs=10, validation_split=0.2)

    loss, mae = best_model.evaluate(X_test, y_test)
    print(f"Mean Absolute Error on test set: {mae}")
    
    return best_model, imp, scl


def train_models():
    try:
    
        #* Entrena cada uno:
        model_red, imp_red, scl_red     = model_prepare("data\winequality-red.csv")
        model_white, imp_white, scl_white = model_prepare("data\winequality-white.csv")


        #* Guardamos los modelos y los objetos de imputación y escalado
        model_red.save("models_imputers_scalers/red_wine_model.keras")       
        model_white.save("models_imputers_scalers/white_wine_model.keras")

        joblib.dump(imp_red,   "models_imputers_scalers/red_imputer.pkl")
        joblib.dump(scl_red,   "models_imputers_scalers/red_scaler.pkl")
        joblib.dump(imp_white, "models_imputers_scalers/white_imputer.pkl")
        joblib.dump(scl_white, "models_imputers_scalers/white_scaler.pkl")

        return {
            "status": "success",
            "message": "Modelos entrenados y guardados correctamente."
        }
    
    except Exception as e:
        print(f"Error al entrenar los modelos: {e}")
        return {"status": "Error al entrenar los modelos", "error": str(e)}