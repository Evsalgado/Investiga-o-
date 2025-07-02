@echo off
title Sistema Avançado de Investigacao de Fraudes
color 0A
cls

echo ===============================================================================
echo                 SISTEMA AVANCADO DE INVESTIGACAO DE FRAUDES
echo ===============================================================================
echo.
echo 🔍 Detecta padroes suspeitos, lavagem de dinheiro e redes criminosas
echo 📊 Analise robusta com algoritmos investigativos avancados  
echo 🚨 Interface moderna com visualizacoes interativas
echo.
echo ===============================================================================
echo.

echo ⏳ Verificando ambiente Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python nao encontrado!
    echo 💡 Instale Python 3.8+ antes de continuar
    echo    Download: https://python.org/downloads
    pause
    exit /b 1
)

echo ✅ Python encontrado!
echo.

echo 🔍 Verificando arquivos necessarios...
if not exist "advanced_fraud_analyzer.py" (
    echo ❌ Arquivo advanced_fraud_analyzer.py nao encontrado!
    pause
    exit /b 1
)

if not exist "advanced_investigation_app.py" (
    echo ❌ Arquivo advanced_investigation_app.py nao encontrado!
    pause
    exit /b 1
)

if not exist "run_advanced_investigation.py" (
    echo ❌ Arquivo run_advanced_investigation.py nao encontrado!
    pause
    exit /b 1
)

echo ✅ Todos os arquivos encontrados!
echo.

echo 🚀 Iniciando Sistema de Investigacao Avancada...
echo.
echo 📝 INSTRUÇÕES:
echo    1. A aplicacao abrira no navegador automaticamente
echo    2. Use o painel lateral para carregar seus dados
echo    3. Configure os parametros de deteccao conforme necessario
echo    4. Clique em 'INICIAR INVESTIGACAO' para analise completa
echo.
echo 🌐 URL de acesso: http://localhost:8501
echo ⏹️  Para parar o sistema: Pressione Ctrl+C
echo.

echo ===============================================================================
echo.

REM Executar o sistema
python run_advanced_investigation.py

echo.
echo ===============================================================================
echo ✅ SISTEMA ENCERRADO
echo 📊 Obrigado por usar o Sistema de Investigacao Avancada!
echo ===============================================================================
echo.
pause 