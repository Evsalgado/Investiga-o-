import json
import re
from typing import List, Dict, Any, Optional
from collections import defaultdict, Counter
import logging

# Para usar LLM local ou APIs
try:
    import openai
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

from models.schemas import PatternDetection, AIInsight

logger = logging.getLogger(__name__)

class AIAssistant:
    """Assistente de IA para análise investigativa"""
    
    def __init__(self):
        self.patterns_db = []
        self.insights_db = []
        
        # Configurar OpenAI se disponível
        if OPENAI_AVAILABLE:
            # openai.api_key = os.getenv("OPENAI_API_KEY")  # Configurar se necessário
            pass
        
        # Palavras-chave para diferentes tipos de análise
        self.fraud_keywords = [
            'suspeito', 'irregular', 'fraude', 'lavagem', 'fantasma',
            'fachada', 'laranja', 'esquema', 'desvio', 'superfaturamento'
        ]
        
        self.risk_keywords = [
            'dinheiro vivo', 'cash', 'offshore', 'paraíso fiscal',
            'conta fantasma', 'transferência internacional', 'criptomoeda'
        ]

    async def process_query(self, query: str) -> Dict[str, Any]:
        """
        Processa consulta em linguagem natural
        """
        logger.info(f"Processando consulta: {query}")
        
        # Análise básica da consulta
        query_analysis = self._analyze_query(query)
        
        # Gerar resposta baseada na análise
        if query_analysis['type'] == 'filter':
            response = await self._process_filter_query(query, query_analysis)
        elif query_analysis['type'] == 'search':
            response = await self._process_search_query(query, query_analysis)
        elif query_analysis['type'] == 'analysis':
            response = await self._process_analysis_query(query, query_analysis)
        else:
            response = await self._process_general_query(query)
        
        return response

    def _analyze_query(self, query: str) -> Dict[str, Any]:
        """Analisa o tipo e intenção da consulta"""
        query_lower = query.lower()
        
        # Detectar tipo de consulta
        if any(word in query_lower for word in ['filtrar', 'mostrar', 'listar']):
            query_type = 'filter'
        elif any(word in query_lower for word in ['buscar', 'encontrar', 'procurar']):
            query_type = 'search'
        elif any(word in query_lower for word in ['analisar', 'padrão', 'suspeito', 'anomalia']):
            query_type = 'analysis'
        else:
            query_type = 'general'
        
        # Extrair entidades mencionadas
        entities = self._extract_entities_from_query(query)
        
        # Extrair datas
        dates = self._extract_dates_from_query(query)
        
        # Extrair tipos de evento
        event_types = self._extract_event_types_from_query(query)
        
        return {
            'type': query_type,
            'entities': entities,
            'dates': dates,
            'event_types': event_types,
            'original': query
        }

    def _extract_entities_from_query(self, query: str) -> List[str]:
        """Extrai nomes de entidades da consulta"""
        # Padrão simples para nomes próprios
        entities = re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b', query)
        return entities

    def _extract_dates_from_query(self, query: str) -> List[str]:
        """Extrai datas da consulta"""
        date_patterns = [
            r'\d{1,2}/\d{1,2}/\d{4}',
            r'\d{1,2}-\d{1,2}-\d{4}',
            r'\w+\s+de\s+\d{4}',
            r'\d{4}'
        ]
        
        dates = []
        for pattern in date_patterns:
            matches = re.findall(pattern, query)
            dates.extend(matches)
        
        return dates

    def _extract_event_types_from_query(self, query: str) -> List[str]:
        """Extrai tipos de evento da consulta"""
        event_mapping = {
            'transferência': 'TRANSFER',
            'pagamento': 'PAYMENT',
            'depósito': 'DEPOSIT',
            'saque': 'WITHDRAWAL',
            'reunião': 'MEETING',
            'contrato': 'CONTRACT',
            'transação': 'TRANSACTION'
        }
        
        query_lower = query.lower()
        found_types = []
        
        for keyword, event_type in event_mapping.items():
            if keyword in query_lower:
                found_types.append(event_type)
        
        return found_types

    async def _process_filter_query(self, query: str, analysis: Dict) -> Dict[str, Any]:
        """Processa consultas de filtro"""
        filters = {}
        
        if analysis['entities']:
            filters['entities'] = analysis['entities']
        
        if analysis['dates']:
            filters['dates'] = analysis['dates']
        
        if analysis['event_types']:
            filters['event_types'] = analysis['event_types']
        
        # Detectar filtros de valor
        amount_match = re.search(r'acima\s+de\s+(?:R\$\s*)?(\d+)', query, re.IGNORECASE)
        if amount_match:
            filters['min_amount'] = float(amount_match.group(1))
        
        response_text = f"Aplicando filtros baseados na consulta: {query}"
        if filters:
            response_text += f"\nFiltros detectados: {', '.join(filters.keys())}"
        
        return {
            'answer': response_text,
            'filters': filters,
            'suggestions': [
                "Refinar filtros por período específico",
                "Adicionar filtro por valor mínimo",
                "Filtrar por tipo de relacionamento"
            ]
        }

    async def _process_search_query(self, query: str, analysis: Dict) -> Dict[str, Any]:
        """Processa consultas de busca"""
        search_terms = analysis['entities'] + analysis['event_types']
        
        response_text = f"Buscando por: {', '.join(search_terms) if search_terms else 'termos da consulta'}"
        
        return {
            'answer': response_text,
            'filters': {'search_terms': search_terms},
            'suggestions': [
                "Expandir busca para entidades relacionadas",
                "Buscar em período específico",
                "Incluir sinônimos na busca"
            ]
        }

    async def _process_analysis_query(self, query: str, analysis: Dict) -> Dict[str, Any]:
        """Processa consultas de análise"""
        response_text = "Iniciando análise investigativa..."
        
        # Detectar tipo de análise solicitada
        if 'suspeito' in query.lower():
            response_text += "\nDetectando atividades suspeitas..."
        elif 'padrão' in query.lower():
            response_text += "\nIdentificando padrões comportamentais..."
        elif 'relacionamento' in query.lower():
            response_text += "\nMapeando relacionamentos entre entidades..."
        
        return {
            'answer': response_text,
            'filters': {},
            'suggestions': [
                "Analisar frequência de transações",
                "Detectar valores atípicos",
                "Mapear rede de relacionamentos"
            ]
        }

    async def _process_general_query(self, query: str) -> Dict[str, Any]:
        """Processa consultas gerais"""
        # Resposta padrão para consultas não categorizadas
        return {
            'answer': f"Processando sua solicitação: {query}. Como posso ajudar especificamente?",
            'filters': {},
            'suggestions': [
                "Seja mais específico sobre o que deseja filtrar",
                "Mencione nomes de pessoas ou empresas",
                "Especifique um período de tempo"
            ]
        }

    async def detect_patterns(self) -> List[PatternDetection]:
        """Detecta padrões suspeitos nos dados"""
        patterns = []
        
        # Simular detecção de padrões
        # Em implementação real, isso analisaria os dados reais
        sample_patterns = [
            {
                'pattern_type': 'FREQUENT_TRANSFERS',
                'description': 'Transferências frequentes entre as mesmas entidades',
                'confidence': 0.85,
                'entities_involved': ['João Silva', 'Empresa XYZ'],
                'frequency': 12,
                'risk_level': 'high',
                'evidence': [
                    'Transferências semanais de valores similares',
                    'Horários consistentes das transações',
                    'Ausência de justificativa comercial aparente'
                ]
            },
            {
                'pattern_type': 'UNUSUAL_AMOUNTS',
                'description': 'Valores atípicos em transações',
                'confidence': 0.75,
                'entities_involved': ['Maria Santos'],
                'frequency': 3,
                'risk_level': 'medium',
                'evidence': [
                    'Transações 300% acima da média',
                    'Valores quebrados (ex: R$ 9.987,43)',
                    'Concentração em final de mês'
                ]
            }
        ]
        
        for pattern_data in sample_patterns:
            pattern = PatternDetection(**pattern_data)
            patterns.append(pattern)
            self.patterns_db.append(pattern)
        
        return patterns

    async def generate_insights(self) -> List[AIInsight]:
        """Gera insights baseados na análise dos dados"""
        insights = []
        
        # Simular geração de insights
        sample_insights = [
            {
                'insight_type': 'RISK_ASSESSMENT',
                'title': 'Rede de transações suspeitas identificada',
                'description': 'Detectada rede de 5 entidades com padrão de transações circulares',
                'confidence': 0.9,
                'impact': 'high',
                'recommendation': 'Investigar relacionamentos entre as entidades e origem dos recursos',
                'supporting_evidence': [
                    'Transações em valores redondos',
                    'Timing coordenado das operações',
                    'Ausência de atividade comercial legítima'
                ]
            },
            {
                'insight_type': 'TEMPORAL_ANOMALY',
                'title': 'Atividade concentrada em períodos específicos',
                'description': 'Movimentações financeiras concentradas em finais de semana',
                'confidence': 0.75,
                'impact': 'medium',
                'recommendation': 'Analisar justificativa para operações fora do horário comercial',
                'supporting_evidence': [
                    '80% das transações em sábados e domingos',
                    'Valores consistentemente altos',
                    'Múltiplas entidades envolvidas'
                ]
            }
        ]
        
        for insight_data in sample_insights:
            insight = AIInsight(**insight_data)
            insights.append(insight)
            self.insights_db.append(insight)
        
        return insights

    def analyze_text_sentiment(self, text: str) -> Dict[str, Any]:
        """Analisa sentimento e tom do texto"""
        # Análise básica de sentimento
        positive_words = ['acordo', 'sucesso', 'positivo', 'benefício', 'ganho']
        negative_words = ['problema', 'erro', 'falha', 'prejuízo', 'suspeito']
        fraud_words = ['fraude', 'esquema', 'ilegal', 'irregular', 'lavagem']
        
        text_lower = text.lower()
        
        positive_count = sum(1 for word in positive_words if word in text_lower)
        negative_count = sum(1 for word in negative_words if word in text_lower)
        fraud_count = sum(1 for word in fraud_words if word in text_lower)
        
        # Calcular score
        total_words = len(text.split())
        sentiment_score = (positive_count - negative_count) / max(total_words, 1)
        fraud_risk = fraud_count / max(total_words, 1)
        
        return {
            'sentiment_score': sentiment_score,
            'sentiment': 'positive' if sentiment_score > 0.1 else 'negative' if sentiment_score < -0.1 else 'neutral',
            'fraud_risk_score': fraud_risk,
            'fraud_indicators': fraud_count,
            'key_terms': {
                'positive': [word for word in positive_words if word in text_lower],
                'negative': [word for word in negative_words if word in text_lower],
                'fraud': [word for word in fraud_words if word in text_lower]
            }
        }

    def suggest_investigation_steps(self, entities: List[str], patterns: List[Dict]) -> List[str]:
        """Sugere próximos passos na investigação"""
        suggestions = []
        
        # Sugestões baseadas em entidades
        if len(entities) > 5:
            suggestions.append("Criar mapa de relacionamentos para visualizar conexões")
        
        if any('ORG' in str(entity) for entity in entities):
            suggestions.append("Verificar registros oficiais das empresas mencionadas")
        
        # Sugestões baseadas em padrões
        if patterns:
            suggestions.append("Aprofundar análise dos padrões detectados")
            
            if any(p.get('risk_level') == 'high' for p in patterns):
                suggestions.append("Priorizar investigação de padrões de alto risco")
        
        # Sugestões gerais
        suggestions.extend([
            "Buscar documentos adicionais do mesmo período",
            "Investigar entidades com maior número de conexões",
            "Analisar cronologia de eventos para identificar sequências suspeitas",
            "Cruzar dados com bases públicas de informações"
        ])
        
        return suggestions[:5]  # Limitar a 5 sugestões

    def get_investigation_summary(self) -> Dict[str, Any]:
        """Gera resumo da investigação atual"""
        return {
            'patterns_detected': len(self.patterns_db),
            'insights_generated': len(self.insights_db),
            'high_risk_patterns': len([p for p in self.patterns_db if p.risk_level == 'high']),
            'recommendations': [
                "Continuar coleta de evidências",
                "Mapear relacionamentos completos",
                "Verificar conformidade regulatória"
            ]
        } 