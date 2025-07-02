#!/usr/bin/env python3
"""
Analisador Avançado de Fraudes e Investigação Financeira
Detecta padrões suspeitos, lavagem de dinheiro e redes criminosas
"""

import pandas as pd
import networkx as nx
import numpy as np
from datetime import datetime, timedelta
from collections import defaultdict, Counter
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

class AdvancedFraudAnalyzer:
    """
    Analisador avançado para detecção de fraudes e investigação financeira.
    
    Características principais:
    - Detecção de structuring (fracionamento)
    - Análise de movimentações circulares
    - Identificação de redes suspeitas
    - Análise de padrões temporais
    - Detecção de outliers financeiros
    - Mapeamento de conexões ocultas
    """
    
    def __init__(self):
        self.data = None
        self.graph = nx.DiGraph()
        self.suspicious_patterns = {}
        self.risk_scores = {}
        self.investigation_results = {}
        self.alert_threshold = 10000  # Limiar para alertas
        self.structuring_threshold = 10000  # Limiar para estruturação
        
    def load_data(self, data_source, file_type='csv'):
        """Carrega dados de transações financeiras."""
        try:
            if file_type == 'csv':
                if isinstance(data_source, str):
                    self.data = pd.read_csv(data_source)
                else:
                    self.data = data_source
            elif file_type == 'excel':
                self.data = pd.read_excel(data_source)
            
            # Padronizar nomes das colunas
            self.data.columns = [col.strip().lower().replace(' ', '_') for col in self.data.columns]
            
            # Converter valores monetários
            self._clean_financial_data()
            
            # Converter datas
            self._parse_dates()
            
            print(f"✅ Dados carregados: {len(self.data)} transações")
            print(f"📊 Colunas disponíveis: {list(self.data.columns)}")
            
            return True
            
        except Exception as e:
            print(f"❌ Erro ao carregar dados: {e}")
            return False
    
    def _clean_financial_data(self):
        """Limpa e padroniza dados financeiros."""
        # Identificar coluna de valor
        value_cols = [col for col in self.data.columns if any(x in col for x in ['valor', 'value', 'amount', 'quantia'])]
        
        for col in value_cols:
            if self.data[col].dtype == 'object':
                # Remover símbolos de moeda e formatar
                self.data[col] = self.data[col].astype(str).str.replace(r'[R$\s]', '', regex=True)
                self.data[col] = self.data[col].str.replace(',', '.')
                self.data[col] = pd.to_numeric(self.data[col], errors='coerce')
        
        # Remover valores nulos
        self.data = self.data.dropna(subset=value_cols)
    
    def _parse_dates(self):
        """Converte colunas de data."""
        date_cols = [col for col in self.data.columns if any(x in col for x in ['data', 'date', 'quando'])]
        
        for col in date_cols:
            self.data[col] = pd.to_datetime(self.data[col], errors='coerce')
    
    def build_transaction_network(self, source_col='nome', target_col='empresa', 
                                value_col='valor', date_col='data'):
        """Constrói rede de transações."""
        if self.data is None:
            print("❌ Nenhum dado carregado")
            return False
        
        # Criar grafo direcionado
        self.graph = nx.DiGraph()
        
        # Adicionar transações como arestas
        for _, row in self.data.iterrows():
            source = str(row[source_col]).strip()
            target = str(row[target_col]).strip()
            value = float(row[value_col]) if pd.notna(row[value_col]) else 0
            date = row[date_col] if date_col in self.data.columns else None
            
            # Adicionar ou atualizar aresta
            if self.graph.has_edge(source, target):
                # Somar valores e adicionar datas
                self.graph[source][target]['total_value'] += value
                self.graph[source][target]['transaction_count'] += 1
                self.graph[source][target]['transactions'].append({
                    'value': value,
                    'date': date,
                    'row_index': row.name
                })
            else:
                self.graph.add_edge(source, target, 
                                  total_value=value,
                                  transaction_count=1,
                                  transactions=[{
                                      'value': value,
                                      'date': date,
                                      'row_index': row.name
                                  }])
        
        # Calcular métricas dos nós
        self._calculate_node_metrics()
        
        print(f"🕸️ Rede construída: {self.graph.number_of_nodes()} entidades, {self.graph.number_of_edges()} conexões")
        return True
    
    def _calculate_node_metrics(self):
        """Calcula métricas avançadas dos nós."""
        for node in self.graph.nodes():
            # Fluxos de entrada e saída
            in_flow = sum([self.graph[source][node]['total_value'] 
                          for source in self.graph.predecessors(node)])
            out_flow = sum([self.graph[node][target]['total_value'] 
                           for target in self.graph.successors(node)])
            
            # Contadores de transações
            in_transactions = sum([self.graph[source][node]['transaction_count'] 
                                  for source in self.graph.predecessors(node)])
            out_transactions = sum([self.graph[node][target]['transaction_count'] 
                                   for target in self.graph.successors(node)])
            
            # Métricas de centralidade
            in_degree = self.graph.in_degree(node)
            out_degree = self.graph.out_degree(node)
            
            # Atualizar atributos do nó
            self.graph.nodes[node].update({
                'in_flow': in_flow,
                'out_flow': out_flow,
                'total_flow': in_flow + out_flow,
                'net_flow': in_flow - out_flow,
                'in_transactions': in_transactions,
                'out_transactions': out_transactions,
                'total_transactions': in_transactions + out_transactions,
                'in_degree': in_degree,
                'out_degree': out_degree,
                'total_degree': in_degree + out_degree
            })
    
    def detect_structuring_patterns(self, threshold=10000, tolerance=0.1):
        """
        Detecta padrões de estruturação (fracionamento de valores).
        
        Estruturação é dividir uma grande transação em várias pequenas 
        para evitar reportes obrigatórios.
        """
        structuring_alerts = []
        
        # Agrupar transações por pessoa e período
        if 'data' in self.data.columns:
            self.data['date_group'] = self.data['data'].dt.date
        else:
            self.data['date_group'] = 'sem_data'
        
        # Identificar possível estruturação
        for person in self.data['nome'].unique():
            person_data = self.data[self.data['nome'] == person]
            
            # Agrupar por data
            for date_group in person_data['date_group'].unique():
                day_transactions = person_data[person_data['date_group'] == date_group]
                
                if len(day_transactions) >= 3:  # Múltiplas transações no mesmo dia
                    values = day_transactions['valor'].tolist()
                    total_value = sum(values)
                    
                    # Verificar se valores são similares (indicativo de estruturação)
                    if len(values) >= 3:
                        avg_value = np.mean(values)
                        std_value = np.std(values)
                        
                        # Coeficiente de variação baixo indica valores similares
                        if avg_value > 0 and (std_value / avg_value) < tolerance:
                            if total_value > threshold:
                                structuring_alerts.append({
                                    'person': person,
                                    'date': date_group,
                                    'transaction_count': len(values),
                                    'individual_values': values,
                                    'total_value': total_value,
                                    'avg_value': avg_value,
                                    'std_value': std_value,
                                    'coefficient_variation': std_value / avg_value,
                                    'risk_level': 'ALTO' if total_value > threshold * 2 else 'MÉDIO'
                                })
        
        self.suspicious_patterns['structuring'] = structuring_alerts
        return structuring_alerts
    
    def detect_circular_transactions(self, min_cycle_length=3):
        """Detecta transações circulares suspeitas."""
        circular_patterns = []
        
        # Encontrar ciclos no grafo
        try:
            cycles = list(nx.simple_cycles(self.graph))
            
            for cycle in cycles:
                if len(cycle) >= min_cycle_length:
                    # Calcular valor total do ciclo
                    total_value = 0
                    cycle_transactions = []
                    
                    for i in range(len(cycle)):
                        source = cycle[i]
                        target = cycle[(i + 1) % len(cycle)]
                        
                        if self.graph.has_edge(source, target):
                            edge_value = self.graph[source][target]['total_value']
                            total_value += edge_value
                            cycle_transactions.append({
                                'from': source,
                                'to': target,
                                'value': edge_value,
                                'transactions': self.graph[source][target]['transaction_count']
                            })
                    
                    if total_value > self.alert_threshold:
                        circular_patterns.append({
                            'cycle': cycle,
                            'cycle_length': len(cycle),
                            'total_value': total_value,
                            'avg_value': total_value / len(cycle),
                            'transactions': cycle_transactions,
                            'risk_level': 'CRÍTICO' if total_value > self.alert_threshold * 5 else 'ALTO'
                        })
        
        except Exception as e:
            print(f"Erro ao detectar ciclos: {e}")
        
        # Ordenar por valor total
        circular_patterns.sort(key=lambda x: x['total_value'], reverse=True)
        
        self.suspicious_patterns['circular'] = circular_patterns
        return circular_patterns
    
    def identify_hub_entities(self, top_n=10):
        """Identifica entidades centrais (hubs) na rede."""
        hub_analysis = []
        
        for node in self.graph.nodes():
            node_data = self.graph.nodes[node]
            
            # Calcular score de centralidade
            centrality_score = (
                node_data.get('total_degree', 0) * 0.3 +
                node_data.get('total_flow', 0) / 100000 * 0.4 +  # Normalizar valor
                node_data.get('total_transactions', 0) * 0.3
            )
            
            hub_analysis.append({
                'entity': node,
                'total_connections': node_data.get('total_degree', 0),
                'in_connections': node_data.get('in_degree', 0),
                'out_connections': node_data.get('out_degree', 0),
                'total_flow': node_data.get('total_flow', 0),
                'in_flow': node_data.get('in_flow', 0),
                'out_flow': node_data.get('out_flow', 0),
                'net_flow': node_data.get('net_flow', 0),
                'total_transactions': node_data.get('total_transactions', 0),
                'centrality_score': centrality_score,
                'risk_level': self._calculate_risk_level(centrality_score)
            })
        
        # Ordenar por score de centralidade
        hub_analysis.sort(key=lambda x: x['centrality_score'], reverse=True)
        
        self.investigation_results['hubs'] = hub_analysis[:top_n]
        return hub_analysis[:top_n]
    
    def _calculate_risk_level(self, score):
        """Calcula nível de risco baseado no score."""
        if score > 100:
            return 'CRÍTICO'
        elif score > 50:
            return 'ALTO'
        elif score > 20:
            return 'MÉDIO'
        else:
            return 'BAIXO'
    
    def detect_unusual_patterns(self):
        """Detecta padrões incomuns nas transações."""
        unusual_patterns = []
        
        # Análise de outliers de valores
        values = self.data['valor'].values
        q1, q3 = np.percentile(values, [25, 75])
        iqr = q3 - q1
        outlier_threshold = q3 + 1.5 * iqr
        
        outliers = self.data[self.data['valor'] > outlier_threshold]
        
        for _, transaction in outliers.iterrows():
            unusual_patterns.append({
                'type': 'high_value_outlier',
                'person': transaction['nome'],
                'company': transaction['empresa'],
                'value': transaction['valor'],
                'date': transaction.get('data', 'N/A'),
                'percentile': (transaction['valor'] > values).mean() * 100,
                'description': f"Transação {transaction['valor']:.2f} é outlier (acima do percentil {(transaction['valor'] > values).mean() * 100:.1f}%)"
            })
        
        # Padrões de frequência suspeitos
        person_frequency = self.data['nome'].value_counts()
        high_frequency_persons = person_frequency[person_frequency > person_frequency.quantile(0.9)]
        
        for person, count in high_frequency_persons.items():
            person_data = self.data[self.data['nome'] == person]
            avg_value = person_data['valor'].mean()
            total_value = person_data['valor'].sum()
            
            unusual_patterns.append({
                'type': 'high_frequency',
                'person': person,
                'transaction_count': count,
                'average_value': avg_value,
                'total_value': total_value,
                'companies': person_data['empresa'].nunique(),
                'description': f"{person} tem {count} transações (acima do normal)"
            })
        
        self.suspicious_patterns['unusual'] = unusual_patterns
        return unusual_patterns
    
    def analyze_temporal_patterns(self):
        """Analisa padrões temporais suspeitos."""
        if 'data' not in self.data.columns:
            return []
        
        temporal_analysis = []
        
        # Análise por dia da semana
        self.data['day_of_week'] = self.data['data'].dt.dayofweek
        self.data['hour'] = self.data['data'].dt.hour
        
        # Transações em horários incomuns (noites, fins de semana)
        weekend_transactions = self.data[self.data['day_of_week'].isin([5, 6])]
        night_transactions = self.data[self.data['hour'].isin([22, 23, 0, 1, 2, 3, 4, 5])]
        
        if len(weekend_transactions) > 0:
            temporal_analysis.append({
                'pattern': 'weekend_activity',
                'count': len(weekend_transactions),
                'total_value': weekend_transactions['valor'].sum(),
                'avg_value': weekend_transactions['valor'].mean(),
                'description': f"{len(weekend_transactions)} transações em fins de semana"
            })
        
        if len(night_transactions) > 0:
            temporal_analysis.append({
                'pattern': 'night_activity',
                'count': len(night_transactions),
                'total_value': night_transactions['valor'].sum(),
                'avg_value': night_transactions['valor'].mean(),
                'description': f"{len(night_transactions)} transações noturnas"
            })
        
        self.suspicious_patterns['temporal'] = temporal_analysis
        return temporal_analysis
    
    def generate_comprehensive_report(self):
        """Gera relatório completo da investigação."""
        print("🔍 RELATÓRIO COMPLETO DE INVESTIGAÇÃO FINANCEIRA")
        print("=" * 80)
        
        # Executar todas as análises
        print("\n📊 1. ANÁLISE DE ESTRUTURAÇÃO (FRACIONAMENTO)")
        structuring = self.detect_structuring_patterns()
        if structuring:
            print(f"   ⚠️  {len(structuring)} padrões de estruturação detectados")
            for pattern in structuring[:3]:  # Top 3
                print(f"   • {pattern['person']}: {pattern['transaction_count']} transações de R$ {pattern['avg_value']:.2f} (Total: R$ {pattern['total_value']:.2f})")
        else:
            print("   ✅ Nenhum padrão de estruturação detectado")
        
        print("\n🔄 2. ANÁLISE DE TRANSAÇÕES CIRCULARES")
        circular = self.detect_circular_transactions()
        if circular:
            print(f"   ⚠️  {len(circular)} ciclos suspeitos detectados")
            for cycle in circular[:3]:  # Top 3
                print(f"   • Ciclo de {cycle['cycle_length']} entidades: R$ {cycle['total_value']:.2f}")
        else:
            print("   ✅ Nenhum ciclo suspeito detectado")
        
        print("\n🎯 3. ENTIDADES CENTRAIS (HUBS)")
        hubs = self.identify_hub_entities()
        if hubs:
            print(f"   📈 Top {len(hubs)} entidades mais conectadas:")
            for hub in hubs[:5]:  # Top 5
                print(f"   • {hub['entity']}: {hub['total_connections']} conexões, R$ {hub['total_flow']:.2f} total")
        
        print("\n🚨 4. PADRÕES INCOMUNS")
        unusual = self.detect_unusual_patterns()
        if unusual:
            print(f"   ⚠️  {len(unusual)} padrões incomuns detectados")
            for pattern in unusual[:3]:  # Top 3
                print(f"   • {pattern['type']}: {pattern['description']}")
        else:
            print("   ✅ Nenhum padrão incomum detectado")
        
        print("\n⏰ 5. ANÁLISE TEMPORAL")
        temporal = self.analyze_temporal_patterns()
        if temporal:
            for pattern in temporal:
                print(f"   • {pattern['description']}: R$ {pattern['total_value']:.2f}")
        else:
            print("   ✅ Nenhum padrão temporal suspeito")
        
        print("\n" + "=" * 80)
        print("📋 RESUMO EXECUTIVO:")
        print(f"   • Total de transações analisadas: {len(self.data)}")
        print(f"   • Entidades únicas: {self.graph.number_of_nodes()}")
        print(f"   • Conexões totais: {self.graph.number_of_edges()}")
        print(f"   • Valor total movimentado: R$ {self.data['valor'].sum():.2f}")
        print(f"   • Alertas de estruturação: {len(structuring)}")
        print(f"   • Ciclos suspeitos: {len(circular)}")
        print(f"   • Padrões incomuns: {len(unusual)}")
        
        # Calcular score de risco geral
        total_alerts = len(structuring) + len(circular) + len(unusual)
        risk_score = min(100, total_alerts * 10)
        
        print(f"\n🎯 SCORE DE RISCO GERAL: {risk_score}/100")
        if risk_score >= 70:
            print("   🚨 RISCO CRÍTICO - Investigação imediata recomendada")
        elif risk_score >= 40:
            print("   ⚠️  RISCO ALTO - Monitoramento intensivo recomendado")
        elif risk_score >= 20:
            print("   ⚡ RISCO MÉDIO - Monitoramento regular recomendado")
        else:
            print("   ✅ RISCO BAIXO - Padrões normais detectados")
        
        return {
            'structuring': structuring,
            'circular': circular,
            'hubs': hubs,
            'unusual': unusual,
            'temporal': temporal,
            'risk_score': risk_score
        }
    
    def create_investigation_visualization(self):
        """Cria visualização interativa para investigação."""
        if self.graph.number_of_nodes() == 0:
            return None
        
        # Calcular layout
        pos = nx.spring_layout(self.graph, k=2, iterations=50)
        
        # Preparar dados dos nós
        node_x = []
        node_y = []
        node_text = []
        node_size = []
        node_color = []
        
        for node in self.graph.nodes():
            x, y = pos[node]
            node_x.append(x)
            node_y.append(y)
            
            # Informações do nó
            node_data = self.graph.nodes[node]
            text = f"<b>{node}</b><br>"
            text += f"Conexões: {node_data.get('total_degree', 0)}<br>"
            text += f"Fluxo Total: R$ {node_data.get('total_flow', 0):,.2f}<br>"
            text += f"Entrada: R$ {node_data.get('in_flow', 0):,.2f}<br>"
            text += f"Saída: R$ {node_data.get('out_flow', 0):,.2f}<br>"
            text += f"Transações: {node_data.get('total_transactions', 0)}"
            node_text.append(text)
            
            # Tamanho baseado no fluxo total
            size = 10 + (node_data.get('total_flow', 0) / 10000)
            node_size.append(min(50, max(10, size)))
            
            # Cor baseada no fluxo líquido
            net_flow = node_data.get('net_flow', 0)
            node_color.append(net_flow)
        
        # Preparar dados das arestas
        edge_x = []
        edge_y = []
        edge_text = []
        
        for edge in self.graph.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])
        
        # Criar gráfico
        fig = go.Figure()
        
        # Adicionar arestas
        fig.add_trace(go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=1, color='rgba(125, 125, 125, 0.3)'),
            hoverinfo='none',
            mode='lines',
            name='Conexões'
        ))
        
        # Adicionar nós
        fig.add_trace(go.Scatter(
            x=node_x, y=node_y,
            mode='markers+text',
            hoverinfo='text',
            hovertext=node_text,
            text=[str(node)[:15] + '...' if len(str(node)) > 15 else str(node) for node in self.graph.nodes()],
            textposition="middle center",
            marker=dict(
                size=node_size,
                color=node_color,
                colorscale='RdYlBu',
                colorbar=dict(title="Fluxo Líquido (R$)"),
                line=dict(width=2, color='white')
            ),
            name='Entidades'
        ))
        
        # Configurar layout
        fig.update_layout(
            title="🔍 Rede de Investigação Financeira",
            showlegend=False,
            hovermode='closest',
            margin=dict(b=20, l=5, r=5, t=40),
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            plot_bgcolor='white',
            height=600
        )
        
        return fig
    
    def export_investigation_report(self, filename_prefix='investigation_report'):
        """Exporta relatório de investigação."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        # Gerar relatório
        report = self.generate_comprehensive_report()
        
        # Salvar em Excel
        with pd.ExcelWriter(f"{filename_prefix}_{timestamp}.xlsx", engine='openpyxl') as writer:
            # Aba principal com resumo
            summary_data = {
                'Métrica': ['Total Transações', 'Entidades Únicas', 'Valor Total', 'Score de Risco'],
                'Valor': [len(self.data), self.graph.number_of_nodes(), 
                         f"R$ {self.data['valor'].sum():,.2f}", f"{report.get('risk_score', 0)}/100"]
            }
            pd.DataFrame(summary_data).to_excel(writer, sheet_name='Resumo', index=False)
            
            # Aba de estruturação
            if report['structuring']:
                structuring_df = pd.DataFrame(report['structuring'])
                structuring_df.to_excel(writer, sheet_name='Estruturação', index=False)
            
            # Aba de hubs
            if report['hubs']:
                hubs_df = pd.DataFrame(report['hubs'])
                hubs_df.to_excel(writer, sheet_name='Entidades_Centrais', index=False)
            
            # Aba de padrões incomuns
            if report['unusual']:
                unusual_df = pd.DataFrame(report['unusual'])
                unusual_df.to_excel(writer, sheet_name='Padrões_Incomuns', index=False)
        
        print(f"📄 Relatório exportado: {filename_prefix}_{timestamp}.xlsx")
        return f"{filename_prefix}_{timestamp}.xlsx"

def main():
    """Função principal para teste."""
    analyzer = AdvancedFraudAnalyzer()
    
    # Carregar dados de exemplo
    if analyzer.load_data('dados_investigacao_avancada.csv'):
        # Construir rede
        analyzer.build_transaction_network()
        
        # Gerar relatório completo
        analyzer.generate_comprehensive_report()
        
        # Exportar resultados
        analyzer.export_investigation_report()

if __name__ == "__main__":
    main()