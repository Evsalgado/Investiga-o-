@echo off
chcp 65001 >nul
color 0A
title InvestigIA - Teste de Análise Avançada

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║              🔍 INVESTIGIA - ANÁLISE AVANÇADA 🔍              ║
echo ║                     Teste das Funcionalidades                  ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

echo 📋 INSTRUÇÕES PARA TESTE COMPLETO:
echo.
echo 1. ✅ Sistema será aberto automaticamente
echo 2. ✅ Carregue o arquivo: dados_investigacao_avancada.csv
echo 3. ✅ Clique em "Processar Arquivos"
echo 4. ✅ Vá para a aba "🔍 Análise Avançada"
echo 5. ✅ Teste todas as funcionalidades:
echo.
echo    💰 Analisar Fluxos         - Detecta maiores enviadores/recebedores
echo    🔍 Detectar Lavagem        - Identifica padrões de lavagem de dinheiro
echo    ⚠️ Identificar Riscos      - Classifica entidades de alto risco
echo    🎯 Centralidade           - Analisa influência na rede
echo    🚨 Detectar Padrões       - Encontra atividades suspeitas
echo    📊 Gerar Relatório        - Cria dashboard executivo
echo.
echo ════════════════════════════════════════════════════════════════
echo.

set "arquivo=investigia_final.html"

if exist "%arquivo%" (
    echo ✅ Abrindo sistema InvestigIA com análise avançada...
    echo.
    echo 🎯 RESULTADOS ESPERADOS:
    echo    • Roberto Alves: Score de risco 90+ (maior movimentador)
    echo    • FastCash Ltda: 12+ transações estruturadas (~R$ 9.900)
    echo    • MoneyFlow S.A.: Atividade circular detectada
    echo    • 8+ valores anômalos identificados
    echo    • Recomendação: INVESTIGAÇÃO URGENTE
    echo.
    echo 🚀 Sistema abrindo...
    start "" "%arquivo%"
    
    timeout /t 3 >nul
    echo.
    echo ✅ Sistema aberto! Siga as instruções acima para testar.
    echo.
    echo 📁 Arquivo de teste: dados_investigacao_avancada.csv
    echo 📋 Documentação: ANALISE_AVANCADA_README.md
    echo.
) else (
    echo ❌ ERRO: Arquivo %arquivo% não encontrado!
    echo.
    echo Certifique-se de estar na pasta correta do InvestigIA.
)

echo ════════════════════════════════════════════════════════════════
echo.
echo 💡 DICAS PARA DEMONSTRAÇÃO:
echo.
echo 1. 📊 Use dados_investigacao_avancada.csv para teste completo
echo 2. 🔍 Explore cada funcionalidade da aba "Análise Avançada"  
echo 3. 📈 Observe os scores de suspeição e classificações de risco
echo 4. 🚨 Verifique os alertas críticos no dashboard
echo 5. 💾 Exporte os resultados para análise posterior
echo.
echo Pressione qualquer tecla para fechar...
pause >nul 