@echo off
title InvestigIA - Sistema de Inicializacao
color 0A

echo.
echo ==========================================
echo   🚀 InvestigIA - Sistema de Inicializacao
echo ==========================================
echo.

REM Verificar se estamos na pasta correta
if not exist "investigia_final.html" (
    echo ❌ ERRO: Arquivo investigia_final.html nao encontrado
    echo 📁 Tentando localizar arquivos...
    dir *.html
    echo.
    echo 💡 Execute este script dentro da pasta investig-ia
    pause
    exit /b 1
)

echo ✅ Arquivo principal encontrado: investigia_final.html
echo.

REM Verificar se Python está disponível
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ ERRO: Python nao encontrado
    echo 💡 Instale Python ou adicione ao PATH
    pause
    exit /b 1
)

echo ✅ Python disponível
echo.

REM Verificar arquivos de teste
if exist "dados_filtros_teste.csv" (
    echo ✅ Arquivo de teste encontrado: dados_filtros_teste.csv
) else (
    echo ⚠️  Arquivo de teste não encontrado, mas sistema pode funcionar
)

echo.
echo 🔄 INICIANDO SISTEMA...
echo.

REM Mostrar opções
echo Escolha uma opcao:
echo.
echo 1. Sistema Principal (investigia_final.html)
echo 2. Teste Rapido (TESTE_RAPIDO.html)
echo 3. Diagnostico do Sistema (DIAGNOSTICO_SISTEMA.html)
echo 4. Apenas iniciar servidor HTTP
echo.
set /p opcao="Digite sua escolha (1-4): "

if "%opcao%"=="1" goto sistema_principal
if "%opcao%"=="2" goto teste_rapido
if "%opcao%"=="3" goto diagnostico
if "%opcao%"=="4" goto apenas_servidor

:sistema_principal
echo.
echo 🌐 Iniciando sistema principal...
echo 📍 URL: http://localhost:8000/investigia_final.html
echo.
start http://localhost:8000/investigia_final.html
goto iniciar_servidor

:teste_rapido
echo.
echo 🧪 Iniciando teste rapido...
echo 📍 URL: http://localhost:8000/TESTE_RAPIDO.html
echo.
start http://localhost:8000/TESTE_RAPIDO.html
goto iniciar_servidor

:diagnostico
echo.
echo 🔧 Iniciando diagnostico do sistema...
echo 📍 URL: http://localhost:8000/DIAGNOSTICO_SISTEMA.html
echo.
start http://localhost:8000/DIAGNOSTICO_SISTEMA.html
goto iniciar_servidor

:apenas_servidor
echo.
echo 🌐 Iniciando apenas servidor HTTP...
echo 📍 Acesse: http://localhost:8000
echo.

:iniciar_servidor
echo ⚡ Servidor HTTP Python iniciado na porta 8000
echo.
echo 📋 INSTRUÇÕES:
echo • Acesse o sistema no navegador
echo • Para testar, use o arquivo: dados_filtros_teste.csv
echo • Pressione Ctrl+C para parar o servidor
echo • Feche esta janela para encerrar
echo.
echo 🔍 TROUBLESHOOTING:
echo • Se nao abrir automaticamente: http://localhost:8000
echo • Se der erro de porta: mude para 8001, 8002, etc.
echo • Se arquivos nao carregarem: verifique permissoes
echo.

python -m http.server 8000

pause 