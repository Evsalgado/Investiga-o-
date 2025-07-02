# 🚀 InvestigIA - Sistema Funcionando - Guia Completo

## 🎯 Visão Geral
O InvestigIA é uma plataforma completa de análise investigativa que funciona 100% no navegador, sem necessidade de backend complexo. O sistema foi desenvolvido com filtros dinâmicos inspirados em ferramentas profissionais como **i2 Analyst Notebook**.

## ✅ Status do Sistema

### **FUNCIONANDO PERFEITAMENTE**
- ✅ Sistema principal (`investigia_final.html`)
- ✅ Filtros dinâmicos com dados reais
- ✅ Processamento de arquivos Excel/CSV/TXT
- ✅ Rede de vínculos automática
- ✅ Interface estilo Mercado Livre/Mercado Pago
- ✅ Zero dados fictícios
- ✅ Carregamento automático da rede
- ✅ Diagnóstico completo do sistema

## 🚀 Como Iniciar

### **Método 1: Script Automático**
```bash
# Execute na pasta investig-ia
INICIAR_SISTEMA.bat
```

**Opções disponíveis:**
1. **Sistema Principal** - Plataforma completa
2. **Teste Rápido** - Verificação básica
3. **Diagnóstico** - Análise completa do sistema
4. **Servidor HTTP** - Apenas servidor

### **Método 2: Manual**
```bash
# Na pasta investig-ia
python -m http.server 8000

# Acesse no navegador:
http://localhost:8000/investigia_final.html
```

## 📊 Funcionalidades Principais

### **1. Filtros Dinâmicos Estilo i2**
- **Contadores em Tempo Real**: Mostra quantidades reais de cada tipo
- **Filtros por Entidade**: Pessoas, empresas, locais com contadores
- **Filtros por Conexão**: Financeiro, corporativo, temporal, etc.
- **Filtros Específicos**: Listas de pessoas/empresas com seleção múltipla
- **Período Automático**: Define datas baseado nos dados reais
- **Reset Inteligente**: Volta aos valores padrão

### **2. Processamento Real de Dados**
- **Excel (.xlsx)**: Biblioteca XLSX.js integrada
- **CSV**: Processamento linha por linha
- **TXT**: Extração por regex avançado
- **Detecção Automática**: Identifica colunas automaticamente
- **Extração Inteligente**: Pessoas, empresas, valores, datas

### **3. Rede de Vínculos Automática**
- **Carregamento Automático**: Rede aparece após processar arquivos
- **Mudança de Aba**: Sistema muda automaticamente para rede
- **Conexões Reais**: Baseadas nos dados processados
- **Visualização Interativa**: Grafo clicável com detalhes
- **Estatísticas Dinâmicas**: Contadores e métricas reais

### **4. Interface Profissional**
- **Identidade ML/MP**: Cores e design do Mercado Livre
- **Responsiva**: Funciona em desktop e mobile
- **Animações**: Transições suaves e feedback visual
- **Notificações**: Mensagens de status em tempo real

## 📁 Arquivos de Teste

### **dados_filtros_teste.csv**
Arquivo com dados complexos para demonstrar os filtros:
- 5 pessoas diferentes
- 4 empresas diferentes
- 20 transações
- 3 meses de dados (Jan-Mar 2024)
- Múltiplos tipos de vínculos

### **Como Testar**
1. Execute `INICIAR_SISTEMA.bat`
2. Escolha opção 1 (Sistema Principal)
3. Carregue `dados_filtros_teste.csv`
4. Observe os contadores sendo preenchidos
5. Teste diferentes combinações de filtros
6. Veja a rede sendo carregada automaticamente

## 🔧 Diagnóstico e Troubleshooting

### **Sistema de Diagnóstico**
Execute `DIAGNOSTICO_SISTEMA.html` para:
- ✅ Verificar conectividade
- ✅ Testar arquivos
- ✅ Validar JavaScript
- ✅ Simular processamento
- ✅ Baixar relatório completo

### **Problemas Comuns e Soluções**

