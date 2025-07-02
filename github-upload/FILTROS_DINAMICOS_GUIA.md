# 🔍 Guia dos Filtros Dinâmicos - InvestigIA

## 🎯 Visão Geral
Os filtros foram redesenhados seguindo as melhores práticas de ferramentas profissionais como **i2 Analyst Notebook**, carregando automaticamente os dados reais processados.

## ✨ Funcionalidades Implementadas

### 1. **Filtros com Contadores Dinâmicos**
- **Tipo de Entidade**: Mostra quantas pessoas, empresas e locais foram encontrados
- **Tipo de Conexão**: Exibe contadores reais de vínculos por categoria
- **Atualização Automática**: Contadores se atualizam após processar arquivos

### 2. **Filtros Específicos por Entidade**
- **Pessoas Específicas**: Lista todas as pessoas encontradas com frequência
- **Empresas Específicas**: Lista todas as empresas com número de documentos
- **Seleção Múltipla**: Permite selecionar várias entidades simultaneamente

### 3. **Filtros Temporais Inteligentes**
- **Período Automático**: Define automaticamente o range baseado nas datas encontradas
- **Filtro por Data**: Filtra conexões dentro do período selecionado
- **Sem Campo de Valor**: Removido conforme solicitado

### 4. **Controles Avançados**
- **Intensidade Mínima**: Slider de 1-10 baseado na força das conexões
- **Reset Inteligente**: Botão para voltar aos valores padrão
- **Aplicação em Tempo Real**: Filtros se aplicam automaticamente

## 🔄 Como Funciona

### Processamento Automático
```javascript
1. Usuário carrega arquivos
2. Sistema processa e extrai entidades
3. atualizarFiltrosDinamicos() é chamada
4. Filtros são populados com dados reais
5. Contadores são atualizados
6. Rede é carregada automaticamente
```

### Análise de Vínculos
```javascript
- Vínculos Financeiros: Detectados por valores monetários
- Vínculos Corporativos: Pessoas + empresas no mesmo documento  
- Vínculos Temporais: Baseados em datas encontradas
- Vínculos Geográficos: Baseados em locais identificados
- Vínculos Pessoais: Pessoas no mesmo documento
```

## 📊 Exemplo de Uso

### Dados de Entrada (CSV)
```csv
nome,empresa,valor,data,local
Carlos Silva,TechCorp Ltda,15000.50,15/01/2024,São Paulo/SP
Maria Santos,TechCorp Ltda,12500.00,16/01/2024,São Paulo/SP
```

### Filtros Gerados
- **Pessoas (2)**: Carlos Silva, Maria Santos
- **Empresas (1)**: TechCorp Ltda  
- **Vínculos Financeiros (2)**: Detectados pelos valores
- **Período**: 15/01/2024 a 16/01/2024 (automático)

## 🎛️ Controles Disponíveis

### Filtros Principais
| Filtro | Opções | Descrição |
|--------|--------|-----------|
| Tipo de Entidade | Todas, Pessoas (N), Empresas (N), Locais (N) | Filtra por tipo com contadores |
| Tipo de Conexão | Todos, Financeiro (N), Corporativo (N), etc. | Filtra por categoria de vínculo |
| Intensidade | 1-10 | Força mínima da conexão |
| Período | Data início/fim | Range temporal automático |

### Filtros Específicos
| Filtro | Funcionalidade |
|--------|---------------|
| Pessoas Específicas | Lista com frequência de documentos |
| Empresas Específicas | Lista com número de documentos |
| Seleção Múltipla | Permite várias entidades simultaneamente |

## 🔧 Funções Implementadas

### `atualizarFiltrosDinamicos()`
- Atualiza contadores com dados reais
- Popula listas de pessoas e empresas
- Define período automático
- Calcula vínculos por tipo

### `aplicarFiltroRede()`
- Aplica todos os filtros simultaneamente
- Filtra por entidade, conexão, intensidade, período
- Filtra por pessoas/empresas específicas
- Mostra resultados em tempo real

### `resetarFiltros()`
- Reset inteligente para valores padrão
- Recarrega rede completa
- Notificação visual do reset

## 🚀 Melhorias Implementadas

### Inspiradas no i2 Analyst
- ✅ Filtros com contadores em tempo real
- ✅ Seleção múltipla de entidades
- ✅ Filtros temporais automáticos
- ✅ Reset inteligente
- ✅ Aplicação em tempo real

### Experiência do Usuário
- ✅ Dados reais (zero dados fictícios)
- ✅ Contadores visuais
- ✅ Mensagens de status
- ✅ Botões de reset
- ✅ Logs detalhados no console

## 📝 Como Testar

1. **Execute**: `TESTE_FILTROS_DINAMICOS.bat`
2. **Carregue**: `dados_filtros_teste.csv`
3. **Observe**: Contadores sendo atualizados
4. **Teste**: Diferentes combinações de filtros
5. **Verifique**: Console para logs detalhados

## 🎯 Resultados Esperados

- Filtros populados automaticamente com dados reais
- Contadores precisos por categoria
- Filtragem em tempo real funcionando
- Período automático baseado nas datas
- Reset completo funcionando
- Zero dados fictícios exibidos

---
*Sistema desenvolvido seguindo padrões profissionais de ferramentas como i2 Analyst Notebook e Caseboard* 