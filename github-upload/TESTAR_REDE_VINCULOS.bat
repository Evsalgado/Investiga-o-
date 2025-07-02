@echo off
title InvestigIA - Teste da Rede de Vínculos Avançada
color 0A

echo ===============================================
echo    🕸️ INVESTIG-IA - REDE DE VÍNCULOS 🕸️
echo ===============================================
echo.
echo 🎯 Inspirado no Caseboard - Software Profissional
echo.
echo ✨ NOVAS FUNCIONALIDADES:
echo    🌐 Rede Completa de Vínculos
echo    🔗 Análise de Vínculos Detalhada  
echo    🎯 Detecção de Padrões
echo    🔍 Filtros Avançados
echo    📊 Estatísticas da Rede
echo    ⚠️ Sistema de Alertas
echo    📊 Matriz de Relacionamentos
echo.
echo 🚀 INICIANDO SISTEMA...
echo.

cd /d "%~dp0"

if exist "investigia_final.html" (
    echo ✅ Sistema encontrado: investigia_final.html
    echo.
    echo 📋 INSTRUÇÕES PARA TESTE:
    echo.
    echo 1. 📁 Carregue arquivos CSV/TXT/Excel
    echo 2. ⚙️ Clique em "Processar Arquivos"  
    echo 3. 🕸️ Vá para aba "Análise de Vínculos"
    echo 4. 🌐 Clique em "Rede Completa"
    echo 5. 🔗 Teste "Análise de Vínculos"
    echo 6. 🎯 Experimente "Detectar Padrões"
    echo 7. 🔍 Use os filtros avançados
    echo 8. 👆 Clique nos nós do grafo
    echo.
    echo 🎯 RECURSOS ESPECIAIS:
    echo    • Vínculos Financeiros (💰)
    echo    • Vínculos Corporativos (🏢)  
    echo    • Vínculos Pessoais (👥)
    echo    • Vínculos Temporais (📅)
    echo    • Alertas Automáticos (⚠️)
    echo    • Matriz de Adjacência (📊)
    echo.
    
    start "" "investigia_final.html"
    
    echo ✅ Sistema aberto no navegador!
    echo.
    echo 💡 DICAS:
    echo    • Use F12 para ver logs detalhados
    echo    • Teste com dados reais para melhores resultados
    echo    • Ajuste filtros para focar em tipos específicos
    echo    • Clique nos nós para ver detalhes das conexões
    echo.
    echo 📚 Documentação: REDE_VINCULOS_AVANCADA.md
    echo.
) else (
    echo ❌ Erro: investigia_final.html não encontrado!
    echo.
    echo 🔍 Verifique se você está na pasta correta.
    echo    Deveria conter: investigia_final.html
    echo.
)

echo 🎯 Pressione qualquer tecla para fechar...
pause > nul 