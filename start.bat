@echo off
echo Iniciando Wine Classifier...

:: Iniciar el backend
start cmd /k "cd %~dp0 && venv\Scripts\activate && uvicorn controller:app --reload"

:: Esperar 2 segundos para que el backend inicie
timeout /t 2 /nobreak

:: Iniciar el frontend
start cmd /k "cd %~dp0\frontend && npm run dev"

echo Aplicacion iniciada!
echo Backend: http://localhost:8000
echo Frontend: http://localhost:3000 