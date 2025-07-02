import React, { useState, useEffect } from 'react';
import { 
  AppBar, 
  Toolbar, 
  Typography, 
  Container, 
  Grid, 
  Paper, 
  Box,
  CssBaseline,
  ThemeProvider,
  createTheme,
  Drawer,
  List,
  ListItem,
  ListItemIcon,
  ListItemText,
  Divider
} from '@mui/material';
import {
  Upload as UploadIcon,
  Timeline as TimelineIcon,
  AccountTree as NetworkIcon,
  Search as SearchIcon,
  Insights as InsightsIcon,
  Dashboard as DashboardIcon
} from '@mui/icons-material';

import DocumentUpload from './components/DocumentUpload';
import Timeline from './components/Timeline';
import EntityNetwork from './components/EntityNetwork';
import QueryInterface from './components/QueryInterface';
import InsightsDashboard from './components/InsightsDashboard';
import './App.css';

const theme = createTheme({
  palette: {
    primary: {
      main: '#1976d2',
    },
    secondary: {
      main: '#dc004e',
    },
    background: {
      default: '#f5f5f5',
    },
  },
});

const drawerWidth = 240;

function App() {
  const [currentView, setCurrentView] = useState('dashboard');
  const [documents, setDocuments] = useState([]);
  const [entities, setEntities] = useState([]);
  const [timelineEvents, setTimelineEvents] = useState([]);
  const [patterns, setPatterns] = useState([]);

  const menuItems = [
    { id: 'dashboard', label: 'Dashboard', icon: <DashboardIcon /> },
    { id: 'upload', label: 'Upload Documentos', icon: <UploadIcon /> },
    { id: 'timeline', label: 'Linha do Tempo', icon: <TimelineIcon /> },
    { id: 'network', label: 'Rede de Entidades', icon: <NetworkIcon /> },
    { id: 'query', label: 'Consultas IA', icon: <SearchIcon /> },
    { id: 'insights', label: 'Insights', icon: <InsightsIcon /> },
  ];

  const handleDocumentProcessed = (documentData) => {
    setDocuments(prev => [...prev, documentData]);
    setEntities(prev => [...prev, ...documentData.entities]);
    setTimelineEvents(prev => [...prev, ...documentData.events]);
  };

  const renderCurrentView = () => {
    switch (currentView) {
      case 'upload':
        return <DocumentUpload onDocumentProcessed={handleDocumentProcessed} />;
      case 'timeline':
        return <Timeline events={timelineEvents} />;
      case 'network':
        return <EntityNetwork entities={entities} />;
      case 'query':
        return <QueryInterface />;
      case 'insights':
        return <InsightsDashboard patterns={patterns} />;
      default:
        return <DashboardOverview 
          documents={documents} 
          entities={entities} 
          events={timelineEvents}
          patterns={patterns}
        />;
    }
  };

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Box sx={{ display: 'flex' }}>
        <AppBar position="fixed" sx={{ zIndex: (theme) => theme.zIndex.drawer + 1 }}>
          <Toolbar>
            <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
              🛠️ InvestigIA - Análise Investigativa Inteligente
            </Typography>
          </Toolbar>
        </AppBar>
        
        <Drawer
          variant="permanent"
          sx={{
            width: drawerWidth,
            flexShrink: 0,
            [`& .MuiDrawer-paper`]: { width: drawerWidth, boxSizing: 'border-box' },
          }}
        >
          <Toolbar />
          <Box sx={{ overflow: 'auto' }}>
            <List>
              {menuItems.map((item) => (
                <ListItem 
                  button 
                  key={item.id}
                  selected={currentView === item.id}
                  onClick={() => setCurrentView(item.id)}
                >
                  <ListItemIcon>
                    {item.icon}
                  </ListItemIcon>
                  <ListItemText primary={item.label} />
                </ListItem>
              ))}
            </List>
          </Box>
        </Drawer>
        
        <Box component="main" sx={{ flexGrow: 1, p: 3 }}>
          <Toolbar />
          <Container maxWidth="xl">
            {renderCurrentView()}
          </Container>
        </Box>
      </Box>
    </ThemeProvider>
  );
}

// Componente Dashboard Overview
function DashboardOverview({ documents, entities, events, patterns }) {
  return (
    <Grid container spacing={3}>
      <Grid item xs={12} md={3}>
        <Paper sx={{ p: 2, textAlign: 'center' }}>
          <Typography variant="h4" color="primary">
            {documents.length}
          </Typography>
          <Typography variant="body1">
            Documentos Processados
          </Typography>
        </Paper>
      </Grid>
      
      <Grid item xs={12} md={3}>
        <Paper sx={{ p: 2, textAlign: 'center' }}>
          <Typography variant="h4" color="primary">
            {entities.length}
          </Typography>
          <Typography variant="body1">
            Entidades Identificadas
          </Typography>
        </Paper>
      </Grid>
      
      <Grid item xs={12} md={3}>
        <Paper sx={{ p: 2, textAlign: 'center' }}>
          <Typography variant="h4" color="primary">
            {events.length}
          </Typography>
          <Typography variant="body1">
            Eventos na Timeline
          </Typography>
        </Paper>
      </Grid>
      
      <Grid item xs={12} md={3}>
        <Paper sx={{ p: 2, textAlign: 'center' }}>
          <Typography variant="h4" color="secondary">
            {patterns.length}
          </Typography>
          <Typography variant="body1">
            Padrões Detectados
          </Typography>
        </Paper>
      </Grid>
      
      <Grid item xs={12}>
        <Paper sx={{ p: 3 }}>
          <Typography variant="h6" gutterBottom>
            Bem-vindo ao InvestigIA
          </Typography>
          <Typography variant="body1" paragraph>
            Esta plataforma utiliza inteligência artificial para auxiliar em investigações, 
            organizando dados em uma linha do tempo interativa e detectando padrões suspeitos.
          </Typography>
          <Typography variant="body2">
            Para começar:
          </Typography>
          <Box component="ul" sx={{ mt: 1 }}>
            <li>Faça upload de documentos (PDF, DOCX, imagens, planilhas)</li>
            <li>Visualize a linha do tempo de eventos</li>
            <li>Explore a rede de relacionamentos entre entidades</li>
            <li>Use consultas em linguagem natural para análises específicas</li>
            <li>Revise insights e padrões detectados pela IA</li>
          </Box>
        </Paper>
      </Grid>
    </Grid>
  );
}

export default App; 