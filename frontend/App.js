import React, { useState, useEffect } from 'react';
import { 
  StyleSheet, 
  Text, 
  View, 
  TextInput, 
  TouchableOpacity, 
  ScrollView, 
  ActivityIndicator,
  Alert,
  StatusBar
} from 'react-native';
import { StatusBar as ExpoStatusBar } from 'expo-status-bar';
import { API_URL } from './config';

export default function App() {
  // Estado da tela atual ('form' ou 'resultado')
  const [telaAtual, setTelaAtual] = useState('form');
  
  // Estados do formulário
  const [materia, setMateria] = useState('');
  const [assunto, setAssunto] = useState('');
  const [nivel, setNivel] = useState('iniciante');
  const [tipo, setTipo] = useState('explicacao');
  
  // Estados de carregamento e resultado
  const [carregando, setCarregando] = useState(false);
  const [resultado, setResultado] = useState(null);
  const [erro, setErro] = useState(null);
  
  // Opções disponíveis (serão carregadas da API)
  const [opcoes, setOpcoes] = useState({
    niveis: ['iniciante', 'intermediario', 'avancado'],
    tipos: ['explicacao', 'resumo', 'quiz', 'perguntas']
  });

  // Carrega opções da API ao iniciar
  useEffect(() => {
    carregarOpcoes();
  }, []);

  const carregarOpcoes = async () => {
    try {
      const response = await fetch(`${API_URL}/opcoes`);
      const data = await response.json();
      if (data.niveis && data.tipos) {
        setOpcoes(data);
      }
    } catch (error) {
      console.log('Erro ao carregar opções, usando padrões:', error);
      // Usa valores padrão se falhar
    }
  };

  const validarFormulario = () => {
    if (!materia.trim()) {
      Alert.alert('Erro', 'Por favor, preencha o campo Matéria.');
      return false;
    }
    if (!assunto.trim()) {
      Alert.alert('Erro', 'Por favor, preencha o campo Assunto.');
      return false;
    }
    return true;
  };

  const gerarConteudo = async () => {
    if (!validarFormulario()) {
      return;
    }

    setCarregando(true);
    setErro(null);

    try {
      const response = await fetch(`${API_URL}/estudo`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          materia: materia.trim(),
          assunto: assunto.trim(),
          nivel: nivel,
          tipo: tipo
        }),
      });

      const data = await response.json();

      if (response.ok) {
        setResultado(data);
        setTelaAtual('resultado');
      } else {
        // Trata diferentes tipos de erro
        if (data.erro) {
          setErro(data.erro);
        } else {
          setErro('Erro desconhecido ao gerar conteúdo.');
        }
        Alert.alert('Erro', data.erro || 'Erro ao gerar conteúdo.');
      }
    } catch (error) {
      console.error('Erro:', error);
      const mensagemErro = 'Não foi possível conectar à API. Verifique se o backend está rodando.';
      setErro(mensagemErro);
      Alert.alert('Erro de Conexão', mensagemErro);
    } finally {
      setCarregando(false);
    }
  };

  const novaConsulta = () => {
    setTelaAtual('form');
    setResultado(null);
    setErro(null);
    // Não limpa os campos para facilitar nova consulta
  };

  // Tela de Formulário
  if (telaAtual === 'form') {
    return (
      <View style={styles.container}>
        <ExpoStatusBar style="dark" />
        
        <ScrollView contentContainerStyle={styles.scrollContent}>
          <View style={styles.card}>
            <Text style={styles.titulo}>📚 StudyIA</Text>
            <Text style={styles.subtitulo}>Seu assistente de estudos inteligente</Text>

            <View style={styles.formGroup}>
              <Text style={styles.label}>Matéria</Text>
              <TextInput
                style={styles.input}
                placeholder="Ex: Estrutura de Dados"
                value={materia}
                onChangeText={setMateria}
                maxLength={80}
              />
            </View>

            <View style={styles.formGroup}>
              <Text style={styles.label}>Assunto</Text>
              <TextInput
                style={styles.input}
                placeholder="Ex: Árvores balanceadas"
                value={assunto}
                onChangeText={setAssunto}
                maxLength={150}
              />
            </View>

            <View style={styles.formGroup}>
              <Text style={styles.label}>Nível</Text>
              <View style={styles.buttonGroup}>
                {opcoes.niveis.map((n) => (
                  <TouchableOpacity
                    key={n}
                    style={[
                      styles.optionButton,
                      nivel === n && styles.optionButtonSelected
                    ]}
                    onPress={() => setNivel(n)}
                  >
                    <Text style={[
                      styles.optionText,
                      nivel === n && styles.optionTextSelected
                    ]}>
                      {n.charAt(0).toUpperCase() + n.slice(1)}
                    </Text>
                  </TouchableOpacity>
                ))}
              </View>
            </View>

            <View style={styles.formGroup}>
              <Text style={styles.label}>O que você quer?</Text>
              <View style={styles.buttonGroup}>
                {opcoes.tipos.map((t) => (
                  <TouchableOpacity
                    key={t}
                    style={[
                      styles.optionButton,
                      tipo === t && styles.optionButtonSelected
                    ]}
                    onPress={() => setTipo(t)}
                  >
                    <Text style={[
                      styles.optionText,
                      tipo === t && styles.optionTextSelected
                    ]}>
                      {t.charAt(0).toUpperCase() + t.slice(1)}
                    </Text>
                  </TouchableOpacity>
                ))}
              </View>
            </View>

            <TouchableOpacity
              style={[styles.button, carregando && styles.buttonDisabled]}
              onPress={gerarConteudo}
              disabled={carregando}
            >
              {carregando ? (
                <ActivityIndicator color="#fff" />
              ) : (
                <Text style={styles.buttonText}>Gerar Conteúdo</Text>
              )}
            </TouchableOpacity>

            {erro && (
              <View style={styles.errorBox}>
                <Text style={styles.errorText}>{erro}</Text>
              </View>
            )}
          </View>
        </ScrollView>
      </View>
    );
  }

  // Tela de Resultado
  return (
    <View style={styles.container}>
      <ExpoStatusBar style="dark" />
      
      <ScrollView contentContainerStyle={styles.scrollContent}>
        <View style={styles.card}>
          <Text style={styles.titulo}>📚 StudyIA</Text>
          
          <View style={styles.resultadoHeader}>
            <Text style={styles.resultadoLabel}>Matéria:</Text>
            <Text style={styles.resultadoValor}>{resultado.materia}</Text>
            
            <Text style={styles.resultadoLabel}>Assunto:</Text>
            <Text style={styles.resultadoValor}>{resultado.assunto}</Text>
            
            <Text style={styles.resultadoLabel}>Nível:</Text>
            <Text style={styles.resultadoValor}>
              {resultado.nivel.charAt(0).toUpperCase() + resultado.nivel.slice(1)}
            </Text>
            
            <Text style={styles.resultadoLabel}>Tipo:</Text>
            <Text style={styles.resultadoValor}>
              {resultado.tipo.charAt(0).toUpperCase() + resultado.tipo.slice(1)}
            </Text>
          </View>

          <View style={styles.respostaContainer}>
            <Text style={styles.respostaLabel}>Resposta:</Text>
            <ScrollView style={styles.respostaScroll}>
              <Text style={styles.respostaTexto}>{resultado.resposta}</Text>
            </ScrollView>
          </View>

          <TouchableOpacity
            style={styles.button}
            onPress={novaConsulta}
          >
            <Text style={styles.buttonText}>Nova Consulta</Text>
          </TouchableOpacity>
        </View>
      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  scrollContent: {
    padding: 20,
    paddingTop: 40,
  },
  card: {
    backgroundColor: '#fff',
    borderRadius: 16,
    padding: 24,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 8,
    elevation: 3,
  },
  titulo: {
    fontSize: 32,
    fontWeight: 'bold',
    color: '#6366f1',
    textAlign: 'center',
    marginBottom: 8,
  },
  subtitulo: {
    fontSize: 16,
    color: '#6b7280',
    textAlign: 'center',
    marginBottom: 32,
  },
  formGroup: {
    marginBottom: 24,
  },
  label: {
    fontSize: 16,
    fontWeight: '600',
    color: '#374151',
    marginBottom: 8,
  },
  input: {
    borderWidth: 1,
    borderColor: '#d1d5db',
    borderRadius: 8,
    padding: 12,
    fontSize: 16,
    backgroundColor: '#fff',
  },
  buttonGroup: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 8,
  },
  optionButton: {
    flex: 1,
    minWidth: 80,
    padding: 12,
    borderRadius: 8,
    borderWidth: 1,
    borderColor: '#d1d5db',
    backgroundColor: '#fff',
    alignItems: 'center',
  },
  optionButtonSelected: {
    backgroundColor: '#6366f1',
    borderColor: '#6366f1',
  },
  optionText: {
    fontSize: 14,
    color: '#374151',
  },
  optionTextSelected: {
    color: '#fff',
    fontWeight: '600',
  },
  button: {
    backgroundColor: '#6366f1',
    borderRadius: 8,
    padding: 16,
    alignItems: 'center',
    marginTop: 8,
  },
  buttonDisabled: {
    backgroundColor: '#9ca3af',
  },
  buttonText: {
    color: '#fff',
    fontSize: 18,
    fontWeight: '600',
  },
  errorBox: {
    backgroundColor: '#fee2e2',
    borderRadius: 8,
    padding: 12,
    marginTop: 16,
  },
  errorText: {
    color: '#dc2626',
    fontSize: 14,
  },
  resultadoHeader: {
    backgroundColor: '#f3f4f6',
    borderRadius: 8,
    padding: 16,
    marginBottom: 16,
  },
  resultadoLabel: {
    fontSize: 14,
    color: '#6b7280',
    marginTop: 8,
  },
  resultadoValor: {
    fontSize: 16,
    fontWeight: '600',
    color: '#1f2937',
  },
  respostaContainer: {
    marginBottom: 16,
  },
  respostaLabel: {
    fontSize: 16,
    fontWeight: '600',
    color: '#374151',
    marginBottom: 8,
  },
  respostaScroll: {
    maxHeight: 400,
    backgroundColor: '#f9fafb',
    borderRadius: 8,
    padding: 16,
  },
  respostaTexto: {
    fontSize: 16,
    color: '#1f2937',
    lineHeight: 24,
  },
});
