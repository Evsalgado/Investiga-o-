@echo off
cls
color 0A
echo ========================================
echo    INVESTIG-IA - SISTEMA EXECUTAR
echo ========================================
echo.

REM Definir diretório do script
cd /d "%~dp0"

echo [INFO] Verificando sistema...
echo.

REM Verificar se o arquivo principal existe
if not exist "investigia_final.html" (
    echo [ERRO] Arquivo principal nao encontrado!
    echo Procurando arquivos alternativos...
    
    if exist "DIAGNOSTICO_SISTEMA.html" (
        echo [OK] Executando diagnostico do sistema...
        start "" "DIAGNOSTICO_SISTEMA.html"
        goto :end
    )
    
    if exist "TESTE_RAPIDO.html" (
        echo [OK] Executando teste rapido...
        start "" "TESTE_RAPIDO.html"
        goto :end
    )
    
    echo [ERRO] Nenhum arquivo do sistema encontrado!
    pause
    exit /b 1
)

echo [OK] Sistema encontrado!
echo.

REM Verificar se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [AVISO] Python nao encontrado. Executando apenas o arquivo HTML...
    start "" "investigia_final.html"
    goto :end
)

echo [OK] Python encontrado!
echo.

echo Escolha uma opcao:
echo.
echo 1. Executar sistema completo (HTML + Servidor)
echo 2. Executar apenas HTML (Mais simples)
echo 3. Executar diagnostico completo
echo 4. Teste rapido de funcionamento
echo 5. Sair
echo.

set /p opcao="Digite sua opcao (1-5): "

if "%opcao%"=="1" goto :servidor
if "%opcao%"=="2" goto :html
if "%opcao%"=="3" goto :diagnostico
if "%opcao%"=="4" goto :teste
if "%opcao%"=="5" goto :end

echo [ERRO] Opcao invalida!
pause
goto :end

:servidor
echo.
echo [INFO] Iniciando servidor HTTP...
echo [INFO] O sistema sera aberto automaticamente no navegador
echo [INFO] Para parar o servidor, pressione Ctrl+C
echo.
timeout /t 3 /nobreak >nul

REM Abrir o navegador após 2 segundos
start "" "http://localhost:8000/investigia_final.html"

REM Iniciar servidor
python -m http.server 8000
goto :end

:html
echo.
echo [INFO] Abrindo sistema no navegador...
start "" "investigia_final.html"
goto :end

:diagnostico
echo.
echo [INFO] Executando diagnostico completo...
start "" "DIAGNOSTICO_SISTEMA.html"
goto :end

:teste
echo.
echo [INFO] Executando teste rapido...
start "" "TESTE_RAPIDO.html"
goto :end

:end
echo.
echo [INFO] Operacao concluida.
pause 