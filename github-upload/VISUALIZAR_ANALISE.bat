@echo off
echo ========================================
echo   🛠️  InvestigIA - Análise Financeira
echo ========================================
echo.
echo Abrindo relatórios da análise...
echo.

start "" "relatorio_visual.html"
timeout /t 2 /nobreak >nul

start "" "rede_entidades.html"

echo ✅ Relatórios abertos no navegador!
echo.
echo Arquivos disponíveis:
echo - relatorio_visual.html (Relatório detalhado)
echo - rede_entidades.html (Visualização da rede)
echo - relatorio_investig_ia.json (Dados em JSON)
echo.
pause 