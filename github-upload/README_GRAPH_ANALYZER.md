# 🕸️ Ferramenta de Análise de Conexões via Grafo

Uma ferramenta poderosa para análise de redes complexas baseada em dados de planilhas Excel ou CSV. Permite visualizar conexões, identificar padrões e extrair insights de dados relacionais.

## 🎯 Funcionalidades Principais

### 📊 Análise de Dados
- **Carregamento de arquivos**: Suporte para Excel (.xlsx, .xls) e CSV
- **Limpeza automática**: Processamento inteligente de valores monetários e datas
- **Validação de dados**: Verificação automática da integridade dos dados

### 🕸️ Criação de Grafos
- **Grafos direcionados e não-direcionados**: Flexibilidade para diferentes tipos de análise
- **Pesos nas arestas**: Considera a força das conexões
- **Atributos personalizados**: Incorpora informações adicionais dos dados

### 📈 Métricas de Análise
- **Centralidade de Grau**: Identifica nós com mais conexões
- **Centralidade de Intermediação**: Encontra nós que servem como pontes
- **Centralidade de Proximidade**: Mede a proximidade média entre nós
- **Detecção de Comunidades**: Identifica grupos densamente conectados
- **Análise de Componentes**: Verifica conectividade da rede

### 🎨 Visualização Interativa
- **Múltiplos layouts**: Spring, circular, random, shell
- **Customização visual**: Tamanho e cor dos nós baseados em métricas
- **Interface intuitiva**: Navegação por clique e arraste
- **Tooltips informativos**: Detalhes sobre nós e conexões

## 🚀 Como Usar

### 1. Instalação e Configuração

```bash
# Navegue até o diretório da ferramenta
cd extensions/investig-ia

# Execute o script de inicialização
python run_graph_analyzer.py
```

O script verificará automaticamente as dependências e oferecerá instalá-las se necessário.

### 2. Preparação dos Dados

Sua planilha deve conter pelo menos duas colunas representando entidades que se conectam:

**Exemplo de estrutura de dados:**

| Pessoa | Empresa | Valor | Tipo | Data |
|--------|---------|-------|------|------|
| João Silva | ABC Corp | 50000 | Contrato | 15/01/2023 |
| Maria Santos | XYZ Ltd | 30000 | Serviço | 22/03/2023 |
| Carlos Oliveira | DEF Co | 25000 | Pagamento | 10/05/2023 |

### 3. Interface Web

A ferramenta abre uma interface web em `http://localhost:8501` com:

#### 📁 Painel Lateral (Configurações)
- **Upload de arquivo**: Arraste e solte ou selecione arquivo
- **Configuração do grafo**:
  - Coluna Origem: Entidades de origem das conexões
  - Coluna Destino: Entidades de destino das conexões
  - Coluna de Peso: Força da conexão (opcional)
  - Tipo de grafo: Direcionado ou não-direcionado
  - Atributos adicionais: Informações extras para análise

#### 🖥️ Área Principal
- **🕸️ Visualização do Grafo**: Grafo interativo com controles de customização
- **📊 Dashboard de Métricas**: Gráficos e tabelas com análise completa
- **🏆 Rankings**: Nós mais importantes por diferentes métricas
- **💾 Exportar**: Download dos resultados em CSV e JSON

## 📋 Exemplos de Uso

### 1. Análise de Transações Financeiras
```
Colunas necessárias: Pessoa, Empresa, Valor
Resultado: Rede de relacionamentos comerciais
```

### 2. Análise de Comunicações
```
Colunas necessárias: Remetente, Destinatário, Frequência
Resultado: Rede de comunicação organizacional
```

### 3. Análise de Colaborações
```
Colunas necessárias: Autor1, Autor2, Projeto
Resultado: Rede de colaboração acadêmica/profissional
```

## 🔧 Dependências

A ferramenta utiliza as seguintes bibliotecas Python:

```
pandas>=1.5.0          # Manipulação de dados
networkx>=2.8.0        # Análise de grafos
plotly>=5.10.0         # Visualização interativa
streamlit>=1.25.0      # Interface web
openpyxl>=3.0.0        # Leitura de Excel
numpy>=1.21.0          # Computação numérica
python-louvain>=0.16   # Detecção de comunidades
scikit-learn>=1.2.0    # Algoritmos de machine learning
```

## 📊 Métricas Explicadas

### Centralidade de Grau
Mede quantas conexões diretas um nó possui. Nós com alta centralidade de grau são "hubs" na rede.

### Centralidade de Intermediação
Identifica nós que frequentemente aparecem nos caminhos mais curtos entre outros nós. São pontos críticos de controle de fluxo.

### Centralidade de Proximidade
Mede quão próximo um nó está de todos os outros nós da rede. Nós centrais têm acesso mais rápido a toda a rede.

### Detecção de Comunidades
Identifica grupos de nós densamente conectados entre si, mas com poucas conexões com outros grupos.

## 🎯 Casos de Uso Práticos

### 🔍 Investigação Criminal
- Análise de redes de comunicação
- Identificação de atores centrais
- Mapeamento de organizações criminosas

### 🏢 Análise Corporativa
- Redes de fornecedores e clientes
- Análise de fluxos financeiros
- Identificação de riscos de concentração

### 📚 Pesquisa Acadêmica
- Redes de colaboração científica
- Análise de citações
- Mapeamento de comunidades de pesquisa

### 💼 Compliance e Auditoria
- Análise de transações suspeitas
- Mapeamento de relacionamentos de risco
- Identificação de conflitos de interesse

## 🛡️ Segurança e Privacidade

- **Processamento local**: Todos os dados são processados localmente
- **Sem armazenamento**: Dados não são persistidos automaticamente
- **Controle total**: Usuário controla exportação e compartilhamento

## 🆘 Solução de Problemas

### Erro de dependências
```bash
pip install -r requirements_graph.txt
```

### Erro de memória com arquivos grandes
- Reduza o tamanho do dataset
- Use amostragem dos dados
- Considere filtrar conexões menos relevantes

### Visualização lenta
- Limite o número de nós (< 1000 para melhor performance)
- Use layouts mais simples (circular, random)
- Reduza a complexidade dos atributos visuais

## 📈 Limitações e Considerações

- **Performance**: Recomendado para redes com até 5.000 nós
- **Memória**: Uso intensivo para grafos muito densos
- **Visualização**: Grafos muito grandes podem ser difíceis de interpretar

## 🔄 Atualizações Futuras

- [ ] Análise temporal de redes
- [ ] Algoritmos avançados de detecção de anomalias
- [ ] Exportação para formatos de outros softwares de análise
- [ ] API REST para integração
- [ ] Análise automatizada com IA

## 📞 Suporte

Para questões e suporte:
1. Verifique a documentação acima
2. Consulte os arquivos de exemplo incluídos
3. Execute o script de diagnóstico para verificar a instalação

---

🔬 **Desenvolvido para análise profissional de redes complexas**