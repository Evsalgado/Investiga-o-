@echo off
echo.
echo ========================================
echo     DIAGNOSTICO SISTEMA INVESTIGIA
echo ========================================
echo.
echo 1. Verificando arquivos principais...
echo.

if exist "investigia_final.html" (
    echo ✅ investigia_final.html - ENCONTRADO
) else (
    echo ❌ investigia_final.html - NAO ENCONTRADO
)

if exist "teste_real.csv" (
    echo ✅ teste_real.csv - ENCONTRADO
) else (
    echo ❌ teste_real.csv - NAO ENCONTRADO
)

if exist "TESTE_SISTEMA.html" (
    echo ✅ TESTE_SISTEMA.html - ENCONTRADO
) else (
    echo ❌ TESTE_SISTEMA.html - NAO ENCONTRADO
)

echo.
echo 2. Testando abertura do sistema...
echo.

echo Abrindo sistema de teste...
start "" "TESTE_SISTEMA.html"

timeout /t 3 /nobreak >nul

echo.
echo 3. Instrucoes de uso:
echo.
echo ✅ Use TESTE_SISTEMA.html para testar o upload
echo ✅ Use teste_real.csv como arquivo de exemplo
echo ✅ Abra investigia_final.html para o sistema completo
echo ✅ Verifique o console do navegador (F12) para logs
echo.
echo 4. Solucao de problemas:
echo.
echo Se nao funcionar:
echo - Verifique se tem conexao com internet (para biblioteca XLSX)
echo - Abra o console do navegador (F12) para ver erros
echo - Teste primeiro com o arquivo teste_real.csv
echo.
pause 