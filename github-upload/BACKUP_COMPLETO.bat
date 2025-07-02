@echo off
echo.
echo ========================================
echo    📂 BACKUP COMPLETO - INVESTIGIA 
echo ========================================
echo.

set data=%date:~0,2%-%date:~3,2%-%date:~6,4%
set pasta=INVESTIGIA_BACKUP_%data%

echo 🔄 Criando backup do projeto...
echo.

:: Criar pasta de backup
if not exist %pasta% mkdir %pasta%

:: Copiar arquivos principais
echo ✅ Copiando sistema principal...
copy investigia_final.html %pasta%\ >nul 2>&1
copy analise_avancada.js %pasta%\ >nul 2>&1
copy app.html %pasta%\ >nul 2>&1

echo ✅ Copiando dados e documentação...
copy *.csv %pasta%\ >nul 2>&1
copy *.md %pasta%\ >nul 2>&1
copy *.txt %pasta%\ >nul 2>&1

echo ✅ Copiando scripts e utilitários...
copy *.bat %pasta%\ >nul 2>&1
copy *.html %pasta%\ >nul 2>&1

echo.
echo 🎯 BACKUP CONCLUÍDO!
echo 📁 Pasta: %pasta%
echo.
echo ========================================
echo   ✅ PROJETO INVESTIGIA SALVO! 
echo ========================================
echo.
echo Pressione qualquer tecla para continuar...
pause >nul 