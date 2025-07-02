from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class Entity(BaseModel):
    """Entidade extraída do texto (pessoa, empresa, local, etc.)"""
    name: str
    type: str  # PERSON, ORG, GPE, MONEY, DATE, etc.
    confidence: float
    mentions: int
    context: List[str]

class EntityRelationship(BaseModel):
    """Relacionamento entre entidades"""
    source: str
    target: str
    relationship_type: str
    confidence: float
    context: str
    document_source: str

class TimelineEvent(BaseModel):
    """Evento para a linha do tempo"""
    id: str
    date: datetime
    title: str
    description: str
    entities_involved: List[str]
    event_type: str  # transaction, meeting, document, etc.
    location: Optional[str] = None
    amount: Optional[float] = None
    confidence: float
    source_document: str

class DocumentAnalysis(BaseModel):
    """Resultado da análise de um documento"""
    filename: str
    extracted_text: str
    entities: List[Entity]
    events: List[TimelineEvent]
    summary: str
    processing_time: Optional[float] = None

class QueryRequest(BaseModel):
    """Requisição de consulta em linguagem natural"""
    query: str
    context: Optional[Dict[str, Any]] = None

class QueryResponse(BaseModel):
    """Resposta para consulta em linguagem natural"""
    query: str
    response: str
    suggestions: List[str]
    filters_applied: Dict[str, Any]
    results_count: Optional[int] = None

class PatternDetection(BaseModel):
    """Padrão detectado pela IA"""
    pattern_type: str
    description: str
    confidence: float
    entities_involved: List[str]
    frequency: int
    risk_level: str  # low, medium, high, critical
    evidence: List[str]

class AIInsight(BaseModel):
    """Insight gerado pela IA"""
    insight_type: str
    title: str
    description: str
    confidence: float
    impact: str  # low, medium, high
    recommendation: str
    supporting_evidence: List[str]

class InvestigationCase(BaseModel):
    """Caso de investigação"""
    id: str
    title: str
    description: str
    created_at: datetime
    status: str  # active, closed, on_hold
    documents: List[str]
    entities: List[Entity]
    timeline: List[TimelineEvent]
    patterns: List[PatternDetection]
    insights: List[AIInsight]

class NetworkNode(BaseModel):
    """Nó para visualização de rede"""
    id: str
    label: str
    type: str
    size: int
    color: str
    metadata: Dict[str, Any]

class NetworkEdge(BaseModel):
    """Aresta para visualização de rede"""
    source: str
    target: str
    weight: float
    type: str
    label: str

class NetworkGraph(BaseModel):
    """Grafo de relacionamentos"""
    nodes: List[NetworkNode]
    edges: List[NetworkEdge]
    metadata: Dict[str, Any] 