#!/usr/bin/env python3
"""
Aplicação Streamlit Avançada para Investigação de Fraudes
Interface moderna e robusta para análise investigativa
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from advanced_fraud_analyzer import AdvancedFraudAnalyzer
import io
import base64
from datetime import datetime
import json

# Configuração da página
st.set_page_config(
    page_title="🔍 Investigação Avançada de Fraudes",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #e74c3c;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .section-header {
        font-size: 1.5rem;
        font-weight: bold;
        color: #2c3e50;
        margin: 1rem 0;
        padding: 0.5rem;
        background: linear-gradient(90deg, #f8f9fa, #e9ecef);
        border-left: 4px solid #e74c3c;
    }
    
    .risk-critical {
        background-color: #dc3545;
        color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
        font-weight: bold;
    }
    
    .risk-high {
        background-color: #fd7e14;
        color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
        font-weight: bold;
    }
    
    .risk-medium {
        background-color: #ffc107;
        color: black;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
        font-weight: bold;
    }
    
    .risk-low {
        background-color: #28a745;
        color: white;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
        font-weight: bold;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 1rem;
        color: white;
        margin: 0.5rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .alert-box {
        background-color: #fff3cd;
        border: 1px solid #ffeaa7;
        color: #856404;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(180deg, #2c3e50 0%, #34495e 100%);
    }
    
    .stButton > button {
        background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%);
        color: white;
        border: none;
        padding: 0.5rem 2rem;
        font-weight: bold;
        border-radius: 0.5rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #c0392b 0%, #a93226 100%);
        transform: translateY(-2px);
        box-shadow: 0 6px 8px rgba(0,0,0,0.15);
    }
</style>
""", unsafe_allow_html=True)

# Título principal
st.markdown('<h1 class="main-header">🔍 INVESTIGAÇÃO AVANÇADA DE FRAUDES</h1>', unsafe_allow_html=True)

# Inicializar o analisador na sessão
if 'analyzer' not in st.session_state:
    st.session_state.analyzer = AdvancedFraudAnalyzer()
    st.session_state.data_loaded = False
    st.session_state.analysis_complete = False
    st.session_state.investigation_results = {}

# Sidebar para configurações
st.sidebar.markdown("## ⚙️ Configurações de Investigação")
st.sidebar.markdown("---")

# Upload de arquivo
st.sidebar.markdown("### 📁 Carregar Dados")
uploaded_file = st.sidebar.file_uploader(
    "Arquivo de Transações",
    type=['csv', 'xlsx', 'xls'],
    help="Carregue dados de transações financeiras para análise"
)

# Configurações de detecção
st.sidebar.markdown("### 🎯 Parâmetros de Detecção")

alert_threshold = st.sidebar.number_input(
    "Limiar de Alerta (R$)", 
    min_value=1000, 
    max_value=1000000, 
    value=10000, 
    step=1000,
    help="Valor mínimo para gerar alertas"
)

structuring_threshold = st.sidebar.number_input(
    "Limiar de Estruturação (R$)", 
    min_value=5000, 
    max_value=500000, 
    value=10000, 
    step=1000,
    help="Limiar para detectar fracionamento de valores"
)

tolerance = st.sidebar.slider(
    "Tolerância de Similaridade", 
    min_value=0.05, 
    max_value=0.5, 
    value=0.1, 
    step=0.05,
    help="Tolerância para detectar valores similares (estruturação)"
)

