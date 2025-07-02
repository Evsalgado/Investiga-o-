# 🔧 Guia de Solução de Problemas - InvestigIA

## 🚨 **Problemas Comuns e Soluções**

### **Problema 1: Não consegue acessar http://localhost:3000**

#### **Diagnóstico:**
```bash
# Verificar se os serviços estão rodando
netstat -ano | findstr :3000  # Windows
lsof -i :3000                 # Linux/Mac
```

#### **Soluções:**

**📋 Passo 1: Verificar Pré-requisitos**
```bash
# Verificar versão do Python
python --version  # Deve ser 3.8+

# Verificar Node.js
node --version     # Deve ser 16+
npm --version      # Deve estar instalado
```

**📋 Passo 2: Execução Manual (se run_dev.py falhar)**

**Backend:**
```bash
cd investig-ia/backend
python -m venv venv

# Windows
venv\Scripts\activate
# Linux/Mac  
source venv/bin/activate

pip install -r requirements.txt
python -m spacy download pt_core_news_sm
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Frontend (em outro terminal):**
```bash
cd investig-ia/frontend
npm install
npm start
```

---

### **Problema 2: Erro de Importação no Backend**

#### **Erro:** `ImportError: No module named 'fastapi'`

#### **Solução:**
```bash
cd backend
pip install --upgrade pip
pip install -r requirements.txt
```

#### **Se persistir:**
```bash
# Criar novo ambiente virtual
python -m venv venv_new
# Ativar e reinstalar
venv_new\Scripts\activate  # Windows
pip install -r requirements.txt
```

---

### **Problema 3: Erro do spaCy**

#### **Erro:** `OSError: [E050] Can't find model 'pt_core_news_sm'`

#### **Solução:**
```bash
# Baixar modelo português
python -m spacy download pt_core_news_sm

# Se falhar, usar modelo inglês
python -m spacy download en_core_web_sm
```

---

### **Problema 4: Porta em Uso**

#### **Erro:** `Address already in use`

#### **Solução:**
```bash
# Verificar processo usando a porta
netstat -ano | findstr :8000    # Windows
lsof -i :8000                   # Linux/Mac

# Matar processo (substitua PID)
taskkill /PID <PID> /F          # Windows
kill -9 <PID>                   # Linux/Mac

# Ou usar porta diferente
uvicorn main:app --port 8001
```

---

### **Problema 5: Frontend Não Carrega**

#### **Diagnóstico:**
1. Verificar se o backend está rodando em `localhost:8000`
2. Verificar erros no console do navegador (F12)
3. Verificar se todas as dependências foram instaladas

#### **Solução:**
```bash
cd frontend
rm -rf node_modules package-lock.json  # Limpar cache
npm install                             # Reinstalar
npm start                              # Executar
```

---

## 🔍 **Verificação Completa do Sistema**

### **Script de Diagnóstico**
Execute este comando para verificar tudo:

```bash
# Criar arquivo de diagnóstico
python -c "
import sys
import subprocess
import os

print('🔍 Diagnóstico do InvestigIA')
print('=' * 40)

# Verificar Python
print(f'Python: {sys.version}')

# Verificar diretórios
dirs = ['backend', 'frontend', 'data']
for d in dirs:
    status = '✅' if os.path.exists(d) else '❌'
    print(f'{status} Diretório {d}')

# Verificar Node.js
try:
    result = subprocess.run(['node', '--version'], capture_output=True, text=True)
    print(f'✅ Node.js: {result.stdout.strip()}')
except:
    print('❌ Node.js não encontrado')

# Verificar npm
try:
    result = subprocess.run(['npm', '--version'], capture_output=True, text=True)
    print(f'✅ npm: {result.stdout.strip()}')
except:
    print('❌ npm não encontrado')

print('\n📋 Próximos passos:')
print('1. Corrigir itens marcados com ❌')
print('2. Executar: python run_dev.py')
print('3. Acessar: http://localhost:3000')
"
```

---

## 🆘 **Execução Alternativa (Modo Simples)**

Se nada funcionar, tente esta versão simplificada:

### **Backend Simplificado:**
```bash
cd backend
pip install fastapi uvicorn python-multipart
echo 'from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "InvestigIA Backend Online"}
' > simple_main.py

uvicorn simple_main:app --reload
```

### **Frontend Simplificado:**
```bash
cd frontend
npx create-react-app . --template typescript
npm start
```

---

## 📞 **Quando Solicitar Ajuda**

Inclua estas informações:

1. **Sistema Operacional:** Windows/Linux/Mac
2. **Versão Python:** `python --version`
3. **Versão Node:** `node --version`
4. **Erro completo:** Copie a mensagem de erro
5. **Comandos executados:** O que você tentou fazer
6. **Logs:** Saída dos comandos

---

## 🚀 **Versão de Desenvolvimento Rápida**

Para demonstração imediata, use:

```bash
# Backend básico
pip install fastapi uvicorn
uvicorn --version

# Frontend básico  
npx create-react-app demo-app
cd demo-app
npm start
```

---

## 💡 **Dicas Importantes**

1. **Sempre use ambientes virtuais** para Python
2. **Verifique se as portas 3000 e 8000 estão livres**
3. **Execute cada comando em terminais separados**
4. **Aguarde alguns segundos entre iniciar backend e frontend**
5. **Use CTRL+C para parar os serviços**

---

**🎯 Objetivo:** Ter o sistema funcionando em `http://localhost:3000`

Se seguir todos os passos e ainda tiver problemas, o issue pode ser específico do seu ambiente. Nesse caso, podemos criar uma versão ainda mais simplificada ou usar alternativas como Docker. 