| Problema | Solução |
|----------|---------|
| Página não carrega | Verificar se está na pasta `investig-ia` |
| Arquivos não processam | Usar formato CSV com cabeçalho |
| Filtros vazios | Carregar arquivo com dados válidos |
| Rede não aparece | Aguardar 2 segundos após processamento |
| Erro de porta | Mudar para porta 8001, 8002, etc. |

### **URLs de Acesso**
- **Sistema Principal**: `http://localhost:8000/investigia_final.html`
- **Teste Rápido**: `http://localhost:8000/TESTE_RAPIDO.html`
- **Diagnóstico**: `http://localhost:8000/DIAGNOSTICO_SISTEMA.html`

## 🎯 Fluxo de Uso Recomendado

### **1. Preparação**
```bash
1. Abra terminal na pasta investig-ia
2. Execute: INICIAR_SISTEMA.bat
3. Escolha opção 1 (Sistema Principal)
```

### **2. Carregamento de Dados**
```bash
1. Clique em "Selecionar Arquivos"
2. Escolha arquivo CSV/Excel/TXT
3. Clique "Processar Arquivos"
4. Aguarde processamento automático
```

### **3. Análise com Filtros**
```bash
1. Observe contadores sendo preenchidos
2. Use filtros por tipo de entidade
3. Filtre por conexões específicas
4. Selecione pessoas/empresas específicas
5. Ajuste período temporal
6. Use "Reset Filtros" quando necessário
```

### **4. Exploração da Rede**
```bash
1. Rede carrega automaticamente após 2s
2. Clique nos nós para ver detalhes
3. Use controles de visualização
4. Analise estatísticas no painel lateral
5. Exporte dados se necessário
```

## 🌟 Destaques Técnicos

### **Arquitetura**
- **Frontend-Only**: Sem necessidade de backend
- **Bibliotecas CDN**: XLSX.js para Excel
- **ES5 Compatible**: Funciona em navegadores antigos
- **Responsive Design**: CSS Grid e Flexbox

### **Algoritmos**
- **Detecção de Entidades**: Regex avançado
- **Análise de Vínculos**: Baseada em co-ocorrência
- **Filtros Múltiplos**: Aplicação em tempo real
- **Cálculo de Intensidade**: Frequência + valores

### **Performance**
- **Processamento Assíncrono**: Não trava a interface
- **Carregamento Progressivo**: Feedback visual
- **Filtros Eficientes**: Algoritmos otimizados
- **Memória Gerenciada**: Limpeza automática

## 📈 Melhorias Implementadas

### **Filtros Dinâmicos**
- ✅ Contadores automáticos por categoria
- ✅ Listas de entidades com frequência
- ✅ Seleção múltipla de pessoas/empresas
- ✅ Período automático baseado nas datas
- ✅ Reset inteligente de todos os filtros

### **Experiência do Usuário**
- ✅ Carregamento automático da rede
- ✅ Mudança automática de aba
- ✅ Notificações visuais de progresso
- ✅ Logs detalhados no console
- ✅ Mensagens de status em tempo real

### **Qualidade dos Dados**
- ✅ Zero dados fictícios
- ✅ Processamento de dados reais
- ✅ Detecção inteligente de colunas
- ✅ Extração robusta de entidades
- ✅ Validação de tipos de arquivo

## 🎉 Conclusão

O InvestigIA está **100% funcional** como uma plataforma profissional de análise investigativa que rivaliza com soluções comerciais como:

- **i2 Analyst Notebook** (filtros avançados)
- **Caseboard** (rede de vínculos)
- **Palantir Gotham** (análise de entidades)

**Principais vantagens:**
- ✅ Gratuito e open-source
- ✅ Funciona inteiramente no navegador
- ✅ Interface moderna e intuitiva
- ✅ Filtros dinâmicos profissionais
- ✅ Processamento de dados reais
- ✅ Rede de vínculos automática

---

*Sistema desenvolvido seguindo as melhores práticas de ferramentas profissionais de investigação e análise de dados.* 