# Carregar dados
if uploaded_file is not None:
    try:
        # Determinar tipo de arquivo
        file_extension = uploaded_file.name.split('.')[-1].lower()
        
        if file_extension == 'csv':
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        
        # Carregar no analisador
        st.session_state.analyzer.data = df
        st.session_state.analyzer._clean_financial_data()
        st.session_state.analyzer._parse_dates()
        st.session_state.analyzer.alert_threshold = alert_threshold
        st.session_state.analyzer.structuring_threshold = structuring_threshold
        
        st.session_state.data_loaded = True
        
        st.sidebar.success(f"✅ Dados carregados!")
        st.sidebar.info(f"📊 {len(df)} transações, {len(df.columns)} colunas")
        
        # Detectar colunas automaticamente
        columns = list(df.columns)
        
        # Configurações das colunas
        st.sidebar.markdown("### 🔗 Mapeamento de Colunas")
        
        # Detectar colunas automaticamente
        name_cols = [col for col in columns if any(x in col.lower() for x in ['nome', 'name', 'pessoa', 'person'])]
        company_cols = [col for col in columns if any(x in col.lower() for x in ['empresa', 'company', 'corporação'])]
        value_cols = [col for col in columns if any(x in col.lower() for x in ['valor', 'value', 'amount', 'quantia'])]
        date_cols = [col for col in columns if any(x in col.lower() for x in ['data', 'date', 'quando'])]
        
        source_col = st.sidebar.selectbox(
            "Coluna de Origem (Pessoa/Entidade)",
            columns,
            index=columns.index(name_cols[0]) if name_cols else 0,
            help="Coluna que identifica quem fez a transação"
        )
        
        target_col = st.sidebar.selectbox(
            "Coluna de Destino (Empresa/Entidade)",
            columns,
            index=columns.index(company_cols[0]) if company_cols else 1,
            help="Coluna que identifica o destino da transação"
        )
        
        value_col = st.sidebar.selectbox(
            "Coluna de Valor",
            columns,
            index=columns.index(value_cols[0]) if value_cols else 2,
            help="Coluna com os valores das transações"
        )
        
        date_col = st.sidebar.selectbox(
            "Coluna de Data (opcional)",
            ["Nenhuma"] + columns,
            index=columns.index(date_cols[0]) + 1 if date_cols else 0,
            help="Coluna com as datas das transações"
        )
        date_col = None if date_col == "Nenhuma" else date_col
        
        # Botão para iniciar análise
        if st.sidebar.button("🚀 INICIAR INVESTIGAÇÃO", type="primary"):
            with st.spinner("🔍 Realizando análise investigativa..."):
                # Construir rede
                success = st.session_state.analyzer.build_transaction_network(
                    source_col=source_col,
                    target_col=target_col,
                    value_col=value_col,
                    date_col=date_col
                )
                
                if success:
                    # Executar análises
                    results = st.session_state.analyzer.generate_comprehensive_report()
                    st.session_state.investigation_results = results
                    st.session_state.analysis_complete = True
                    st.sidebar.success("✅ Investigação concluída!")
                else:
                    st.sidebar.error("❌ Erro na análise")
        
    except Exception as e:
        st.sidebar.error(f"❌ Erro ao carregar arquivo: {e}")
        st.session_state.data_loaded = False

