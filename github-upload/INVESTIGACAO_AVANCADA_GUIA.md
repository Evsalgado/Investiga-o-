# 🔍 SISTEMA AVANÇADO DE INVESTIGAÇÃO DE FRAUDES

## Guia Completo de Uso e Interpretação

### 📋 VISÃO GERAL

O Sistema Avançado de Investigação de Fraudes é uma ferramenta profissional que utiliza algoritmos de análise de redes e detecção de padrões para identificar atividades suspeitas em dados financeiros. 

### 🎯 PRINCIPAIS FUNCIONALIDADES

#### 1. **Detecção de Estruturação (Fracionamento)**
- **O que é**: Identifica quando grandes transações são divididas em múltiplas pequenas transações para evitar detecção
- **Como funciona**: Analisa transações de uma mesma pessoa no mesmo dia, verificando se os valores são similares
- **Parâmetros configuráveis**: 
  - Limiar de estruturação (valor mínimo para alertar)
  - Tolerância de similaridade (quão similares devem ser os valores)

#### 2. **Análise de Transações Circulares**
- **O que é**: Detecta ciclos de transações que podem indicar lavagem de dinheiro
- **Como funciona**: Utiliza algoritmos de grafos para encontrar ciclos fechados na rede de transações
- **Indicadores de risco**: Tamanho do ciclo, valor total circulante, frequência

#### 3. **Identificação de Entidades Centrais (Hubs)**
- **O que é**: Encontra pessoas/empresas que são centrais na rede de transações
- **Métricas analisadas**:
  - Número total de conexões
  - Volume total de transações
  - Centralidade na rede
  - Fluxo de entrada vs saída

#### 4. **Detecção de Padrões Incomuns**
- **Outliers de valor**: Transações com valores muito acima da média
- **Alta frequência**: Pessoas com número anômalo de transações
- **Análise estatística**: Usa percentis e desvios padrão para identificar anomalias

#### 5. **Análise Temporal**
- **Atividades suspeitas**: Transações em horários incomuns (noites, fins de semana)
- **Padrões temporais**: Concentração de atividades em períodos específicos
- **Correlação temporal**: Relaciona timing com outros indicadores

### 🚀 COMO USAR

#### Passo 1: Iniciar o Sistema
```bash
python run_advanced_investigation.py
```

#### Passo 2: Preparar os Dados
Sua planilha deve conter pelo menos:
- **Nome/Pessoa**: Quem fez a transação
- **Empresa/Destino**: Para onde foi a transação
- **Valor**: Quantia da transação
- **Data**: Quando ocorreu (opcional)

#### Passo 3: Carregar Dados
1. Use o upload de arquivo no painel lateral
2. Selecione o arquivo CSV ou Excel
3. Configure o mapeamento das colunas
4. Ajuste os parâmetros de detecção

#### Passo 4: Executar Análise
1. Clique em "INICIAR INVESTIGAÇÃO"
2. Aguarde o processamento
3. Analise os resultados nas diferentes abas

### 📊 INTERPRETAÇÃO DOS RESULTADOS

#### Score de Risco Geral
- **0-19**: 🟢 Risco Baixo - Padrões normais
- **20-39**: 🟡 Risco Médio - Monitoramento recomendado
- **40-69**: 🟠 Risco Alto - Investigação recomendada
- **70-100**: 🔴 Risco Crítico - Ação imediata necessária

#### Indicadores de Estruturação
```
Pessoa: João Silva
Data: 15/01/2024
Transações: 5
Valores: [9.950, 9.800, 9.900, 9.850, 9.750]
Total: R$ 49.250
Coeficiente de Variação: 0.08 (muito baixo = suspeito)
```

#### Análise de Ciclos
```
Ciclo Detectado: João → Empresa A → Maria → Empresa B → João
Tamanho: 4 entidades
Valor Total: R$ 500.000
Risco: CRÍTICO
```

#### Entidades Centrais
```
Carlos Mendes:
- Conexões: 15
- Fluxo Total: R$ 2.500.000
- Entrada: R$ 1.200.000
- Saída: R$ 1.300.000
- Score de Centralidade: 85.6
- Risco: ALTO
```

### 🔍 DICAS DE INVESTIGAÇÃO

#### Sinais de Alerta Críticos
1. **Estruturação clara**: Múltiplas transações de valores similares
2. **Ciclos complexos**: Dinheiro voltando à origem após passar por várias entidades
3. **Hubs anômalos**: Pessoas físicas com volume empresarial
4. **Padrões temporais**: Atividades em horários incomuns

#### Combinações Suspeitas
- Pessoa com alta centralidade + transações estruturadas + ciclos
- Outliers de valor + atividade noturna + múltiplas empresas
- Ciclos curtos + valores similares + mesma data

#### Técnicas de Análise
1. **Análise Top-Down**: Comece pelos maiores scores de risco
2. **Análise Bottom-Up**: Investigue padrões específicos
3. **Análise Temporal**: Correlacione com eventos externos
4. **Análise de Rede**: Mapeie conexões entre entidades suspeitas

