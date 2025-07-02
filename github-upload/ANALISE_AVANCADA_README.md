# 🔍 InvestigIA - Análise Avançada e Investigativa

## 🚀 Novas Funcionalidades Implementadas

O sistema InvestigIA foi **significativamente melhorado** com algoritmos avançados de análise investigativa para detecção de fraudes e padrões suspeitos.

---

## 📊 Funcionalidades de Análise Avançada

### 💰 **Análise de Fluxo Financeiro**
- **Maiores Enviadores**: Identifica pessoas que mais enviam dinheiro
- **Maiores Recebedores**: Identifica pessoas que mais recebem dinheiro  
- **Fluxos Bidirecionais**: Detecta transações suspeitas entre as mesmas pessoas
- **Valores Anômalos**: Identifica transações fora do padrão estatístico
- **Score de Suspeição**: Sistema de pontuação baseado em múltiplos fatores

### 🕸️ **Análise de Centralidade de Rede**
- **Betweenness Centrality**: Pessoas que servem como "pontes" na rede
- **Closeness Centrality**: Pessoas com menor distância para outras
- **Degree Centrality**: Pessoas com mais conexões diretas
- **Detecção de Clusters**: Grupos de pessoas altamente conectadas
- **Pontes Estratégicas**: Conexões críticas que mantêm a rede unida

### 🚨 **Detecção de Padrões Suspeitos**
- **Lavagem de Dinheiro**: Valores redondos e múltiplas transações pequenas
- **Estruturação**: Transações próximas aos limites de declaração (ex: R$ 9.900)
- **Atividade Circular**: Esquemas A→B→C→A para mascarar origem dos recursos
- **Valores Anômalos**: Transações que fogem ao padrão estatístico

### 🎯 **Identificação de Entidades de Alto Risco**
- **Pessoas de Alto Risco**: Score baseado em frequência e conexões
- **Empresas Suspeitas**: Análise de padrões corporativos
- **Fatores de Risco**: Lista detalhada dos motivos da classificação
- **Recomendações**: Ações sugeridas baseadas no nível de risco

---

## 🧮 Algoritmos Implementados

### **Sistema de Scoring Inteligente**
```javascript
// Exemplo de cálculo para enviadores
score += Math.min(dados.enviado / 100000, 50);     // Valor enviado
score += Math.min(dados.conexoes.size * 2, 30);    // Número de conexões
score += Math.min(dados.transacoes, 20);           // Número de transações
```

### **Detecção de Anomalias Estatísticas**
- Usa **desvio padrão** para identificar valores fora do padrão
- Considera transações **3σ** acima ou abaixo da média como anômalas
- Calcula **score de suspeição** baseado na distância da média

### **Análise de Rede Social Avançada**
- **Algoritmo de Dijkstra** para calcular distâncias mínimas
- **Detecção de componentes conectados** para encontrar clusters
- **Análise de pontes** para identificar nós críticos na rede

---

## 📋 Como Usar as Novas Funcionalidades

### 1. **Processamento de Dados**
```
1. Carregue seus documentos (CSV, XLSX, TXT, PDF)
2. Clique em "Processar Arquivos"
3. O sistema irá automaticamente para a aba "Rede de Conexões"
```

### 2. **Análise Avançada**
```
1. Vá para a aba "🔍 Análise Avançada"
2. Execute as análises específicas:
   - "💰 Analisar Fluxos" - Análise financeira
   - "⚠️ Identificar Riscos" - Entidades de alto risco
   - "🎯 Centralidade" - Análise de rede
   - "🚨 Detectar Padrões" - Padrões suspeitos
```

### 3. **Relatório Executivo**
```
1. Clique em "📊 Gerar Relatório"
2. Visualize o dashboard com:
   - Alertas críticos
   - Pessoas de alto risco
   - Densidade da rede
   - Recomendação geral
```

---

## 🎯 Exemplo de Uso Prático

### **Cenário: Investigação de Lavagem de Dinheiro**

1. **Carregue dados**: `dados_investigacao_avancada.csv`
2. **Execute análise**: O sistema detectará automaticamente:
   - ⚠️ **Roberto Alves**: Maior movimentador (R$ 3.4M+)
   - 🔴 **FastCash Ltda**: Múltiplas transações ~R$ 9.900 (estruturação)
   - 🔄 **MoneyFlow S.A.**: Atividade circular suspeita
   - 📊 **8+ valores anômalos** detectados

3. **Resultados típicos**:
   ```
   🚨 PADRÕES SUSPEITOS DETECTADOS:
   • 12 transações próximas ao limite de declaração (ALTA)
   • 3 possíveis esquemas circulares detectados (MEDIA)
   • 8 valores anômalos identificados
   
   ⚠️ RECOMENDAÇÃO: INVESTIGAÇÃO URGENTE
   ```

---

## 📈 Métricas e Indicadores

### **Scores de Suspeição**
- **0-30**: Baixo risco (verde)
- **31-70**: Médio risco (laranja)  
- **71-100**: Alto risco (vermelho)

### **Tipos de Alerta**
- 🔴 **CRÍTICO**: Investigação urgente necessária
- 🟡 **MÉDIO**: Monitoramento intensivo
- 🟢 **BAIXO**: Revisão periódica

### **Padrões Detectados**
- **Estruturação**: Transações entre R$ 9.000-9.999
- **Lavagem**: Valores redondos (múltiplos de R$ 1.000)
- **Circular**: Ciclos A→B→C→A
- **Anômalos**: Desvio > 3σ da média

---

## 🔧 Arquivos Modificados

1. **`investigia_final.html`**: Sistema principal com nova aba
2. **`analise_avancada.js`**: Algoritmos de análise avançada
3. **`dados_investigacao_avancada.csv`**: Dados de teste robustos

---

## 🎓 Baseado em Técnicas Profissionais

### **Inspirações Acadêmicas e Profissionais**
- **IBM i2 Analyst Notebook**: Análise de redes complexas
- **Palantir Gotham**: Detecção de padrões em big data
- **COAF/BACEN**: Metodologias de detecção de lavagem de dinheiro
- **Network Analysis Theory**: Algoritmos de centralidade e clustering

### **Algoritmos Utilizados**
- **Betweenness Centrality**: Identificar intermediários críticos
- **Clustering Coefficient**: Medir densidade local da rede
- **Statistical Outlier Detection**: Identificar valores anômalos
- **Graph Traversal (BFS/DFS)**: Detectar componentes conectados

---

## 🚀 Próximas Melhorias Planejadas

- [ ] **Machine Learning**: Modelos preditivos para classificação de risco
- [ ] **Visualização 3D**: Grafos interativos com D3.js ou Three.js
- [ ] **API Integration**: Conectar com bases de dados externas
- [ ] **Real-time Analysis**: Análise em tempo real de transações
- [ ] **Export Avançado**: Relatórios em PDF/Excel com gráficos

---

## ✅ Resultado Final

O sistema agora oferece uma **análise investigativa de nível profissional**, capaz de:

1. **Identificar automaticamente** pessoas e empresas de alto risco
2. **Detectar padrões suspeitos** como lavagem de dinheiro e estruturação  
3. **Analisar redes complexas** com algoritmos de centralidade
4. **Gerar relatórios executivos** com recomendações acionáveis
5. **Scoring inteligente** baseado em múltiplos fatores de risco

**O sistema está agora muito mais robusto e profissional para investigações reais!** 🎯 