# Área principal
if not st.session_state.data_loaded:
    # Tela de boas-vindas
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div class="alert-box">
        <h3>🎯 Sistema de Investigação Avançada</h3>
        <p>Esta ferramenta utiliza algoritmos avançados de detecção de fraudes para identificar:</p>
        <ul>
            <li><strong>Estruturação (Fracionamento)</strong>: Divisão de valores para evitar detecção</li>
            <li><strong>Transações Circulares</strong>: Ciclos suspeitos de movimentação</li>
            <li><strong>Entidades Centrais</strong>: Pessoas/empresas com muitas conexões</li>
            <li><strong>Padrões Incomuns</strong>: Outliers e anomalias</li>
            <li><strong>Análise Temporal</strong>: Atividades em horários suspeitos</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        ### 📋 Formato dos Dados
        
        Sua planilha deve conter:
        - **Pessoa/Entidade**: Quem fez a transação
        - **Empresa/Destino**: Para onde foi a transação  
        - **Valor**: Quantia da transação
        - **Data**: Quando ocorreu (opcional)
        
        **Exemplo:**
        | Nome | Empresa | Valor | Data |
        |------|---------|-------|------|
        | João Silva | ABC Corp | 95000 | 15/01/2024 |
        | Maria Santos | XYZ Ltda | 180000 | 18/01/2024 |
        """)

elif not st.session_state.analysis_complete:
    # Mostrar preview dos dados
    st.markdown('<div class="section-header">📋 Preview dos Dados Carregados</div>', unsafe_allow_html=True)
    
    df = st.session_state.analyzer.data
    st.dataframe(df.head(10), use_container_width=True)
    
    # Métricas básicas
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("📊 Total de Transações", len(df))
    with col2:
        st.metric("💰 Valor Total", f"R$ {df['valor'].sum():,.2f}")
    with col3:
        st.metric("👥 Pessoas Únicas", df['nome'].nunique())
    with col4:
        st.metric("🏢 Empresas Únicas", df['empresa'].nunique())
    
    # Gráficos de distribuição
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📈 Distribuição de Valores")
        fig = px.histogram(df, x='valor', nbins=30, title="Distribuição de Valores das Transações")
        fig.update_layout(xaxis_title="Valor (R$)", yaxis_title="Frequência")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.markdown("### 👥 Top Pessoas por Transações")
        top_people = df['nome'].value_counts().head(10)
        fig = px.bar(x=top_people.values, y=top_people.index, orientation='h',
                     title="Pessoas com Mais Transações")
        fig.update_layout(xaxis_title="Número de Transações", yaxis_title="Pessoa")
        st.plotly_chart(fig, use_container_width=True)

else:
    # Interface principal com análise completa
    results = st.session_state.investigation_results
    analyzer = st.session_state.analyzer
    
    # Score de risco geral
    risk_score = results.get('risk_score', 0)
    
    if risk_score >= 70:
        risk_class = "risk-critical"
        risk_text = "🚨 RISCO CRÍTICO"
        risk_desc = "Investigação imediata recomendada"
    elif risk_score >= 40:
        risk_class = "risk-high"
        risk_text = "⚠️ RISCO ALTO"
        risk_desc = "Monitoramento intensivo recomendado"
    elif risk_score >= 20:
        risk_class = "risk-medium"
        risk_text = "⚡ RISCO MÉDIO"
        risk_desc = "Monitoramento regular recomendado"
    else:
        risk_class = "risk-low"
        risk_text = "✅ RISCO BAIXO"
        risk_desc = "Padrões normais detectados"
    
    st.markdown(f"""
    <div class="{risk_class}">
        <h3>{risk_text}</h3>
        <p>Score de Risco: {risk_score}/100</p>
        <p>{risk_desc}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Métricas principais
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("📊 Transações", len(analyzer.data))
    with col2:
        st.metric("🕸️ Entidades", analyzer.graph.number_of_nodes())
    with col3:
        st.metric("🔗 Conexões", analyzer.graph.number_of_edges())
    with col4:
        st.metric("💰 Valor Total", f"R$ {analyzer.data['valor'].sum():,.2f}")
    with col5:
        st.metric("🎯 Score Risco", f"{risk_score}/100")
    
    # Tabs para diferentes análises
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "🔍 Visão Geral", "📊 Estruturação", "🔄 Ciclos", 
        "🎯 Entidades Centrais", "🚨 Padrões Incomuns", "🕸️ Visualização"
    ])
    
    with tab1:
        st.markdown('<div class="section-header">📋 Resumo Executivo</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📊 Estatísticas Gerais")
            st.write(f"• **Transações analisadas**: {len(analyzer.data)}")
            st.write(f"• **Entidades únicas**: {analyzer.graph.number_of_nodes()}")
            st.write(f"• **Conexões totais**: {analyzer.graph.number_of_edges()}")
            st.write(f"• **Valor total**: R$ {analyzer.data['valor'].sum():,.2f}")
            
            st.markdown("### 🚨 Alertas Detectados")
            st.write(f"• **Estruturação**: {len(results.get('structuring', []))}")
            st.write(f"• **Ciclos suspeitos**: {len(results.get('circular', []))}")
            st.write(f"• **Padrões incomuns**: {len(results.get('unusual', []))}")
            st.write(f"• **Padrões temporais**: {len(results.get('temporal', []))}")
        
        with col2:
            # Gráfico de alertas
            alert_data = {
                'Tipo': ['Estruturação', 'Ciclos', 'Incomuns', 'Temporais'],
                'Quantidade': [
                    len(results.get('structuring', [])),
                    len(results.get('circular', [])),
                    len(results.get('unusual', [])),
                    len(results.get('temporal', []))
                ]
            }
            
            fig = px.bar(alert_data, x='Tipo', y='Quantidade', 
                        title="Alertas por Categoria",
                        color='Quantidade', color_continuous_scale='Reds')
            st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.markdown('<div class="section-header">📊 Análise de Estruturação (Fracionamento)</div>', unsafe_allow_html=True)
        
        structuring = results.get('structuring', [])
        
        if structuring:
            st.warning(f"⚠️ {len(structuring)} padrões de estruturação detectados!")
            
            # Criar DataFrame para exibição
            struct_df = pd.DataFrame(structuring)
            
            # Mostrar tabela
            st.dataframe(struct_df, use_container_width=True)
            
            # Gráfico de estruturação
            if len(structuring) > 0:
                fig = px.scatter(struct_df, x='transaction_count', y='total_value',
                               size='avg_value', color='risk_level',
                               hover_data=['person'], 
                               title="Padrões de Estruturação Detectados")
                fig.update_layout(xaxis_title="Número de Transações", yaxis_title="Valor Total (R$)")
                st.plotly_chart(fig, use_container_width=True)
        else:
            st.success("✅ Nenhum padrão de estruturação detectado")
    
    with tab3:
        st.markdown('<div class="section-header">🔄 Análise de Transações Circulares</div>', unsafe_allow_html=True)
        
        circular = results.get('circular', [])
        
        if circular:
            st.error(f"🚨 {len(circular)} ciclos suspeitos detectados!")
            
            for i, cycle in enumerate(circular[:5]):  # Mostrar top 5
                st.markdown(f"### Ciclo {i+1}")
                st.write(f"**Entidades**: {' → '.join(cycle['cycle'])}")
                st.write(f"**Valor Total**: R$ {cycle['total_value']:,.2f}")
                st.write(f"**Tamanho do Ciclo**: {cycle['cycle_length']} entidades")
                st.write(f"**Nível de Risco**: {cycle['risk_level']}")
                st.markdown("---")
        else:
            st.success("✅ Nenhum ciclo suspeito detectado")
    
    with tab4:
        st.markdown('<div class="section-header">🎯 Entidades Centrais (Hubs)</div>', unsafe_allow_html=True)
        
        hubs = results.get('hubs', [])
        
        if hubs:
            st.info(f"📈 Top {len(hubs)} entidades mais conectadas")
            
            # Criar DataFrame
            hubs_df = pd.DataFrame(hubs)
            
            # Mostrar tabela
            st.dataframe(hubs_df, use_container_width=True)
            
            # Gráfico de centralidade
            fig = px.scatter(hubs_df, x='total_connections', y='total_flow',
                           size='centrality_score', color='risk_level',
                           hover_data=['entity'], 
                           title="Entidades Centrais por Conexões e Fluxo")
            fig.update_layout(xaxis_title="Total de Conexões", yaxis_title="Fluxo Total (R$)")
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("📊 Análise de entidades centrais não disponível")
    
    with tab5:
        st.markdown('<div class="section-header">🚨 Padrões Incomuns</div>', unsafe_allow_html=True)
        
        unusual = results.get('unusual', [])
        
        if unusual:
            st.warning(f"⚠️ {len(unusual)} padrões incomuns detectados!")
            
            # Separar por tipo
            outliers = [p for p in unusual if p['type'] == 'high_value_outlier']
            high_freq = [p for p in unusual if p['type'] == 'high_frequency']
            
            if outliers:
                st.markdown("### 💰 Outliers de Valor Alto")
                outlier_df = pd.DataFrame(outliers)
                st.dataframe(outlier_df, use_container_width=True)
            
            if high_freq:
                st.markdown("### 🔁 Alta Frequência de Transações")
                freq_df = pd.DataFrame(high_freq)
                st.dataframe(freq_df, use_container_width=True)
        else:
            st.success("✅ Nenhum padrão incomum detectado")
    
    with tab6:
        st.markdown('<div class="section-header">🕸️ Visualização da Rede</div>', unsafe_allow_html=True)
        
        # Criar visualização
        fig = analyzer.create_investigation_visualization()
        
        if fig:
            st.plotly_chart(fig, use_container_width=True)
            
            # Controles de visualização
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### 📊 Legenda")
                st.markdown("""
                - **Tamanho do nó**: Proporcional ao fluxo total
                - **Cor do nó**: Baseada no fluxo líquido (entrada - saída)
                - **Azul**: Mais entrada que saída
                - **Vermelho**: Mais saída que entrada
                """)
            
            with col2:
                st.markdown("### 🎯 Interpretação")
                st.markdown("""
                - **Nós grandes**: Entidades com alto volume de transações
                - **Nós centrais**: Possíveis intermediários ou concentradores
                - **Clusters**: Grupos de entidades conectadas
                - **Conexões grossas**: Relacionamentos financeiros intensos
                """)
        else:
            st.error("❌ Erro ao gerar visualização")
    
    # Botão para exportar relatório
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col2:
        if st.button("📄 EXPORTAR RELATÓRIO COMPLETO", type="primary"):
            try:
                filename = analyzer.export_investigation_report()
                st.success(f"✅ Relatório exportado: {filename}")
            except Exception as e:
                st.error(f"❌ Erro ao exportar: {e}")

# Footer com informações
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.8rem;">
    🔍 Sistema de Investigação Avançada de Fraudes | 
    Desenvolvido para análise investigativa profissional | 
    Use com responsabilidade e dentro dos aspectos legais
</div>
""", unsafe_allow_html=True)