# 🔧 InvestigIA - Solução de Problemas

## 🚀 EXECUÇÃO RÁPIDA (RECOMENDADA)

### Método 1: Mais Simples
1. **Abra o arquivo diretamente**: `investigia_final.html`
2. **Arraste para o navegador** ou **clique duplo**
3. **Pronto!** O sistema funciona 100% no navegador

### Método 2: Com Servidor Local
1. **Execute**: `EXECUTAR_INVESTIGIA.bat`
2. **Escolha opção 2**: "Executar apenas HTML"
3. **Sistema abre automaticamente**

---

## ❌ PROBLEMAS COMUNS E SOLUÇÕES

### 1. "Arquivo não encontrado" ou "Module not found"

**PROBLEMA**: Tentando executar scripts Python que não existem
```
python run_simple.py
python run_funcional.py
python -m uvicorn backend.main:app
```

**SOLUÇÃO**: 
- ✅ **Use**: `EXECUTAR_INVESTIGIA.bat`
- ✅ **Ou abra**: `investigia_final.html` diretamente
- ❌ **NÃO execute** scripts Python antigos

### 2. PowerShell não reconhece "&&"

**PROBLEMA**: 
```
cd frontend && python -m http.server 3000
O token '&&' não é um separador de instruções válido
```

**SOLUÇÃO PowerShell**:
```powershell
cd investig-ia
python -m http.server 8000
```

**SOLUÇÃO CMD**:
```cmd
cd investig-ia && python -m http.server 8000
```

### 3. Sistema mostra dados fictícios

**PROBLEMA**: Após carregar arquivos, aparecem "João Silva", "Maria Santos"

**SOLUÇÃO**: 
- ✅ Use `investigia_final.html` (versão limpa)
- ❌ Não use arquivos antigos como `investigia.html`

### 4. Upload de Excel não funciona

**PROBLEMA**: Arquivo .xlsx carregado mas "0 entidades encontradas"

**SOLUÇÃO**: 
- ✅ Sistema atual suporta Excel automaticamente
- ✅ Verifique se dados estão em formato tabular
- ✅ Use dados com nomes, empresas, valores, datas

### 5. JavaScript desabilitado

**PROBLEMA**: Página não carrega funcionalidades

**SOLUÇÃO**:
1. **Chrome**: Configurações → Privacidade → JavaScript → Permitir
2. **Firefox**: about:config → javascript.enabled → true
3. **Edge**: Configurações → JavaScript → Permitir

---

## 📁 ESTRUTURA DE ARQUIVOS

### Arquivos Principais (USE ESTES):
- `investigia_final.html` - **Sistema principal completo**
- `EXECUTAR_INVESTIGIA.bat` - **Script de execução**
- `VERIFICAR_SISTEMA.html` - **Teste de funcionamento**
- `dados_filtros_teste.csv` - **Dados de exemplo**

### Arquivos Antigos (NÃO USE):
- `run_simple.py` - Removido
- `run_funcional.py` - Removido  
- `investigia.html` - Versão antiga
- Scripts Python diversos - Desnecessários

---

## 🧪 TESTE RÁPIDO

### 1. Verificar Sistema
```
1. Abra: VERIFICAR_SISTEMA.html
2. Clique: "Testar Sistema"
3. Resultado: Deve mostrar "Sistema 100% Funcional"
```

### 2. Teste com Dados Reais
```
1. Abra: investigia_final.html
2. Carregue: dados_filtros_teste.csv
3. Resultado: Deve processar e mostrar entidades
```

---

## 🌐 NAVEGADORES SUPORTADOS

### ✅ Totalmente Compatível:
- **Google Chrome** 90+
- **Microsoft Edge** 90+
- **Mozilla Firefox** 88+
- **Safari** 14+

### ⚠️ Limitações:
- **Internet Explorer** - Não suportado
- **Navegadores muito antigos** - Funcionalidade limitada

---

## 🔍 DIAGNÓSTICO AVANÇADO

### Verificar Console do Navegador:
1. **F12** para abrir ferramentas
2. **Console** tab
3. Procurar por **erros vermelhos**

### Erros Comuns no Console:
- `CORS error` - Use servidor local
- `File not found` - Verifique caminho dos arquivos
- `Script error` - JavaScript desabilitado

---

## 📊 DADOS DE TESTE

### Formato CSV Recomendado:
```csv
Nome,Empresa,Valor,Data,Observacoes
João Silva,ABC Ltda,R$ 15000,15/01/2024,Pagamento consultor
Maria Santos,XYZ S.A.,R$ 25000,20/01/2024,Contrato prestação
```

### Formato TXT Recomendado:
```
Em 15/01/2024, João Silva da ABC Ltda recebeu R$ 15.000.
Maria Santos, diretora da XYZ S.A., aprovou pagamento de R$ 25.000.
```

---

## 🆘 SUPORTE EMERGENCIAL

### Se NADA funcionar:

1. **Baixe navegador atualizado**:
   - Chrome: https://www.google.com/chrome/
   - Edge: https://www.microsoft.com/edge/

2. **Teste básico**:
   - Abra `VERIFICAR_SISTEMA.html`
   - Se não funcionar = problema do navegador

3. **Último recurso**:
   - Use `DIAGNOSTICO_SISTEMA.html`
   - Mostra diagnóstico completo

---

## 📱 VERSÃO MOBILE

O sistema funciona em **tablets e smartphones**:
- **Android**: Chrome, Samsung Internet
- **iOS**: Safari, Chrome
- **Interface responsiva** se adapta à tela

---

## 🔒 SEGURANÇA E PRIVACIDADE

- ✅ **100% Local** - Nenhum dado enviado para servidores
- ✅ **Sem instalação** - Roda direto no navegador  
- ✅ **Sem cadastro** - Uso imediato
- ✅ **Dados privados** - Permanecem no seu computador

---

## 📞 CONTATO TÉCNICO

Se os problemas persistirem:
1. **Documente o erro** (screenshot do console)
2. **Informe o navegador** e versão
3. **Descreva os passos** que causaram o problema
4. **Inclua arquivo de teste** se possível

**Sistema testado e funcionando em ambientes Windows, Mac e Linux.** 