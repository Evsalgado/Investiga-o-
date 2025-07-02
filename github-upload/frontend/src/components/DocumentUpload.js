import React, { useState } from 'react';
import {
  Paper,
  Typography,
  Box,
  Button,
  LinearProgress,
  Alert,
  Chip,
  Stack,
  Grid,
  Card,
  CardContent,
  List,
  ListItem,
  ListItemText,
  ListItemIcon
} from '@mui/material';
import {
  CloudUpload as UploadIcon,
  Description as FileIcon,
  CheckCircle as SuccessIcon,
  Error as ErrorIcon
} from '@mui/icons-material';
import { useDropzone } from 'react-dropzone';
import axios from 'axios';

function DocumentUpload({ onDocumentProcessed }) {
  const [uploading, setUploading] = useState(false);
  const [uploadProgress, setUploadProgress] = useState(0);
  const [uploadedFiles, setUploadedFiles] = useState([]);
  const [error, setError] = useState(null);

  const onDrop = async (acceptedFiles) => {
    setError(null);
    
    for (const file of acceptedFiles) {
      await uploadFile(file);
    }
  };

  const uploadFile = async (file) => {
    setUploading(true);
    setUploadProgress(0);

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://localhost:8000/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
        onUploadProgress: (progressEvent) => {
          const percentCompleted = Math.round(
            (progressEvent.loaded * 100) / progressEvent.total
          );
          setUploadProgress(percentCompleted);
        },
      });

      const documentData = response.data;
      setUploadedFiles(prev => [...prev, {
        name: file.name,
        size: file.size,
        type: file.type,
        status: 'success',
        data: documentData
      }]);

      // Notificar componente pai
      if (onDocumentProcessed) {
        onDocumentProcessed(documentData);
      }

    } catch (error) {
      console.error('Erro ao fazer upload:', error);
      setError(`Erro ao processar ${file.name}: ${error.response?.data?.detail || error.message}`);
      
      setUploadedFiles(prev => [...prev, {
        name: file.name,
        size: file.size,
        type: file.type,
        status: 'error',
        error: error.response?.data?.detail || error.message
      }]);
    } finally {
      setUploading(false);
      setUploadProgress(0);
    }
  };

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      'application/pdf': ['.pdf'],
      'application/vnd.openxmlformats-officedocument.wordprocessingml.document': ['.docx'],
      'text/plain': ['.txt'],
      'text/csv': ['.csv'],
      'application/vnd.ms-excel': ['.xls'],
      'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet': ['.xlsx'],
      'image/png': ['.png'],
      'image/jpeg': ['.jpg', '.jpeg']
    },
    maxSize: 50 * 1024 * 1024, // 50MB
    disabled: uploading
  });

  const formatFileSize = (bytes) => {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
  };

  return (
    <Grid container spacing={3}>
      <Grid item xs={12} md={6}>
        <Paper sx={{ p: 3 }}>
          <Typography variant="h6" gutterBottom>
            📤 Upload de Documentos
          </Typography>
          
          <Box
            {...getRootProps()}
            sx={{
              border: '2px dashed',
              borderColor: isDragActive ? 'primary.main' : 'grey.300',
              borderRadius: 2,
              p: 4,
              textAlign: 'center',
              cursor: uploading ? 'not-allowed' : 'pointer',
              backgroundColor: isDragActive ? 'action.hover' : 'background.paper',
              '&:hover': {
                borderColor: 'primary.main',
                backgroundColor: 'action.hover'
              }
            }}
          >
            <input {...getInputProps()} />
            <UploadIcon sx={{ fontSize: 48, color: 'grey.400', mb: 2 }} />
            
            {isDragActive ? (
              <Typography variant="body1">
                Solte os arquivos aqui...
              </Typography>
            ) : (
              <>
                <Typography variant="body1" gutterBottom>
                  Arraste arquivos aqui ou clique para selecionar
                </Typography>
                <Typography variant="body2" color="text.secondary">
                  Suporta: PDF, DOCX, TXT, CSV, XLSX, PNG, JPG
                </Typography>
                <Typography variant="caption" color="text.secondary">
                  Tamanho máximo: 50MB por arquivo
                </Typography>
              </>
            )}
          </Box>

          {uploading && (
            <Box sx={{ mt: 2 }}>
              <Typography variant="body2" gutterBottom>
                Processando arquivo... {uploadProgress}%
              </Typography>
              <LinearProgress variant="determinate" value={uploadProgress} />
            </Box>
          )}

          {error && (
            <Alert severity="error" sx={{ mt: 2 }}>
              {error}
            </Alert>
          )}

          <Box sx={{ mt: 2 }}>
            <Typography variant="body2" color="text.secondary">
              Tipos de análise realizados:
            </Typography>
            <Stack direction="row" spacing={1} sx={{ mt: 1 }}>
              <Chip label="Extração de Texto" size="small" />
              <Chip label="OCR (Imagens)" size="small" />
              <Chip label="Análise de Entidades" size="small" />
              <Chip label="Detecção de Eventos" size="small" />
            </Stack>
          </Box>
        </Paper>
      </Grid>

      <Grid item xs={12} md={6}>
        <Paper sx={{ p: 3 }}>
          <Typography variant="h6" gutterBottom>
            📋 Arquivos Processados ({uploadedFiles.length})
          </Typography>
          
          {uploadedFiles.length === 0 ? (
            <Typography variant="body2" color="text.secondary">
              Nenhum arquivo processado ainda.
            </Typography>
          ) : (
            <List>
              {uploadedFiles.map((file, index) => (
                <ListItem key={index} divider>
                  <ListItemIcon>
                    {file.status === 'success' ? (
                      <SuccessIcon color="success" />
                    ) : (
                      <ErrorIcon color="error" />
                    )}
                  </ListItemIcon>
                  <ListItemText
                    primary={file.name}
                    secondary={
                      <Box>
                        <Typography variant="caption">
                          {formatFileSize(file.size)} • {file.type}
                        </Typography>
                        {file.status === 'success' && file.data && (
                          <Box sx={{ mt: 1 }}>
                            <Chip 
                              label={`${file.data.entities?.length || 0} entidades`} 
                              size="small" 
                              sx={{ mr: 1 }} 
                            />
                            <Chip 
                              label={`${file.data.events?.length || 0} eventos`} 
                              size="small" 
                            />
                          </Box>
                        )}
                        {file.status === 'error' && (
                          <Typography variant="caption" color="error">
                            Erro: {file.error}
                          </Typography>
                        )}
                      </Box>
                    }
                  />
                </ListItem>
              ))}
            </List>
          )}
        </Paper>
      </Grid>

      {/* Resumo dos dados processados */}
      {uploadedFiles.some(f => f.status === 'success') && (
        <Grid item xs={12}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>
                📊 Resumo do Processamento
              </Typography>
              
              <Grid container spacing={2}>
                <Grid item xs={12} md={3}>
                  <Box textAlign="center">
                    <Typography variant="h4" color="primary">
                      {uploadedFiles.filter(f => f.status === 'success').length}
                    </Typography>
                    <Typography variant="body2">
                      Documentos Processados
                    </Typography>
                  </Box>
                </Grid>
                
                <Grid item xs={12} md={3}>
                  <Box textAlign="center">
                    <Typography variant="h4" color="primary">
                      {uploadedFiles
                        .filter(f => f.status === 'success' && f.data)
                        .reduce((sum, f) => sum + (f.data.entities?.length || 0), 0)}
                    </Typography>
                    <Typography variant="body2">
                      Entidades Extraídas
                    </Typography>
                  </Box>
                </Grid>
                
                <Grid item xs={12} md={3}>
                  <Box textAlign="center">
                    <Typography variant="h4" color="primary">
                      {uploadedFiles
                        .filter(f => f.status === 'success' && f.data)
                        .reduce((sum, f) => sum + (f.data.events?.length || 0), 0)}
                    </Typography>
                    <Typography variant="body2">
                      Eventos Detectados
                    </Typography>
                  </Box>
                </Grid>
                
                <Grid item xs={12} md={3}>
                  <Box textAlign="center">
                    <Typography variant="h4" color="secondary">
                      {Math.round(uploadedFiles
                        .filter(f => f.status === 'success')
                        .reduce((sum, f) => sum + f.size, 0) / 1024 / 1024 * 100) / 100}
                    </Typography>
                    <Typography variant="body2">
                      MB Processados
                    </Typography>
                  </Box>
                </Grid>
              </Grid>
            </CardContent>
          </Card>
        </Grid>
      )}
    </Grid>
  );
}

export default DocumentUpload; 