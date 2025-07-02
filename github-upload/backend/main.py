from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os
from typing import List, Optional
import uvicorn

from services.document_processor import DocumentProcessor
from services.entity_extractor import EntityExtractor
from services.timeline_builder import TimelineBuilder
from services.ai_assistant import AIAssistant
from models.schemas import (
    DocumentAnalysis, 
    EntityRelationship, 
    TimelineEvent,
    QueryRequest,
    QueryResponse
)

app = FastAPI(
    title="InvestigIA API",
    description="Plataforma de Análise Investigativa Inteligente",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inicializar serviços
document_processor = DocumentProcessor()
entity_extractor = EntityExtractor()
timeline_builder = TimelineBuilder()
ai_assistant = AIAssistant()

@app.get("/")
async def root():
    return {"message": "InvestigIA API está funcionando!", "version": "1.0.0"}

@app.post("/upload", response_model=DocumentAnalysis)
async def upload_document(file: UploadFile = File(...)):
    """
    Fazer upload e processar documento (PDF, DOCX, TXT, CSV, XLSX, imagens)
    """
    try:
        # Verificar tipo do arquivo
        allowed_types = [
            "application/pdf", "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            "text/plain", "text/csv", "application/vnd.ms-excel",
            "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            "image/png", "image/jpeg", "image/jpg"
        ]
        
        if file.content_type not in allowed_types:
            raise HTTPException(status_code=400, detail="Tipo de arquivo não suportado")
        
        # Salvar arquivo temporariamente
        upload_dir = "uploads"
        os.makedirs(upload_dir, exist_ok=True)
        file_path = os.path.join(upload_dir, file.filename)
        
        with open(file_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)
        
        # Processar documento
        extracted_text = document_processor.process_document(file_path, file.content_type)
        
        # Extrair entidades
        entities = entity_extractor.extract_entities(extracted_text)
        
        # Construir eventos da timeline
        events = timeline_builder.extract_events(extracted_text, entities)
        
        # Limpar arquivo temporário
        os.remove(file_path)
        
        return DocumentAnalysis(
            filename=file.filename,
            extracted_text=extracted_text,
            entities=entities,
            events=events,
            summary=f"Processado {len(entities)} entidades e {len(events)} eventos"
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar documento: {str(e)}")

@app.get("/timeline", response_model=List[TimelineEvent])
async def get_timeline(
    start_date: Optional[str] = None,
    end_date: Optional[str] = None,
    entity_filter: Optional[str] = None
):
    """
    Obter eventos da linha do tempo com filtros opcionais
    """
    try:
        events = timeline_builder.get_filtered_timeline(
            start_date=start_date,
            end_date=end_date,
            entity_filter=entity_filter
        )
        return events
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao obter timeline: {str(e)}")

@app.get("/entities", response_model=List[EntityRelationship])
async def get_entity_relationships():
    """
    Obter mapa de relacionamentos entre entidades
    """
    try:
        relationships = entity_extractor.get_relationships()
        return relationships
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao obter relacionamentos: {str(e)}")

@app.post("/query", response_model=QueryResponse)
async def natural_language_query(request: QueryRequest):
    """
    Processar consulta em linguagem natural
    """
    try:
        response = await ai_assistant.process_query(request.query)
        return QueryResponse(
            query=request.query,
            response=response["answer"],
            suggestions=response.get("suggestions", []),
            filters_applied=response.get("filters", {})
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao processar consulta: {str(e)}")

@app.get("/patterns")
async def detect_patterns():
    """
    Detectar padrões suspeitos e anomalias
    """
    try:
        patterns = await ai_assistant.detect_patterns()
        return {"patterns": patterns}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao detectar padrões: {str(e)}")

@app.get("/insights")
async def get_ai_insights():
    """
    Obter insights gerados pela IA
    """
    try:
        insights = await ai_assistant.generate_insights()
        return {"insights": insights}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao gerar insights: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 