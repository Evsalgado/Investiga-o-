import pandas as pd
import networkx as nx
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
from collections import defaultdict, Counter
import openpyxl
from datetime import datetime
import streamlit as st
import json

class GraphAnalyzer:
    """
    Ferramenta para análise de conexões via grafo baseada em dados de planilhas Excel.
    Permite carregar dados, criar grafos e visualizar conexões entre entidades.
    """
    
    def __init__(self):
        self.data = None
        self.graph = nx.Graph()
        self.directed_graph = nx.DiGraph()
        self.node_attributes = {}
        self.edge_attributes = {}
        self.analysis_results = {}
        
    def load_excel_data(self, file_path, sheet_name=None):
        """
        Carrega dados de uma planilha Excel.
        
        Args:
            file_path: Caminho para o arquivo Excel
            sheet_name: Nome da planilha (opcional)
        """
        try:
            if sheet_name:
                self.data = pd.read_excel(file_path, sheet_name=sheet_name)
            else:
                self.data = pd.read_excel(file_path)
            
            # Limpar dados e converter tipos
            self.data = self.data.dropna()
            self._clean_data()
            
            print(f"Dados carregados com sucesso: {len(self.data)} linhas")
            print(f"Colunas: {list(self.data.columns)}")
            return True
            
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")
            return False
    
    def load_csv_data(self, file_path):
        """
        Carrega dados de um arquivo CSV.
        
        Args:
            file_path: Caminho para o arquivo CSV
        """
        try:
            self.data = pd.read_csv(file_path)
            self.data = self.data.dropna()
            self._clean_data()
            
            print(f"Dados carregados com sucesso: {len(self.data)} linhas")
            print(f"Colunas: {list(self.data.columns)}")
            return True
            
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")
            return False
    
    def _clean_data(self):
        """Limpa e padroniza os dados."""
        # Converter valores monetários
        for col in self.data.columns:
            if any(keyword in col.lower() for keyword in ['valor', 'value', 'amount', 'quantia']):
                if self.data[col].dtype == 'object':
                    # Remover símbolos de moeda e converter para float
                    self.data[col] = self.data[col].astype(str).str.replace(r'[R$\s,.]', '', regex=True)
                    self.data[col] = pd.to_numeric(self.data[col], errors='coerce')
        
        # Converter datas
        for col in self.data.columns:
            if any(keyword in col.lower() for keyword in ['data', 'date', 'quando']):
                self.data[col] = pd.to_datetime(self.data[col], errors='coerce')
    
    def create_graph_from_data(self, source_col, target_col, weight_col=None, 
                             directed=False, additional_attrs=None):
        """
        Cria um grafo baseado nos dados carregados.
        
        Args:
            source_col: Nome da coluna com nós de origem
            target_col: Nome da coluna com nós de destino
            weight_col: Nome da coluna com pesos das arestas (opcional)
            directed: Se o grafo é direcionado (True) ou não direcionado (False)
            additional_attrs: Lista de colunas adicionais para atributos dos nós/arestas
        """
        if self.data is None:
            print("Erro: Nenhum dado carregado")
            return False
        
        # Selecionar tipo de grafo
        if directed:
            self.graph = nx.DiGraph()
        else:
            self.graph = nx.Graph()
        
        # Adicionar arestas
        for _, row in self.data.iterrows():
            source = str(row[source_col])
            target = str(row[target_col])
            
            # Atributos da aresta
            edge_attrs = {}
            if weight_col and weight_col in self.data.columns:
                edge_attrs['weight'] = float(row[weight_col]) if pd.notna(row[weight_col]) else 1.0
            else:
                edge_attrs['weight'] = 1.0
            
            # Adicionar atributos adicionais
            if additional_attrs:
                for attr in additional_attrs:
                    if attr in self.data.columns:
                        edge_attrs[attr] = row[attr]
            
            # Adicionar aresta
            if self.graph.has_edge(source, target):
                # Se a aresta já existe, somar os pesos
                self.graph[source][target]['weight'] += edge_attrs['weight']
            else:
                self.graph.add_edge(source, target, **edge_attrs)
        
        # Calcular atributos dos nós
        self._calculate_node_attributes()
        
        print(f"Grafo criado com {self.graph.number_of_nodes()} nós e {self.graph.number_of_edges()} arestas")
        return True
    
    def _calculate_node_attributes(self):
        """Calcula atributos dos nós."""
        # Centralidade
        try:
            degree_centrality = nx.degree_centrality(self.graph)
            betweenness_centrality = nx.betweenness_centrality(self.graph)
            closeness_centrality = nx.closeness_centrality(self.graph)
            
            if isinstance(self.graph, nx.Graph):
                eigenvector_centrality = nx.eigenvector_centrality(self.graph, max_iter=1000)
            else:
                eigenvector_centrality = {}
            
            # Adicionar atributos aos nós
            for node in self.graph.nodes():
                self.graph.nodes[node]['degree_centrality'] = degree_centrality.get(node, 0)
                self.graph.nodes[node]['betweenness_centrality'] = betweenness_centrality.get(node, 0)
                self.graph.nodes[node]['closeness_centrality'] = closeness_centrality.get(node, 0)
                self.graph.nodes[node]['eigenvector_centrality'] = eigenvector_centrality.get(node, 0)
                
                # Força do nó (soma dos pesos das arestas)
                if isinstance(self.graph, nx.DiGraph):
                    in_strength = sum([self.graph[u][node].get('weight', 1) for u in self.graph.predecessors(node)])
                    out_strength = sum([self.graph[node][v].get('weight', 1) for v in self.graph.successors(node)])
                    self.graph.nodes[node]['in_strength'] = in_strength
                    self.graph.nodes[node]['out_strength'] = out_strength
                    self.graph.nodes[node]['total_strength'] = in_strength + out_strength
                else:
                    strength = sum([self.graph[node][neighbor].get('weight', 1) for neighbor in self.graph.neighbors(node)])
                    self.graph.nodes[node]['strength'] = strength
        
        except Exception as e:
            print(f"Erro ao calcular atributos dos nós: {e}")
    
    def detect_communities(self, method='louvain'):
        """
        Detecta comunidades no grafo.
        
        Args:
            method: Método de detecção ('louvain', 'greedy', 'label_propagation')
        """
        if self.graph.number_of_nodes() == 0:
            return {}
        
        try:
            if method == 'louvain':
                import community as community_louvain
                partition = community_louvain.best_partition(self.graph)
            elif method == 'greedy':
                communities = nx.algorithms.community.greedy_modularity_communities(self.graph)
                partition = {}
                for i, community in enumerate(communities):
                    for node in community:
                        partition[node] = i
            elif method == 'label_propagation':
                communities = nx.algorithms.community.label_propagation_communities(self.graph)
                partition = {}
                for i, community in enumerate(communities):
                    for node in community:
                        partition[node] = i
            else:
                return {}
            
            # Adicionar informação de comunidade aos nós
            for node, community_id in partition.items():
                self.graph.nodes[node]['community'] = community_id
            
            return partition
        
        except Exception as e:
            print(f"Erro na detecção de comunidades: {e}")
            return {}
    
    def analyze_graph(self):
        """Realiza análise completa do grafo."""
        if self.graph.number_of_nodes() == 0:
            return {}
        
        analysis = {}
        
        # Métricas básicas
        analysis['basic_metrics'] = {
            'nodes': self.graph.number_of_nodes(),
            'edges': self.graph.number_of_edges(),
            'density': nx.density(self.graph),
            'is_connected': nx.is_connected(self.graph) if isinstance(self.graph, nx.Graph) else nx.is_weakly_connected(self.graph)
        }
        
        # Componentes conectados
        if isinstance(self.graph, nx.Graph):
            components = list(nx.connected_components(self.graph))
        else:
            components = list(nx.weakly_connected_components(self.graph))
        
        analysis['components'] = {
            'count': len(components),
            'sizes': [len(comp) for comp in components]
        }
        
        # Nós mais importantes
        nodes_data = []
        for node in self.graph.nodes():
            node_data = {'node': node}
            node_data.update(self.graph.nodes[node])
            nodes_data.append(node_data)
        
        nodes_df = pd.DataFrame(nodes_data)
        
        # Top nós por diferentes métricas
        analysis['top_nodes'] = {}
        for metric in ['degree_centrality', 'betweenness_centrality', 'closeness_centrality']:
            if metric in nodes_df.columns:
                top_nodes = nodes_df.nlargest(10, metric)[['node', metric]].to_dict('records')
                analysis['top_nodes'][metric] = top_nodes
        
        # Comunidades
        communities = self.detect_communities()
        if communities:
            community_sizes = Counter(communities.values())
            analysis['communities'] = {
                'count': len(community_sizes),
                'sizes': dict(community_sizes)
            }
        
        self.analysis_results = analysis
        return analysis
    
    def create_interactive_visualization(self, layout='spring', node_size_attr='degree_centrality',
                                       edge_width_attr='weight', color_attr='community',
                                       title="Análise de Rede de Conexões"):
        """
        Cria visualização interativa do grafo.
        
        Args:
            layout: Tipo de layout ('spring', 'circular', 'random', 'shell')
            node_size_attr: Atributo para tamanho dos nós
            edge_width_attr: Atributo para largura das arestas
            color_attr: Atributo para colorir os nós
            title: Título do gráfico
        """
        if self.graph.number_of_nodes() == 0:
            return None
        
        # Calcular posições dos nós
        if layout == 'spring':
            pos = nx.spring_layout(self.graph, k=1, iterations=50)
        elif layout == 'circular':
            pos = nx.circular_layout(self.graph)
        elif layout == 'random':
            pos = nx.random_layout(self.graph)
        elif layout == 'shell':
            pos = nx.shell_layout(self.graph)
        else:
            pos = nx.spring_layout(self.graph)
        
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
            
            # Texto do nó
            text = f"<b>{node}</b><br>"
            for attr, value in self.graph.nodes[node].items():
                if isinstance(value, (int, float)):
                    text += f"{attr}: {value:.3f}<br>"
                else:
                    text += f"{attr}: {value}<br>"
            node_text.append(text)
            
            # Tamanho do nó
            if node_size_attr in self.graph.nodes[node]:
                size = self.graph.nodes[node][node_size_attr]
                node_size.append(20 + size * 30)  # Escalar tamanho
            else:
                node_size.append(20)
            
            # Cor do nó
            if color_attr in self.graph.nodes[node]:
                node_color.append(self.graph.nodes[node][color_attr])
            else:
                node_color.append(0)
        
        # Preparar dados das arestas
        edge_x = []
        edge_y = []
        edge_text = []
        edge_width = []
        
        for edge in self.graph.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])
            
            # Largura da aresta
            if edge_width_attr in self.graph.edges[edge]:
                width = self.graph.edges[edge][edge_width_attr]
                edge_width.append(max(1, width / max([self.graph.edges[e].get(edge_width_attr, 1) for e in self.graph.edges()]) * 5))
            else:
                edge_width.append(1)
        
        # Criar gráfico
        fig = go.Figure()
        
        # Adicionar arestas
        fig.add_trace(go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=2, color='rgba(125, 125, 125, 0.5)'),
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
            text=[str(node) for node in self.graph.nodes()],
            textposition="middle center",
            marker=dict(
                size=node_size,
                color=node_color,
                colorscale='Viridis',
                colorbar=dict(title=color_attr),
                line=dict(width=2, color='white')
            ),
            name='Entidades'
        ))
        
        # Configurar layout
        fig.update_layout(
            title=title,
            showlegend=False,
            hovermode='closest',
            margin=dict(b=20, l=5, r=5, t=40),
            annotations=[
                dict(
                    text="Clique e arraste para navegar. Passe o mouse sobre os nós para ver detalhes.",
                    showarrow=False,
                    xref="paper", yref="paper",
                    x=0.005, y=-0.002,
                    xanchor='left', yanchor='bottom',
                    font=dict(color='gray', size=12)
                )
            ],
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            plot_bgcolor='white'
        )
        
        return fig
    
    def create_metrics_dashboard(self):
        """Cria dashboard com métricas do grafo."""
        if not self.analysis_results:
            self.analyze_graph()
        
        # Criar subplots
        fig = make_subplots(
            rows=2, cols=2,
            subplot_titles=('Distribuição de Grau', 'Centralidade de Intermediação', 
                          'Tamanho das Comunidades', 'Métricas Principais'),
            specs=[[{"type": "bar"}, {"type": "scatter"}],
                   [{"type": "pie"}, {"type": "table"}]]
        )
        
        # Distribuição de grau
        degrees = [self.graph.degree(node) for node in self.graph.nodes()]
        degree_counts = Counter(degrees)
        
        fig.add_trace(
            go.Bar(x=list(degree_counts.keys()), y=list(degree_counts.values()), 
                   name='Distribuição de Grau'),
            row=1, col=1
        )
        
        # Centralidade de intermediação vs grau
        if 'betweenness_centrality' in self.graph.nodes[list(self.graph.nodes())[0]]:
            degrees = [self.graph.degree(node) for node in self.graph.nodes()]
            betweenness = [self.graph.nodes[node]['betweenness_centrality'] for node in self.graph.nodes()]
            
            fig.add_trace(
                go.Scatter(x=degrees, y=betweenness, mode='markers',
                          name='Centralidade vs Grau'),
                row=1, col=2
            )
        
        # Tamanho das comunidades
        if 'communities' in self.analysis_results:
            community_sizes = list(self.analysis_results['communities']['sizes'].values())
            community_labels = [f'Comunidade {i+1}' for i in range(len(community_sizes))]
            
            fig.add_trace(
                go.Pie(values=community_sizes, labels=community_labels,
                       name='Comunidades'),
                row=2, col=1
            )
        
        # Tabela de métricas
        metrics_data = [
            ['Nós', self.analysis_results['basic_metrics']['nodes']],
            ['Arestas', self.analysis_results['basic_metrics']['edges']],
            ['Densidade', f"{self.analysis_results['basic_metrics']['density']:.3f}"],
            ['Componentes', self.analysis_results['components']['count']],
            ['Conectado', 'Sim' if self.analysis_results['basic_metrics']['is_connected'] else 'Não']
        ]
        
        if 'communities' in self.analysis_results:
            metrics_data.append(['Comunidades', self.analysis_results['communities']['count']])
        
        fig.add_trace(
            go.Table(
                header=dict(values=['Métrica', 'Valor']),
                cells=dict(values=[[row[0] for row in metrics_data], 
                                  [row[1] for row in metrics_data]])
            ),
            row=2, col=2
        )
        
        fig.update_layout(height=800, showlegend=False, title_text="Dashboard de Métricas da Rede")
        return fig
    
    def export_results(self, filename_prefix='graph_analysis'):
        """Exporta resultados da análise."""
        if self.graph.number_of_nodes() == 0:
            return
        
        # Exportar dados dos nós
        nodes_data = []
        for node in self.graph.nodes():
            node_data = {'node': node}
            node_data.update(self.graph.nodes[node])
            nodes_data.append(node_data)
        
        nodes_df = pd.DataFrame(nodes_data)
        nodes_df.to_csv(f'{filename_prefix}_nodes.csv', index=False)
        
        # Exportar dados das arestas
        edges_data = []
        for edge in self.graph.edges():
            edge_data = {'source': edge[0], 'target': edge[1]}
            edge_data.update(self.graph.edges[edge])
            edges_data.append(edge_data)
        
        edges_df = pd.DataFrame(edges_data)
        edges_df.to_csv(f'{filename_prefix}_edges.csv', index=False)
        
        # Exportar análise
        with open(f'{filename_prefix}_analysis.json', 'w', encoding='utf-8') as f:
            json.dump(self.analysis_results, f, indent=2, ensure_ascii=False, default=str)
        
        print(f"Resultados exportados: {filename_prefix}_nodes.csv, {filename_prefix}_edges.csv, {filename_prefix}_analysis.json")


