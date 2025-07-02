import React from 'react';
import { 
  Paper, 
  Typography, 
  Box, 
  Grid,
  Card,
  CardContent,
  Chip
} from '@mui/material';
import { AccountTree as NetworkIcon } from '@mui/icons-material';

function EntityNetwork({ entities = [] }) {
  if (entities.length === 0) {
    return (
      <Paper sx={{ p: 3, textAlign: 'center' }}>
        <NetworkIcon sx={{ fontSize: 48, color: 'grey.400', mb: 2 }} />
        <Typography variant="h6" color="text.secondary">
          Nenhuma entidade identificada ainda
        </Typography>
        <Typography variant="body2" color="text.secondary">
          Faça upload de documentos para ver a rede de relacionamentos
        </Typography>
      </Paper>
    );
  }

  // Agrupar entidades por tipo
  const entitiesByType = entities.reduce((acc, entity) => {
    const type = entity.type || 'UNKNOWN';
    if (!acc[type]) acc[type] = [];
    acc[type].push(entity);
    return acc;
  }, {});

  const getTypeColor = (type) => {
    const colors = {
      'PERSON': 'error',
      'ORG': 'primary', 
      'MONEY': 'success',
      'DATE': 'info',
      'CPF': 'warning',
      'CNPJ': 'secondary',
      'EMAIL': 'info',
      'PHONE': 'default'
    };
    return colors[type] || 'default';
  };

  const getTypeLabel = (type) => {
    const labels = {
      'PERSON': 'Pessoas',
      'ORG': 'Organizações',
      'MONEY': 'Valores',
      'DATE': 'Datas',
      'CPF': 'CPFs',
      'CNPJ': 'CNPJs',
      'EMAIL': 'E-mails',
      'PHONE': 'Telefones'
    };
    return labels[type] || type;
  };

  return (
    <Box>
      <Typography variant="h6" gutterBottom>
        🕸️ Rede de Entidades ({entities.length} entidades)
      </Typography>
      
      <Grid container spacing={3}>
        {Object.entries(entitiesByType).map(([type, typeEntities]) => (
          <Grid item xs={12} md={6} lg={4} key={type}>
            <Card>
              <CardContent>
                <Typography variant="h6" gutterBottom>
                  {getTypeLabel(type)} ({typeEntities.length})
                </Typography>
                
                <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 1 }}>
                  {typeEntities.slice(0, 10).map((entity, index) => (
                    <Chip
                      key={index}
                      label={entity.name}
                      color={getTypeColor(type)}
                      size="small"
                      variant="outlined"
                      sx={{ mb: 1 }}
                    />
                  ))}
                  {typeEntities.length > 10 && (
                    <Chip
                      label={`+${typeEntities.length - 10} mais`}
                      size="small"
                      variant="filled"
                      color="default"
                    />
                  )}
                </Box>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>

      {/* Seção para visualizações futuras */}
      <Paper sx={{ p: 3, mt: 3, textAlign: 'center', bgcolor: 'grey.50' }}>
        <Typography variant="body1" color="text.secondary">
          🚧 Visualização de rede interativa será implementada aqui
        </Typography>
        <Typography variant="body2" color="text.secondary">
          Em breve: grafo interativo com D3.js/Cytoscape
        </Typography>
      </Paper>
    </Box>
  );
}

export default EntityNetwork; 