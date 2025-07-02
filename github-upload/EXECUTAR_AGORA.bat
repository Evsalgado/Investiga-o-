@echo off
title InvestigIA - Sistema Funcional
color 0A

echo.
echo ========================================
echo    🛠️  INVESTIGIA - SISTEMA FUNCIONAL
echo ========================================
echo.

echo 🔍 Verificando dependencias...
python -c "import fastapi, uvicorn, spacy, easyocr" 2>nul
if errorlevel 1 (
    echo ❌ Instalando dependencias...
    pip install -r backend\requirements.txt
    python -m spacy download pt_core_news_sm
)

echo ✅ Dependencias OK!
echo.

echo 🚀 Iniciando Backend (API com IA)...
start "InvestigIA Backend" /min python -m uvicorn backend.main:app --host 0.0.0.0 --port 8000

echo ⏳ Aguardando backend iniciar...
timeout /t 5 /nobreak >nul

echo 🌐 Iniciando Frontend...
start "InvestigIA Frontend" /min python -m http.server 3000 -d frontend

echo ⏳ Aguardando frontend iniciar...
timeout /t 3 /nobreak >nul

echo.
echo 🎉 INVESTIGIA FUNCIONAL PRONTO!
echo ========================================
echo 🌐 Acesse: http://localhost:3000
echo 🔧 API: http://localhost:8000
echo 📚 Docs: http://localhost:8000/docs
echo ========================================
echo.

echo 🚀 Abrindo navegador...
start http://localhost:3000

echo.
echo ✨ Sistema rodando em segundo plano!
echo 💡 Feche esta janela para parar o sistema
echo.
pause 