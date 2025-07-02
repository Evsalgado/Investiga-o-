@echo off
title InvestigIA - Sistema Completo com Rede Automática
color 0A

echo ===============================================
echo    🔍 INVESTIG-IA - SISTEMA COMPLETO 🔍
echo ===============================================
echo.
echo 🎨 IDENTIDADE VISUAL: Mercado Livre/Mercado Pago
echo 🕸️ REDE AUTOMÁTICA: Carregamento após processamento
echo 🔍 FILTROS AVANÇADOS: Estilo i2 Analyst Notebook
echo.
echo ✨ NOVAS FUNCIONALIDADES:
echo    🌐 Carregamento automático da rede
echo    🔍 Filtros por entidade, conexão, valor, data
echo    👁️ 4 modos de visualização diferentes
echo    ⭐ Detecção de caminhos críticos
echo    📊 Exportação de dados
echo    🎨 Interface moderna ML/MP
echo.
echo 🚀 INICIANDO SISTEMA...
echo.

cd /d "%~dp0"

if exist "investigia_final.html" (
    echo ✅ Sistema encontrado: investigia_final.html
    echo.
    echo 📋 FLUXO DE TESTE RECOMENDADO:
    echo.
    echo 1. 📁 Carregue o arquivo: dados_rede_teste.csv
    echo 2. ⚙️ Clique em "Processar Arquivos"
    echo 3. ⏱️ Aguarde 3 segundos - a rede carregará automaticamente
    echo 4. 🕸️ Sistema mudará para aba "Rede de Vínculos"
    echo 5. 🔍 Teste os filtros avançados:
    echo    • Tipo de Entidade (pessoas/empresas)
    echo    • Tipo de Conexão (financeiro/corporativo)
    echo    • Intensidade (slider 1-10)
    echo    • Valor Mínimo (R$)
    echo    • Período (datas)
    echo 6. 👁️ Experimente os modos de visualização:
    echo    • Circular (padrão)
    echo    • Hierárquico (por importância)
    echo    • Por Força (tamanho = conexões)
    echo    • Timeline (cronológico)
    echo 7. ⭐ Clique em "Caminhos Críticos"
    echo 8. 📊 Teste "Exportar Dados"
    echo.
    echo 🎯 RECURSOS ESPECIAIS:
    echo    • Interface azul/amarelo (ML/MP)
    echo    • Nós clicáveis com detalhes
    echo    • Estatísticas em tempo real
    echo    • Alertas automáticos
    echo    • Matriz de adjacência
    echo    • Reset de filtros
    echo.
    
    start "" "investigia_final.html"
    
    echo ✅ Sistema aberto no navegador!
    echo.
    echo 💡 DICAS IMPORTANTES:
    echo    • Use F12 para ver logs detalhados
    echo    • A rede carrega AUTOMATICAMENTE após processar
    echo    • Teste todos os filtros para ver o poder do sistema
    echo    • Clique nos nós coloridos para ver detalhes
    echo    • Use "Caminhos Críticos" para análise avançada
    echo.
    echo 📚 Documentação:
    echo    • REDE_VINCULOS_AVANCADA.md
    echo    • RESUMO_MELHORIAS_REDE.md
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