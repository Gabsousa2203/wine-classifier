Write-Host "Iniciando Wine Classifier..." -ForegroundColor Green

# Iniciar el backend
$backendJob = Start-Process powershell -ArgumentList "-NoExit", "-Command", "Set-Location '$PSScriptRoot'; .\venv\Scripts\Activate.ps1; uvicorn controller:app --reload" -PassThru

# Esperar 2 segundos para que el backend inicie
Start-Sleep -Seconds 2

# Iniciar el frontend
$frontendJob = Start-Process powershell -ArgumentList "-NoExit", "-Command", "Set-Location '$PSScriptRoot\frontend'; npm run dev" -PassThru

Write-Host "`nAplicación iniciada!" -ForegroundColor Green
Write-Host "Backend: http://localhost:8000" -ForegroundColor Cyan
Write-Host "Frontend: http://localhost:3000" -ForegroundColor Cyan

# Esperar a que el usuario presione una tecla para cerrar todo
Write-Host "`nPresiona cualquier tecla para detener la aplicación..." -ForegroundColor Yellow
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")

# Detener los procesos
Stop-Process -Id $backendJob.Id -Force
Stop-Process -Id $frontendJob.Id -Force 