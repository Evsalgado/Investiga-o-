import React from 'react';
import { 
  Paper, 
  Typography, 
  Box, 
  Grid,
  Card,
  CardContent,
  Alert,
  Chip,
  LinearProgress
} from '@mui/material';
import { 
  Insights as InsightsIcon,
  Warning as WarningIcon,
  TrendingUp as TrendIcon,
  Security as SecurityIcon 
} from '@mui/icons-material';

function InsightsDashboard({ patterns = [] }) {
  const mockInsights = [
    {
      id: 1,
      type: 'RISK_ASSESSMENT',
      title: 'Padrão de Transferências Suspeitas Detectado',
      description: 'Identificadas 8 transferências em valores quebrados realizadas sempre aos finais de semana',
      confidence: 0.85,
      riskLevel: 'high',
      recommendations: [
        'Investigar justificativas para operações fora do horário comercial',
        'Verificar relacionamento entre as entidades envolvidas',
        'Analisar origem dos recursos transferidos'
      ]
    },
    {
      id: 2,
      type: 'TEMPORAL_ANOMALY',
      title: 'Concentração Temporal de Atividades',
      description: 'Movimentações financeiras concentradas no período de 15/01 a 28/02/2024',
      confidence: 0.72,
      riskLevel: 'medium',
      recommendations: [
        'Verificar eventos que possam explicar a concentração',
        'Investigar mudanças organizacionais no período',
        'Analisar padrões similares em períodos anteriores'
      ]
    },
    {
      id: 3,
      type: 'ENTITY_CLUSTERING',
      title: 'Rede de Entidades Relacionadas',
      description: 'Identificado cluster de 5 entidades com padrão de relacionamento circular',
      confidence: 0.91,
      riskLevel: 'critical',
      recommendations: [
        'Mapear todos os relacionamentos entre as entidades',
        'Verificar legitimidade das operações',
        'Investigar possível esquema de lavagem de dinheiro'
      ]
    }
  ];

  const getRiskColor = (riskLevel) => {
    switch (riskLevel) {
      case 'critical': return 'error';
      case 'high': return 'warning';
      case 'medium': return 'info';
      case 'low': return 'success';
      default: return 'default';
    }
  };

  const getRiskIcon = (riskLevel) => {
    switch (riskLevel) {
      case 'critical': return <SecurityIcon />;
      case 'high': return <WarningIcon />;
      case 'medium': return <TrendIcon />;
      case 'low': return <InsightsIcon />;
      default: return <InsightsIcon />;
    }
  };

  const getRiskLabel = (riskLevel) => {
    const labels = {
      'critical': 'CRÍTICO',
      'high': 'ALTO',
      'medium': 'MÉDIO',
      'low': 'BAIXO'
    };
    return labels[riskLevel] || 'DESCONHECIDO';
  };

  return (
    <Box>
      <Typography variant="h6" gutterBottom>
        💡 Insights e Análises
      </Typography>
      
      {/* Resumo */}
      <Grid container spacing={2} sx={{ mb: 3 }}>
        <Grid item xs={12} md={3}>
          <Card>
            <CardContent sx={{ textAlign: 'center' }}>
              <Typography variant="h4" color="error">
                1
              </Typography>
              <Typography variant="body2">
                Risco Crítico
              </Typography>
            </CardContent>
          </Card>
        </Grid>
        <Grid item xs={12} md={3}>
          <Card>
            <CardContent sx={{ textAlign: 'center' }}>
              <Typography variant="h4" color="warning.main">
                1
              </Typography>
              <Typography variant="body2">
                Risco Alto
              </Typography>
            </CardContent>
          </Card>
        </Grid>
        <Grid item xs={12} md={3}>
          <Card>
            <CardContent sx={{ textAlign: 'center' }}>
              <Typography variant="h4" color="info.main">
                1
              </Typography>
              <Typography variant="body2">
                Risco Médio
              </Typography>
            </CardContent>
          </Card>
        </Grid>
        <Grid item xs={12} md={3}>
          <Card>
            <CardContent sx={{ textAlign: 'center' }}>
              <Typography variant="h4" color="primary">
                3
              </Typography>
              <Typography variant="body2">
                Total Insights
              </Typography>
            </CardContent>
          </Card>
        </Grid>
      </Grid>

      {/* Lista de Insights */}
      <Grid container spacing={3}>
        {mockInsights.map((insight) => (
          <Grid item xs={12} key={insight.id}>
            <Card sx={{ borderLeft: 4, borderColor: `${getRiskColor(insight.riskLevel)}.main` }}>
              <CardContent>
                <Box sx={{ display: 'flex', alignItems: 'flex-start', mb: 2 }}>
                  <Box sx={{ mr: 2, color: `${getRiskColor(insight.riskLevel)}.main` }}>
                    {getRiskIcon(insight.riskLevel)}
                  </Box>
                  <Box sx={{ flexGrow: 1 }}>
                    <Box sx={{ display: 'flex', alignItems: 'center', mb: 1 }}>
                      <Typography variant="h6" sx={{ flexGrow: 1 }}>
                        {insight.title}
                      </Typography>
                      <Chip 
                        label={getRiskLabel(insight.riskLevel)}
                        color={getRiskColor(insight.riskLevel)}
                        size="small"
                      />
                    </Box>
                    
                    <Typography variant="body1" paragraph>
                      {insight.description}
                    </Typography>
                    
                    <Box sx={{ mb: 2 }}>
                      <Typography variant="body2" gutterBottom>
                        Confiança: {Math.round(insight.confidence * 100)}%
                      </Typography>
                      <LinearProgress 
                        variant="determinate" 
                        value={insight.confidence * 100}
                        color={getRiskColor(insight.riskLevel)}
                        sx={{ height: 6, borderRadius: 3 }}
                      />
                    </Box>
                    
                    <Typography variant="subtitle2" gutterBottom>
                      Recomendações:
                    </Typography>
                    <Box component="ul" sx={{ pl: 2, m: 0 }}>
                      {insight.recommendations.map((rec, index) => (
                        <Typography component="li" key={index} variant="body2" sx={{ mb: 0.5 }}>
                          {rec}
                        </Typography>
                      ))}
                    </Box>
                  </Box>
                </Box>
              </CardContent>
            </Card>
          </Grid>
        ))}
      </Grid>

      {/* Alerta informativo */}
      <Alert severity="info" sx={{ mt: 3 }}>
        <Typography variant="body2">
          <strong>📊 Como interpretar:</strong> Os insights são gerados automaticamente 
          pela análise de IA dos documentos processados. Níveis de risco mais altos 
          requerem investigação prioritária.
        </Typography>
      </Alert>
    </Box>
  );
}

export default InsightsDashboard; 