def main():
    """Função principal para execução standalone."""
    print("=== Ferramenta de Análise de Conexões via Grafo ===\n")
    
    analyzer = GraphAnalyzer()
    
    # Exemplo de uso
    print("Exemplo de uso com dados de teste...")
    
    # Carregar dados de exemplo
    if analyzer.load_csv_data('dados_rede_teste.csv'):
        print("\nCriando grafo...")
        analyzer.create_graph_from_data(
            source_col='Pessoa',
            target_col='Empresa',
            weight_col='Valor',
            directed=False,
            additional_attrs=['Tipo', 'Local', 'Data']
        )
        
        print("\nAnalisando grafo...")
        results = analyzer.analyze_graph()
        
        print(f"\n=== Resultados da Análise ===")
        print(f"Nós: {results['basic_metrics']['nodes']}")
        print(f"Arestas: {results['basic_metrics']['edges']}")
        print(f"Densidade: {results['basic_metrics']['density']:.3f}")
        print(f"Componentes conectados: {results['components']['count']}")
        
        if 'communities' in results:
            print(f"Comunidades detectadas: {results['communities']['count']}")
        
        # Exportar resultados
        analyzer.export_results('exemplo_analise')
        
        print("\n=== Análise concluída ===")
        print("Use a interface web para visualização interativa.")


if __name__ == "__main__":
    main()