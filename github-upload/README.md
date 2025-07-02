# 🔍 InvestigIA - Plataforma de Análise Investigativa Inteligente

## 📝 Descrição

O **InvestigIA** é uma plataforma completa de análise investigativa que utiliza inteligência artificial para detectar padrões suspeitos, analisar relacionamentos entre entidades e visualizar dados complexos através de grafos interativos.

## ✨ Principais Funcionalidades

### 🎯 Análise Visual Avançada
- **Grafo Interativo**: Visualização de relacionamentos com Cytoscape.js
- **Customização Visual**: Ícones e cores personalizáveis por campo
- **Análise Otimizada**: Foco automático nas conexões mais importantes
- **Múltiplos Layouts**: Força, hierárquico, circular, grade, concêntrico

### 🔍 Detecção de Fraudes
- **Estruturação (Fracionamento)**: Identificação de divisão de valores
- **Transações Circulares**: Detecção de ciclos suspeitos
- **Entidades Centrais**: Análise de hubs de alta conectividade
- **Padrões Temporais**: Atividades em horários suspeitos

### 🤖 Inteligência Artificial
- **Processamento de Linguagem Natural**: Consultas em português
- **Detecção de Padrões**: Algoritmos de ML para anomalias
- **Geração de Insights**: Recomendações automáticas
- **Análise de Sentimento**: Classificação de textos

### 📊 Análise de Dados
- **Upload Múltiplo**: CSV, Excel, XML
- **Processamento em Tempo Real**: Análise instantânea
- **Filtros Dinâmicos**: Busca e segmentação avançada
- **Exportação**: PNG, JSON, relatórios

## 🏗️ Arquitetura

### Frontend
- **HTML5 Puro**: Interface principal responsiva
- **React Alternative**: Dashboard moderno com Material-UI
- **JavaScript ES6+**: Funcionalidades avançadas
- **Cytoscape.js**: Visualização de grafos

### Backend
- **FastAPI**: API RESTful de alta performance
- **Python 3.8+**: Processamento de dados
- **Pydantic**: Validação e serialização
- **NetworkX**: Análise de grafos

### Análise
- **Streamlit**: Interface de investigação avançada
- **Pandas**: Manipulação de dados
- **Plotly**: Visualizações interativas
- **Scikit-learn**: Machine Learning

## 🚀 Como Usar

### 1. Interface Web Principal
```bash
# Abrir o arquivo principal no navegador
file:///caminho/para/app_principal.html
```

### 2. Aplicação Streamlit
```bash
# Executar investigação avançada
python -m streamlit run advanced_investigation_app.py
```

### 3. API Backend
```bash
# Iniciar servidor FastAPI
python backend/main.py
# Acessar: http://localhost:8000
```

### 4. Frontend React
```bash
# Instalar dependências e executar
cd frontend
npm install
npm start
```

## 📦 Instalação

### Dependências Python
```bash
pip install streamlit pandas plotly networkx fastapi uvicorn pydantic
pip install openpyxl xlsxwriter python-multipart
```

### Dependências Frontend (React)
```bash
npm install @mui/material @emotion/react @emotion/styled
npm install @mui/icons-material plotly.js-dist-min
```

## 📁 Estrutura do Projeto

```
InvestigIA/
├── app_principal.html          # Interface web principal
├── advanced_investigation_app.py   # Aplicação Streamlit
├── graph_analyzer.py          # Analisador de grafos
├── advanced_fraud_analyzer.py # Detector de fraudes
├── backend/                   # API FastAPI
│   ├── main.py               # Servidor principal
│   ├── models/               # Esquemas de dados
│   └── services/             # Serviços de IA
├── frontend/                 # Interface React
│   ├── src/                  # Código fonte
│   └── public/              # Recursos públicos
└── docs/                     # Documentação
```

## 🎨 Exemplos de Uso

### 1. Análise de Transações Financeiras
- Upload de planilha CSV/Excel
- Mapeamento automático de campos
- Visualização de fluxos suspeitos
- Detecção de estruturação

### 2. Investigação de Relacionamentos
- Identificação de entidades centrais
- Análise de comunidades
- Detecção de ciclos
- Métricas de centralidade

### 3. Detecção de Fraudes
- Padrões temporais incomuns
- Valores atípicos
- Atividades coordenadas
- Alertas automáticos

## 🛠️ Funcionalidades Avançadas

### Sistema de Cores Automático
- 🔴 Ultra Alto (≥ R$ 1M)
- 🟠 Muito Alto (≥ R$ 500K)  
- 🟣 Roxo Alto (≥ R$ 250K)
- 🟡 Alto (≥ R$ 100K)
- 🔵 Médio (≥ R$ 50K)
- 🔷 Médio-Baixo (≥ R$ 10K)
- 🟢 Baixo (< R$ 10K)

### Personalização Visual
- Ícones FontAwesome
- Cores por valor
- Tamanhos dinâmicos
- Layouts adaptativos

## 📈 Métricas de Análise

### Centralidade
- **Grau**: Número de conexões
- **Intermediação**: Importância como ponte
- **Proximidade**: Distância média
- **Autovetor**: Influência na rede

### Detecção de Padrões
- **Frequência**: Repetição de transações
- **Valores**: Análise estatística
- **Timing**: Padrões temporais
- **Geografía**: Distribuição espacial

## 🔧 Configuração

### Variáveis de Ambiente
```bash
OPENAI_API_KEY=sua_chave_aqui    # Para IA avançada (opcional)
DATABASE_URL=sqlite:///app.db    # Banco de dados
DEBUG=True                       # Modo desenvolvimento
```

### Configurações da API
- **Host**: 0.0.0.0
- **Porta**: 8000
- **CORS**: Habilitado para desenvolvimento
- **Documentação**: /docs (Swagger UI)

## 🤝 Contribuições

Contribuições são bem-vindas! Por favor:

1. Faça fork do projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🆘 Suporte

Para suporte e dúvidas:
- Abra uma **Issue** no GitHub
- Consulte a **documentação** na pasta `docs/`
- Verifique os **exemplos** de uso

## 🏆 Status do Projeto

**Versão**: 1.0.0  
**Status**: ✅ Produção  
**Última Atualização**: Janeiro 2025

### Recursos Implementados
- ✅ Interface web responsiva
- ✅ API REST completa
- ✅ Análise de grafos
- ✅ Detecção de fraudes
- ✅ IA integrada
- ✅ Exportação de dados
- ✅ Múltiplos formatos de entrada

### Próximas Versões
- 🔄 Dashboard em tempo real
- 🔄 Integração com bases externas
- 🔄 Machine Learning avançado
- 🔄 Relatórios automatizados

---

**InvestigIA** - Transformando dados em insights investigativos 🔍 