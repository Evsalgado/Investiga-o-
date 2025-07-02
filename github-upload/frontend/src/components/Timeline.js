import React from 'react';
import { 
  Paper, 
  Typography, 
  Box, 
  List, 
  ListItem, 
  ListItemText,
  Chip,
  Avatar
} from '@mui/material';
import { Timeline as TimelineIcon } from '@mui/icons-material';

function Timeline({ events = [] }) {
  if (events.length === 0) {
    return (
      <Paper sx={{ p: 3, textAlign: 'center' }}>
        <TimelineIcon sx={{ fontSize: 48, color: 'grey.400', mb: 2 }} />
        <Typography variant="h6" color="text.secondary">
          Nenhum evento na timeline ainda
        </Typography>
        <Typography variant="body2" color="text.secondary">
          Faça upload de documentos para ver eventos cronológicos
        </Typography>
      </Paper>
    );
  }

  return (
    <Paper sx={{ p: 3 }}>
      <Typography variant="h6" gutterBottom>
        📅 Linha do Tempo ({events.length} eventos)
      </Typography>
      
      <List>
        {events.map((event, index) => (
          <ListItem key={index} sx={{ mb: 2, border: 1, borderColor: 'grey.200', borderRadius: 2 }}>
            <Avatar sx={{ mr: 2, bgcolor: 'primary.main' }}>
              {index + 1}
            </Avatar>
            <ListItemText
              primary={
                <Box>
                  <Typography variant="subtitle1">
                    {event.title || `Evento ${index + 1}`}
                  </Typography>
                  <Box sx={{ mt: 1 }}>
                    <Chip label={event.date || 'Data não informada'} size="small" sx={{ mr: 1 }} />
                    <Chip label={event.event_type || 'UNKNOWN'} size="small" color="primary" />
                  </Box>
                </Box>
              }
              secondary={
                <Box sx={{ mt: 1 }}>
                  <Typography variant="body2">
                    {event.description || 'Descrição não disponível'}
                  </Typography>
                  {event.entities_involved && event.entities_involved.length > 0 && (
                    <Typography variant="caption" color="text.secondary">
                      Entidades: {event.entities_involved.join(', ')}
                    </Typography>
                  )}
                </Box>
              }
            />
          </ListItem>
        ))}
      </List>
    </Paper>
  );
}

export default Timeline; 