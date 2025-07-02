import re
import uuid
from datetime import datetime, timedelta
from typing import List, Optional, Dict, Any
from collections import defaultdict
import logging

from models.schemas import TimelineEvent, Entity

logger = logging.getLogger(__name__)

class TimelineBuilder:
    """Constrói e gerencia linha do tempo de eventos"""
    
    def __init__(self):
        self.events_db = []
        self.date_patterns = [
            r'\d{1,2}[\/\-\.]\d{1,2}[\/\-\.]\d{4}',  # DD/MM/YYYY
            r'\d{1,2}[\/\-\.]\d{1,2}[\/\-\.]\d{2}',   # DD/MM/YY
            r'\d{4}[\/\-\.]\d{1,2}[\/\-\.]\d{1,2}',   # YYYY/MM/DD
            r'\d{1,2}\s+de\s+\w+\s+de\s+\d{4}',      # DD de MMMM de YYYY
            r'\w+\s+\d{1,2},?\s+\d{4}',               # MMMM DD, YYYY
        ]
        
        # Palavras-chave que indicam eventos
        self.event_keywords = {
            'transferencia': 'TRANSFER',
            'pagamento': 'PAYMENT',
            'deposito': 'DEPOSIT',
            'saque': 'WITHDRAWAL',
            'reuniao': 'MEETING',
            'contrato': 'CONTRACT',
            'acordo': 'AGREEMENT',
            'compra': 'PURCHASE',
            'venda': 'SALE',
            'investimento': 'INVESTMENT',
            'emprestimo': 'LOAN',
            'financiamento': 'FINANCING'
        }

    def extract_events(self, text: str, entities: List[Entity]) -> List[TimelineEvent]:
        """
        Extrai eventos do texto baseado em datas e entidades
        """
        events = []
        
        # Encontrar todas as datas no texto
        dates_found = self._extract_dates(text)
        
        # Dividir texto em sentenças
        sentences = self._split_into_sentences(text)
        
        for sentence in sentences:
            # Verificar se a sentença contém uma data
            sentence_dates = []
            for date_info in dates_found:
                if date_info['text'] in sentence:
                    sentence_dates.append(date_info)
            
            if sentence_dates:
                # Extrair evento da sentença
                event = self._extract_event_from_sentence(sentence, sentence_dates, entities)
                if event:
                    events.append(event)
                    self.events_db.append(event)
        
        return sorted(events, key=lambda x: x.date)

    def _extract_dates(self, text: str) -> List[Dict[str, Any]]:
        """Extrai datas do texto"""
        dates_found = []
        
        for pattern in self.date_patterns:
            matches = re.finditer(pattern, text, re.IGNORECASE)
            
            for match in matches:
                date_text = match.group().strip()
                parsed_date = self._parse_date(date_text)
                
                if parsed_date:
                    dates_found.append({
                        'text': date_text,
                        'date': parsed_date,
                        'start': match.start(),
                        'end': match.end()
                    })
        
        return dates_found

    def _parse_date(self, date_text: str) -> Optional[datetime]:
        """Converte texto de data em objeto datetime"""
        try:
            # Tentar diferentes formatos
            formats = [
                "%d/%m/%Y", "%d-%m-%Y", "%d.%m.%Y",
                "%d/%m/%y", "%d-%m-%y", "%d.%m.%y",
                "%Y/%m/%d", "%Y-%m-%d", "%Y.%m.%d",
                "%d de %B de %Y", "%d de %b de %Y"
            ]
            
            # Substituir nomes de meses em português
            date_text = date_text.lower()
            month_replacements = {
                'janeiro': 'january', 'fevereiro': 'february', 'março': 'march',
                'abril': 'april', 'maio': 'may', 'junho': 'june',
                'julho': 'july', 'agosto': 'august', 'setembro': 'september',
                'outubro': 'october', 'novembro': 'november', 'dezembro': 'december',
                'jan': 'jan', 'fev': 'feb', 'mar': 'mar', 'abr': 'apr',
                'mai': 'may', 'jun': 'jun', 'jul': 'jul', 'ago': 'aug',
                'set': 'sep', 'out': 'oct', 'nov': 'nov', 'dez': 'dec'
            }
            
            for pt_month, en_month in month_replacements.items():
                date_text = date_text.replace(pt_month, en_month)
            
            for fmt in formats:
                try:
                    return datetime.strptime(date_text, fmt)
                except ValueError:
                    continue
                    
        except Exception as e:
            logger.warning(f"Erro ao processar data '{date_text}': {e}")
            
        return None

    def _split_into_sentences(self, text: str) -> List[str]:
        """Divide texto em sentenças"""
        # Divisão simples por pontos, quebras de linha, etc.
        sentences = re.split(r'[.!?;]\s+|\n\s*\n', text)
        return [s.strip() for s in sentences if len(s.strip()) > 10]

    def _extract_event_from_sentence(self, sentence: str, sentence_dates: List[Dict], entities: List[Entity]) -> Optional[TimelineEvent]:
        """Extrai evento de uma sentença"""
        
        # Verificar se a sentença contém palavras-chave de evento
        event_type = 'UNKNOWN'
        for keyword, etype in self.event_keywords.items():
            if keyword in sentence.lower():
                event_type = etype
                break
        
        # Encontrar entidades na sentença
        entities_involved = []
        for entity in entities:
            if entity.name.lower() in sentence.lower():
                entities_involved.append(entity.name)
        
        # Extrair valor monetário se houver
        amount = self._extract_amount(sentence)
        
        # Extrair local se houver
        location = self._extract_location(sentence)
        
        # Se não há entidades ou data, não é um evento válido
        if not entities_involved or not sentence_dates:
            return None
        
        # Usar a primeira data encontrada
        event_date = sentence_dates[0]['date']
        
        # Criar evento
        event = TimelineEvent(
            id=str(uuid.uuid4()),
            date=event_date,
            title=self._generate_event_title(event_type, entities_involved),
            description=sentence[:200] + "..." if len(sentence) > 200 else sentence,
            entities_involved=entities_involved,
            event_type=event_type,
            location=location,
            amount=amount,
            confidence=0.8,
            source_document="current_document"
        )
        
        return event

    def _extract_amount(self, text: str) -> Optional[float]:
        """Extrai valor monetário do texto"""
        # Padrão para valores em reais
        pattern = r'R\$\s*(\d{1,3}(?:\.\d{3})*(?:,\d{2})?)'
        matches = re.findall(pattern, text)
        
        if matches:
            try:
                # Converter para float (substituir vírgula por ponto e remover pontos de milhares)
                amount_str = matches[0].replace('.', '').replace(',', '.')
                return float(amount_str)
            except ValueError:
                pass
        
        return None

    def _extract_location(self, text: str) -> Optional[str]:
        """Extrai localização do texto"""
        # Padrões simples para localização
        location_patterns = [
            r'em\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)',
            r'na\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)',
            r'no\s+([A-Z][a-z]+(?:\s+[A-Z][a-z]+)*)'
        ]
        
        for pattern in location_patterns:
            matches = re.findall(pattern, text)
            if matches:
                return matches[0]
        
        return None

    def _generate_event_title(self, event_type: str, entities: List[str]) -> str:
        """Gera título para o evento"""
        if event_type == 'TRANSFER':
            return f"Transferência envolvendo {', '.join(entities[:2])}"
        elif event_type == 'PAYMENT':
            return f"Pagamento entre {', '.join(entities[:2])}"
        elif event_type == 'MEETING':
            return f"Reunião com {', '.join(entities[:3])}"
        elif event_type == 'CONTRACT':
            return f"Contrato com {', '.join(entities[:2])}"
        else:
            return f"Evento {event_type.lower()} - {', '.join(entities[:2])}"

    def get_filtered_timeline(self, start_date: Optional[str] = None, 
                            end_date: Optional[str] = None,
                            entity_filter: Optional[str] = None) -> List[TimelineEvent]:
        """
        Retorna timeline filtrada
        """
        filtered_events = self.events_db.copy()
        
        # Filtrar por data de início
        if start_date:
            try:
                start_dt = datetime.fromisoformat(start_date.replace('Z', '+00:00'))
                filtered_events = [e for e in filtered_events if e.date >= start_dt]
            except ValueError:
                logger.warning(f"Data de início inválida: {start_date}")
        
        # Filtrar por data de fim
        if end_date:
            try:
                end_dt = datetime.fromisoformat(end_date.replace('Z', '+00:00'))
                filtered_events = [e for e in filtered_events if e.date <= end_dt]
            except ValueError:
                logger.warning(f"Data de fim inválida: {end_date}")
        
        # Filtrar por entidade
        if entity_filter:
            filtered_events = [
                e for e in filtered_events 
                if any(entity_filter.lower() in entity.lower() for entity in e.entities_involved)
            ]
        
        return sorted(filtered_events, key=lambda x: x.date)

    def get_timeline_statistics(self) -> Dict[str, Any]:
        """Retorna estatísticas da timeline"""
        if not self.events_db:
            return {}
        
        # Contar eventos por tipo
        event_types = defaultdict(int)
        for event in self.events_db:
            event_types[event.event_type] += 1
        
        # Contar eventos por mês
        events_by_month = defaultdict(int)
        for event in self.events_db:
            month_key = event.date.strftime('%Y-%m')
            events_by_month[month_key] += 1
        
        # Calcular período
        dates = [e.date for e in self.events_db]
        min_date = min(dates)
        max_date = max(dates)
        
        return {
            'total_events': len(self.events_db),
            'event_types': dict(event_types),
            'events_by_month': dict(events_by_month),
            'date_range': {
                'start': min_date.isoformat(),
                'end': max_date.isoformat(),
                'duration_days': (max_date - min_date).days
            }
        }

    def detect_timeline_patterns(self) -> List[Dict[str, Any]]:
        """Detecta padrões na timeline"""
        patterns = []
        
        if len(self.events_db) < 3:
            return patterns
        
        # Detectar eventos recorrentes
        recurring_events = self._detect_recurring_events()
        if recurring_events:
            patterns.extend(recurring_events)
        
        # Detectar clusters temporais
        temporal_clusters = self._detect_temporal_clusters()
        if temporal_clusters:
            patterns.extend(temporal_clusters)
        
        return patterns

    def _detect_recurring_events(self) -> List[Dict[str, Any]]:
        """Detecta eventos que se repetem"""
        patterns = []
        
        # Agrupar por tipo de evento e entidades
        event_groups = defaultdict(list)
        for event in self.events_db:
            key = (event.event_type, tuple(sorted(event.entities_involved)))
            event_groups[key].append(event)
        
        for (event_type, entities), events in event_groups.items():
            if len(events) >= 3:  # Pelo menos 3 ocorrências
                patterns.append({
                    'type': 'RECURRING_EVENT',
                    'description': f"Evento recorrente: {event_type} com {', '.join(entities)}",
                    'frequency': len(events),
                    'dates': [e.date.isoformat() for e in events],
                    'risk_level': 'medium' if len(events) >= 5 else 'low'
                })
        
        return patterns

    def _detect_temporal_clusters(self) -> List[Dict[str, Any]]:
        """Detecta clusters de eventos em períodos próximos"""
        patterns = []
        
        # Ordenar eventos por data
        sorted_events = sorted(self.events_db, key=lambda x: x.date)
        
        # Detectar clusters (eventos próximos no tempo)
        clusters = []
        current_cluster = [sorted_events[0]]
        
        for i in range(1, len(sorted_events)):
            current_event = sorted_events[i]
            last_event = current_cluster[-1]
            
            # Se eventos estão próximos (menos de 7 dias)
            if (current_event.date - last_event.date).days <= 7:
                current_cluster.append(current_event)
            else:
                if len(current_cluster) >= 3:
                    clusters.append(current_cluster)
                current_cluster = [current_event]
        
        # Adicionar último cluster se válido
        if len(current_cluster) >= 3:
            clusters.append(current_cluster)
        
        # Converter clusters em padrões
        for cluster in clusters:
            patterns.append({
                'type': 'TEMPORAL_CLUSTER',
                'description': f"Cluster de {len(cluster)} eventos em período de {(cluster[-1].date - cluster[0].date).days} dias",
                'event_count': len(cluster),
                'start_date': cluster[0].date.isoformat(),
                'end_date': cluster[-1].date.isoformat(),
                'events': [e.title for e in cluster],
                'risk_level': 'high' if len(cluster) >= 5 else 'medium'
            })
        
        return patterns 