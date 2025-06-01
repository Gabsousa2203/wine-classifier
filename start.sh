#!/bin/bash

# Colores para los mensajes
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${GREEN}Iniciando Wine Classifier...${NC}"

# Función para limpiar procesos al salir
cleanup() {
    echo -e "\n${YELLOW}Deteniendo servicios...${NC}"
    kill $BACKEND_PID $FRONTEND_PID 2>/dev/null
    exit 0
}

# Configurar trap para SIGINT (Ctrl+C)
trap cleanup SIGINT

# Iniciar el backend
source ./venv/Scripts/activate
uvicorn controller:app --reload &
BACKEND_PID=$!

# Esperar 2 segundos para que el backend inicie
sleep 2

# Verificar si los modelos ya existen
if [ ! -f "models_imputers_scalers/red_wine_model.keras" ] || [ ! -f "models_imputers_scalers/white_wine_model.keras" ]; then
    echo -e "\n${YELLOW}Modelos no encontrados. Iniciando entrenamiento...${NC}"
    curl -X POST http://localhost:8000/train_models
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}Modelos entrenados correctamente${NC}"
    else
        echo -e "${RED}Error al entrenar los modelos${NC}"
        cleanup
    fi
else
    echo -e "\n${GREEN}Modelos encontrados. Continuando con el inicio...${NC}"
fi

# Iniciar el frontend
cd frontend
npm run dev &
FRONTEND_PID=$!
cd ..

echo -e "\n${GREEN}¡Aplicación iniciada!${NC}"
echo -e "${CYAN}Backend: http://localhost:8000${NC}"
echo -e "${CYAN}Frontend: http://localhost:3000${NC}"
echo -e "\n${YELLOW}Presiona Ctrl+C para detener todos los servicios${NC}"

# Esperar a que alguno de los procesos termine
wait 