### 📈 VISUALIZAÇÃO DA REDE

#### Interpretação do Grafo
- **Tamanho dos nós**: Proporcional ao volume de transações
- **Cor dos nós**: 
  - Azul: Mais recebem que enviam
  - Vermelho: Mais enviam que recebem
  - Cinza: Fluxo equilibrado
- **Espessura das arestas**: Volume da relação financeira
- **Proximidade**: Entidades próximas têm relações mais fortes

#### Padrões Visuais Suspeitos
- **Estrelas**: Um nó central conectado a muitos outros
- **Clusters isolados**: Grupos que transacionam apenas entre si
- **Pontes**: Nós que conectam diferentes grupos
- **Nós periféricos**: Entidades com poucas conexões mas alto volume

### 📄 RELATÓRIOS DE EXPORTAÇÃO

#### Conteúdo dos Relatórios
1. **Resumo Executivo**: Métricas gerais e score de risco
2. **Estruturação**: Lista detalhada de padrões detectados
3. **Entidades Centrais**: Ranking por importância na rede
4. **Padrões Incomuns**: Outliers e anomalias detectadas
5. **Análise Temporal**: Atividades suspeitas por período

#### Formatos Disponíveis
- **Excel**: Planilhas separadas por categoria
- **CSV**: Dados estruturados para análise adicional
- **JSON**: Dados para integração com outros sistemas

### ⚖️ CONSIDERAÇÕES LEGAIS

#### Uso Responsável
- Esta ferramenta é para análise preliminar e identificação de padrões
- Não substitui investigação formal ou perícia judicial
- Resultados devem ser validados por especialistas
- Respeite a privacidade e legislação vigente

#### Documentação
- Mantenha registros de todos os parâmetros utilizados
- Documente as fontes dos dados analisados
- Registre as interpretações e conclusões
- Preserve evidências digitais adequadamente

### 🛠️ PARÂMETROS AVANÇADOS

#### Configurações de Estruturação
```python
# Valores recomendados para diferentes cenários
limiar_estruturacao = 10000    # R$ 10.000 (padrão brasileiro)
tolerancia_similaridade = 0.1  # 10% de variação (rígido)
min_transacoes_dia = 3         # Mínimo 3 transações por dia
```

#### Configurações de Ciclos
```python
tamanho_minimo_ciclo = 3       # Mínimo 3 entidades no ciclo
valor_minimo_ciclo = 50000     # R$ 50.000 valor mínimo
max_ciclos_analisar = 50       # Analisar até 50 ciclos
```

#### Configurações de Centralidade
```python
peso_conexoes = 0.3           # 30% do score para número de conexões
peso_volume = 0.4             # 40% do score para volume financeiro
peso_transacoes = 0.3         # 30% do score para número de transações
```

### 🎯 CASOS DE USO TÍPICOS

#### 1. Investigação de Lavagem de Dinheiro
- Foco em ciclos e estruturação
- Análise de grandes volumes
- Identificação de intermediários

#### 2. Detecção de Fraude Corporativa
- Análise de fornecedores suspeitos
- Identificação de beneficiários ocultos
- Padrões de superfaturamento

#### 3. Compliance e Auditoria
- Monitoramento contínuo
- Identificação de riscos
- Validação de políticas

#### 4. Investigação Jornalística
- Mapeamento de conexões
- Identificação de padrões
- Visualização de redes

### 💡 DICAS DE OTIMIZAÇÃO

#### Performance
- Limite datasets a 50.000 transações para melhor performance
- Use filtros temporais para análises focadas
- Execute análises incrementais para grandes volumes

#### Qualidade dos Dados
- Padronize nomes de pessoas e empresas
- Verifique consistência de valores
- Valide formatos de data
- Remova duplicatas

#### Interpretação
- Combine múltiplos indicadores
- Considere contexto temporal
- Valide padrões manualmente
- Use conhecimento do domínio

### 🆘 SOLUÇÃO DE PROBLEMAS

#### Problemas Comuns
1. **Erro de dependências**: Execute `pip install -r requirements.txt`
2. **Dados não carregam**: Verifique formato e codificação do arquivo
3. **Análise muito lenta**: Reduza o tamanho do dataset
4. **Resultados inconsistentes**: Verifique qualidade dos dados

#### Suporte Técnico
- Verifique logs de erro no terminal
- Teste com dados de exemplo fornecidos
- Documente problemas com capturas de tela
- Mantenha backups dos dados originais

---

## 🎯 CONCLUSÃO

O Sistema Avançado de Investigação de Fraudes é uma ferramenta poderosa para análise de padrões suspeitos em dados financeiros. Use-o com responsabilidade, sempre validando resultados e respeitando aspectos legais e éticos.

Para suporte adicional ou dúvidas técnicas, consulte a documentação completa ou entre em contato com a equipe de desenvolvimento.

**Versão**: 2.0
**Última Atualização**: 2024