import React, { useState } from 'react';
import { 
  Paper, 
  Typography, 
  Box, 
  TextField,
  Button,
  Alert,
  Chip,
  Stack,
  CircularProgress
} from '@mui/material';
import { Send as SendIcon, Psychology as AIIcon } from '@mui/icons-material';

function QueryInterface() {
  const [query, setQuery] = useState('');
  const [loading, setLoading] = useState(false);
  const [response, setResponse] = useState(null);
  const [error, setError] = useState(null);

  const exampleQueries = [
    "Mostrar transações suspeitas em março de 2024",
    "Filtrar por João Silva",
    "Buscar transferências acima de R$ 50.000",
    "Analisar padrões de fraude",
    "Mostrar conexões entre entidades"
  ];

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!query.trim()) return;

    setLoading(true);
    setError(null);

    try {
      // Simular resposta da API
      await new Promise(resolve => setTimeout(resolve, 2000));
      
      setResponse({
        query: query,
        answer: `Analisando sua consulta: "${query}". Aqui estão os resultados encontrados baseados nos dados disponíveis.`,
        suggestions: [
          "Refinar busca com período específico",
          "Incluir outras entidades relacionadas",
          "Expandir análise para documentos similares"
        ]
      });
    } catch (err) {
      setError('Erro ao processar consulta. Tente novamente.');
    } finally {
      setLoading(false);
    }
  };

  const handleExampleClick = (exampleQuery) => {
    setQuery(exampleQuery);
  };

  return (
    <Box>
      <Typography variant="h6" gutterBottom>
        🤖 Consultas com IA
      </Typography>
      
      <Paper sx={{ p: 3, mb: 3 }}>
        <Typography variant="body1" gutterBottom>
          Faça perguntas em linguagem natural sobre os dados da investigação:
        </Typography>
        
        <Box component="form" onSubmit={handleSubmit} sx={{ mt: 2 }}>
          <TextField
            fullWidth
            multiline
            rows={3}
            placeholder="Ex: Mostrar todas as transações suspeitas envolvendo João Silva em fevereiro..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            disabled={loading}
            sx={{ mb: 2 }}
          />
          
          <Button
            type="submit"
            variant="contained"
            startIcon={loading ? <CircularProgress size={20} /> : <SendIcon />}
            disabled={loading || !query.trim()}
            fullWidth
          >
            {loading ? 'Processando...' : 'Enviar Consulta'}
          </Button>
        </Box>
      </Paper>

      {/* Exemplos de consultas */}
      <Paper sx={{ p: 3, mb: 3 }}>
        <Typography variant="h6" gutterBottom>
          💡 Exemplos de Consultas
        </Typography>
        <Stack direction="row" spacing={1} flexWrap="wrap" useFlexGap>
          {exampleQueries.map((example, index) => (
            <Chip
              key={index}
              label={example}
              variant="outlined"
              clickable
              onClick={() => handleExampleClick(example)}
              sx={{ mb: 1 }}
            />
          ))}
        </Stack>
      </Paper>

      {/* Resposta */}
      {response && (
        <Paper sx={{ p: 3, mb: 3 }}>
          <Box sx={{ display: 'flex', alignItems: 'center', mb: 2 }}>
            <AIIcon sx={{ mr: 1, color: 'primary.main' }} />
            <Typography variant="h6">Resposta da IA</Typography>
          </Box>
          
          <Alert severity="info" sx={{ mb: 2 }}>
            <Typography variant="body2">
              <strong>Sua pergunta:</strong> {response.query}
            </Typography>
          </Alert>
          
          <Typography variant="body1" paragraph>
            {response.answer}
          </Typography>
          
          {response.suggestions && response.suggestions.length > 0 && (
            <Box>
              <Typography variant="subtitle2" gutterBottom>
                Sugestões para refinar:
              </Typography>
              <Stack spacing={1}>
                {response.suggestions.map((suggestion, index) => (
                  <Chip
                    key={index}
                    label={suggestion}
                    size="small"
                    color="primary"
                    variant="outlined"
                  />
                ))}
              </Stack>
            </Box>
          )}
        </Paper>
      )}

      {error && (
        <Alert severity="error" sx={{ mb: 3 }}>
          {error}
        </Alert>
      )}

      {/* Informações sobre funcionalidades */}
      <Paper sx={{ p: 3, bgcolor: 'grey.50' }}>
        <Typography variant="h6" gutterBottom>
          🔧 Funcionalidades Disponíveis
        </Typography>
        <Typography variant="body2" paragraph>
          • Filtros por data, entidade, tipo de evento
        </Typography>
        <Typography variant="body2" paragraph>
          • Busca semântica em documentos
        </Typography>
        <Typography variant="body2" paragraph>
          • Detecção de padrões suspeitos
        </Typography>
        <Typography variant="body2">
          • Análise de relacionamentos
        </Typography>
      </Paper>
    </Box>
  );
}

export default QueryInterface; 