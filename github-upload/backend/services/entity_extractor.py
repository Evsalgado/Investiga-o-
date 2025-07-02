import spacy
import re
from typing import List, Dict, Tuple
from collections import defaultdict, Counter
import logging

from models.schemas import Entity, EntityRelationship

logger = logging.getLogger(__name__)

class EntityExtractor:
    """Extrai entidades nomeadas e relacionamentos do texto"""
    
    def __init__(self):
        try:
            # Carregar modelo em português
            self.nlp = spacy.load("pt_core_news_sm")
        except OSError:
            logger.warning("Modelo pt_core_news_sm não encontrado, usando modelo em inglês")
            try:
                self.nlp = spacy.load("en_core_web_sm")
            except OSError:
                logger.error("Nenhum modelo spaCy encontrado. Instale com: python -m spacy download pt_core_news_sm")
                raise
        
        # Padrões específicos para investigação
        self.patterns = {
            'cpf': r'\d{3}\.?\d{3}\.?\d{3}-?\d{2}',
            'cnpj': r'\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}',
            'conta_bancaria': r'\d{4,6}-?\d{1,2}',
            'valor_monetario': r'R\$?\s*\d{1,3}(?:\.\d{3})*(?:,\d{2})?',
            'data': r'\d{1,2}[\/\-\.]\d{1,2}[\/\-\.]\d{2,4}',
            'email': r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
            'telefone': r'(?:\+55\s?)?(?:\(\d{2}\)\s?)?(?:9\s?)?\d{4,5}-?\d{4}'
        }
        
        # Armazenar entidades e relacionamentos
        self.entities_db = {}
        self.relationships_db = []

    def extract_entities(self, text: str) -> List[Entity]:
        """
        Extrai entidades nomeadas do texto
        """
        entities = []
        
        # Processamento com spaCy
        doc = self.nlp(text)
        
        # Contadores para entidades
        entity_counts = Counter()
        entity_contexts = defaultdict(list)
        
        # Extrair entidades nomeadas
        for ent in doc.ents:
            entity_name = ent.text.strip()
            entity_type = ent.label_
            
            # Filtrar entidades muito pequenas ou irrelevantes
            if len(entity_name) < 2:
                continue
                
            entity_counts[entity_name] += 1
            context = ent.sent.text[:200] + "..." if len(ent.sent.text) > 200 else ent.sent.text
            entity_contexts[entity_name].append(context)
        
        # Extrair padrões específicos
        self._extract_patterns(text, entity_counts, entity_contexts)
        
        # Criar objetos Entity
        for entity_name, count in entity_counts.items():
            entity_type = self._classify_entity_type(entity_name)
            confidence = min(0.9, 0.3 + (count * 0.1))  # Confiança baseada na frequência
            
            entity = Entity(
                name=entity_name,
                type=entity_type,
                confidence=confidence,
                mentions=count,
                context=entity_contexts[entity_name][:3]  # Máximo 3 contextos
            )
            entities.append(entity)
            
            # Armazenar no banco interno
            self.entities_db[entity_name] = entity
        
        return sorted(entities, key=lambda x: x.mentions, reverse=True)

    def _extract_patterns(self, text: str, entity_counts: Counter, entity_contexts: defaultdict):
        """Extrai padrões específicos usando regex"""
        
        for pattern_name, pattern in self.patterns.items():
            matches = re.finditer(pattern, text, re.IGNORECASE)
            
            for match in matches:
                entity_name = match.group().strip()
                entity_counts[entity_name] += 1
                
                # Contexto ao redor do match
                start = max(0, match.start() - 50)
                end = min(len(text), match.end() + 50)
                context = text[start:end]
                entity_contexts[entity_name].append(context)

    def _classify_entity_type(self, entity_name: str) -> str:
        """Classifica o tipo da entidade"""
        
        # Verificar padrões específicos
        if re.match(self.patterns['cpf'], entity_name):
            return 'CPF'
        elif re.match(self.patterns['cnpj'], entity_name):
            return 'CNPJ'
        elif re.match(self.patterns['conta_bancaria'], entity_name):
            return 'CONTA_BANCARIA'
        elif re.match(self.patterns['valor_monetario'], entity_name):
            return 'MONEY'
        elif re.match(self.patterns['data'], entity_name):
            return 'DATE'
        elif re.match(self.patterns['email'], entity_name):
            return 'EMAIL'
        elif re.match(self.patterns['telefone'], entity_name):
            return 'PHONE'
        elif entity_name.isupper() and len(entity_name) > 3:
            return 'ORG'  # Provavelmente empresa
        elif any(title in entity_name.lower() for title in ['ltda', 'sa', 'mei', 'eireli']):
            return 'ORG'
        else:
            return 'PERSON'  # Default para pessoa

    def extract_relationships(self, text: str, entities: List[Entity]) -> List[EntityRelationship]:
        """
        Extrai relacionamentos entre entidades
        """
        relationships = []
        doc = self.nlp(text)
        
        # Palavras-chave que indicam relacionamentos
        relationship_keywords = {
            'transferiu': 'TRANSFER',
            'pagou': 'PAYMENT',
            'recebeu': 'RECEIVED',
            'enviou': 'SENT',
            'trabalha': 'WORKS_FOR',
            'diretor': 'DIRECTOR_OF',
            'sócio': 'PARTNER_OF',
            'proprietário': 'OWNS',
            'contratou': 'HIRED',
            'vendeu': 'SOLD_TO',
            'comprou': 'BOUGHT_FROM'
        }
        
        entity_names = [ent.name for ent in entities]
        
        for sent in doc.sents:
            sent_text = sent.text.lower()
            
            # Encontrar entidades na sentença
            entities_in_sent = []
            for entity_name in entity_names:
                if entity_name.lower() in sent_text:
                    entities_in_sent.append(entity_name)
            
            # Se há pelo menos 2 entidades na sentença
            if len(entities_in_sent) >= 2:
                # Procurar palavras-chave de relacionamento
                for keyword, rel_type in relationship_keywords.items():
                    if keyword in sent_text:
                        # Criar relacionamento entre as entidades
                        for i in range(len(entities_in_sent)):
                            for j in range(i + 1, len(entities_in_sent)):
                                relationship = EntityRelationship(
                                    source=entities_in_sent[i],
                                    target=entities_in_sent[j],
                                    relationship_type=rel_type,
                                    confidence=0.7,
                                    context=sent.text,
                                    document_source="current_document"
                                )
                                relationships.append(relationship)
        
        self.relationships_db.extend(relationships)
        return relationships

    def get_relationships(self) -> List[EntityRelationship]:
        """Retorna todos os relacionamentos armazenados"""
        return self.relationships_db

    def get_entity_network(self) -> Dict:
        """
        Constrói um grafo de relacionamentos entre entidades
        """
        nodes = []
        edges = []
        
        # Criar nós
        for entity_name, entity in self.entities_db.items():
            nodes.append({
                'id': entity_name,
                'label': entity_name,
                'type': entity.type,
                'size': entity.mentions * 10,
                'color': self._get_entity_color(entity.type)
            })
        
        # Criar arestas
        for rel in self.relationships_db:
            edges.append({
                'source': rel.source,
                'target': rel.target,
                'weight': rel.confidence,
                'type': rel.relationship_type,
                'label': rel.relationship_type
            })
        
        return {
            'nodes': nodes,
            'edges': edges
        }

    def _get_entity_color(self, entity_type: str) -> str:
        """Retorna cor baseada no tipo de entidade"""
        colors = {
            'PERSON': '#FF6B6B',
            'ORG': '#4ECDC4',
            'MONEY': '#45B7D1',
            'DATE': '#96CEB4',
            'CPF': '#FFEAA7',
            'CNPJ': '#DDA0DD',
            'EMAIL': '#98D8C8',
            'PHONE': '#F7DC6F'
        }
        return colors.get(entity_type, '#95A5A6')

    def find_entity_clusters(self) -> List[Dict]:
        """
        Agrupa entidades relacionadas em clusters
        """
        clusters = []
        
        # Agrupar por tipo de relacionamento
        rel_groups = defaultdict(list)
        for rel in self.relationships_db:
            rel_groups[rel.relationship_type].append(rel)
        
        for rel_type, relationships in rel_groups.items():
            if len(relationships) >= 3:  # Cluster mínimo de 3 relacionamentos
                entities_in_cluster = set()
                for rel in relationships:
                    entities_in_cluster.add(rel.source)
                    entities_in_cluster.add(rel.target)
                
                clusters.append({
                    'type': rel_type,
                    'entities': list(entities_in_cluster),
                    'relationships_count': len(relationships),
                    'description': f"Cluster de {len(entities_in_cluster)} entidades com relacionamento {rel_type}"
                })
        
        return clusters 