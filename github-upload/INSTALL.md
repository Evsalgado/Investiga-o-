# 🚀 Guia de Instalação - InvestigIA

## 📋 Pré-requisitos

### Python 3.8+
```bash
python --version  # Verificar se está instalado
```

### Node.js 16+ (para frontend React)
```bash
node --version    # Verificar se está instalado
npm --version     # Verificar NPM
```

## ⚡ Instalação Rápida

### 1. Clone o Repositório
```bash
git clone https://github.com/Evsalgado/Investiga-o-.git
cd Investiga-o-
```

### 2. Instalar Dependências Python
```bash
pip install -r requirements.txt
```

### 3. Instalar Dependências Frontend (opcional)
```bash
cd frontend
npm install
cd ..
```

## 🎯 Executar o Sistema

### Opção 1: Interface Web Principal (Recomendado)
```bash
# Abrir no navegador
app_principal.html
```

### Opção 2: Aplicação Streamlit
```bash
streamlit run advanced_investigation_app.py
```

### Opção 3: API Backend
```bash
python backend/main.py
# Acesse: http://localhost:8000
```

### Opção 4: Frontend React
```bash
cd frontend
npm start
# Acesse: http://localhost:3000
```

## 🔧 Configuração Avançada

### Variáveis de Ambiente (opcional)
Crie um arquivo `.env`:
```bash
OPENAI_API_KEY=sua_chave_openai_aqui
DEBUG=True
DATABASE_URL=sqlite:///app.db
```

### Instalação de Modelos NLP (opcional)
```bash
python -m spacy download pt_core_news_sm
```

## 📱 Scripts de Inicialização

### Windows
- `EXECUTAR_AGORA.bat` - Inicia sistema completo
- `TESTE_RAPIDO.bat` - Teste básico
- `ABRIR_APP_I2_ENHANCED.bat` - Interface principal

### Linux/Mac
```bash
# Dar permissão de execução
chmod +x *.sh

# Executar
./start_system.sh
```

## 🔍 Verificação da Instalação

### Teste Python
```bash
python -c "import pandas, networkx, streamlit; print('✅ Dependências OK')"
```

### Teste Frontend
```bash
cd frontend
npm test
```

## 🆘 Solução de Problemas

### Erro: ModuleNotFoundError
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Erro: Node não encontrado
```bash
# Instalar Node.js do site oficial
# https://nodejs.org/
```

### Porta em uso
```bash
# Verificar portas em uso
netstat -tulpn | grep :8000
```

## 📊 Dados de Exemplo

O sistema incluí dados de exemplo para teste:
- `data/sample_data/transacoes_financeiras.csv`
- `data/sample_data/caso_fraude_corporativa.txt`

## 🎓 Primeiros Passos

1. **Abra `app_principal.html`** no navegador
2. **Carregue um arquivo CSV** com dados de transações
3. **Configure os campos** (origem, destino, valor)
4. **Clique em "Gerar Grafo"**
5. **Explore as análises** e filtros

## 📚 Documentação Adicional

- `README.md` - Visão geral do projeto
- `TROUBLESHOOTING.md` - Solução de problemas
- `docs/` - Documentação técnica completa

## 🎯 Arquivos Principais

- `app_principal.html` - Interface web principal
- `advanced_investigation_app.py` - Análise avançada
- `graph_analyzer.py` - Analisador de grafos
- `backend/main.py` - API FastAPI

## ✅ Checklist de Instalação

- [ ] Python 3.8+ instalado
- [ ] Dependências Python instaladas
- [ ] Interface web funcionando
- [ ] Aplicação Streamlit funcionando
- [ ] Dados de exemplo carregados
- [ ] Testes básicos executados

---

**Pronto para investigar!** 🕵️‍♂️ 