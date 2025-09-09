# 🚀 Ollama + Pytest + BDD - Automação de Testes com IA

Este projeto demonstra como integrar **Ollama** (IA local), **Pytest** e **BDD** (Behavior Driven Development) para criar testes automatizados inteligentes que geram dados dinamicamente usando modelos de linguagem.

## 📋 Índice

- [Visão Geral](#-visão-geral)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Pré-requisitos](#-pré-requisitos)
- [Instalação](#-instalação)
- [Configuração](#-configuração)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Cenários de Teste](#-cenários-de-teste)
- [Executando os Testes](#-executando-os-testes)
- [Relatórios](#-relatórios)
- [Exemplos de Uso](#-exemplos-de-uso)
- [Troubleshooting](#-troubleshooting)

## 🎯 Visão Geral

Este projeto combina:
- **Ollama**: Para gerar dados de teste dinamicamente usando IA
- **Pytest**: Framework de testes Python
- **BDD**: Desenvolvimento orientado a comportamento com Gherkin
- **ReqRes API**: API pública para testes (https://reqres.in)

### Principais Benefícios

✅ **Geração Inteligente de Dados**: Usa IA para criar payloads de teste únicos  
✅ **Testes Legíveis**: Cenários em linguagem natural (Gherkin)  
✅ **Automação Completa**: Execução e validação automática  
✅ **Relatórios Detalhados**: Saída em HTML e JSON  

## 🛠 Tecnologias Utilizadas

| Tecnologia | Versão | Descrição |
|------------|--------|-----------|
| Python | 3.8+ | Linguagem principal |
| Pytest | 7.2+ | Framework de testes |
| Pytest-BDD | 4.1+ | Integração BDD |
| Ollama | Latest | IA local para geração de dados |
| Requests | 2.28+ | Cliente HTTP |
| HTTPX | 0.24+ | Cliente HTTP assíncrono |

## 📋 Pré-requisitos

### 1. Python 3.8+
```bash
python --version
# ou
python3 --version
```

### 2. Ollama Instalado
```bash
# macOS
brew install ollama

# Linux
curl -fsSL https://ollama.ai/install.sh | sh

# Windows
# Baixe do site: https://ollama.ai/download
```

### 3. Modelo de IA Baixado
```bash
# Baixe um modelo (exemplo: phi3)
ollama pull phi3

# Ou use outros modelos disponíveis
ollama list
```

## 🚀 Instalação

### 1. Clone o Repositório
```bash
git clone <url-do-repositorio>
cd Ollama_Pytest-_BDD
```

### 2. Crie um Ambiente Virtual
```bash
python -m venv venv

# Ative o ambiente virtual
# macOS/Linux:
source venv/bin/activate

# Windows:
venv\Scripts\activate
```

### 3. Instale as Dependências
```bash
pip install -r requirements.txt
```

## ⚙️ Configuração

### 1. Variáveis de Ambiente (Opcional)
```bash
# Defina o modelo Ollama a ser usado
export OLLAMA_MODEL=phi3

# Ou crie um arquivo .env
echo "OLLAMA_MODEL=phi3" > .env
```

### 2. Verifique a Instalação
```bash
# Teste se o Ollama está funcionando
ollama list

# Teste se o Python consegue importar as dependências
python -c "import pytest, ollama, requests; print('✅ Todas as dependências instaladas!')"
```

## 📁 Estrutura do Projeto

```
Ollama_Pytest-_BDD/
├── src/
│   ├── tests/
│   │   ├── features/           # Arquivos .feature (Gherkin)
│   │   │   └── users.feature
│   │   └── steps/             # Implementação dos steps
│   │       └── test_users_steps.py
│   └── utils/                 # Utilitários
│       └── payload_generator.py
├── pytest.ini                # Configuração do Pytest
├── requirements.txt          # Dependências Python
├── report.json              # Relatório de execução
└── README.md               # Este arquivo
```

### Descrição dos Arquivos

- **`users.feature`**: Cenários de teste em linguagem Gherkin
- **`test_users_steps.py`**: Implementação dos steps dos cenários
- **`payload_generator.py`**: Geração de dados usando Ollama
- **`pytest.ini`**: Configuração do Pytest

## 🧪 Cenários de Teste

### 1. Listar Usuários
```gherkin
Scenario: Listar usuários
  When eu faço uma requisição GET para "/users?page=2"
  Then a resposta deve ter status 200
  And a resposta deve conter o campo "data"
```

**O que testa:**
- ✅ Endpoint GET funcional
- ✅ Status code correto (200)
- ✅ Estrutura da resposta válida

### 2. Criar Usuário Válido
```gherkin
Scenario: Criar usuário válido
  Given que eu gero um payload de usuário válido
  When eu faço uma requisição POST para "/users" com esse payload
  Then a resposta deve ter status 201
  And a resposta deve conter o campo "id"
```

**O que testa:**
- ✅ Geração dinâmica de dados com IA
- ✅ Criação de usuário via POST
- ✅ Status code de criação (201)
- ✅ Retorno do ID do usuário criado

### 3. Login Inválido
```gherkin
Scenario: Login inválido
  When eu faço uma requisição POST para "/login" com payload inválido
  Then a resposta deve ter status 401
  And a resposta deve conter o campo "error"
```

**O que testa:**
- ✅ Tratamento de credenciais inválidas
- ✅ Status code de erro (401)
- ✅ Mensagem de erro apropriada

## 🏃‍♂️ Executando os Testes

### 1. Execução Básica
```bash
# Execute todos os testes
pytest

# Execute com output detalhado
pytest -v

# Execute um arquivo específico
pytest src/tests/steps/test_users_steps.py
```

### 2. Execução com Relatórios
```bash
# Gere relatório HTML
pytest --html=report.html

# Gere relatório JSON
pytest --json-report --json-report-file=report.json

# Execute em paralelo (mais rápido)
pytest -n auto
```

### 3. Execução com Filtros
```bash
# Execute apenas cenários com tag específica
pytest -k "criar_usuario"

# Execute com output colorido
pytest --color=yes

# Execute e pare no primeiro erro
pytest -x
```

### 4. Execução com Debug
```bash
# Execute com logs detalhados
pytest -s -v

# Execute com breakpoint no primeiro erro
pytest --pdb
```

## 📊 Relatórios

### Relatório HTML
```bash
pytest --html=report.html --self-contained-html
```
- Abra `report.html` no navegador
- Visualização interativa dos resultados
- Detalhes de cada teste executado

### Relatório JSON
```bash
pytest --json-report --json-report-file=report.json
```
- Estrutura de dados para integração
- Análise programática dos resultados
- Integração com CI/CD

## 💡 Exemplos de Uso

### 1. Execução Completa
```bash
# Ambiente virtual ativado
source venv/bin/activate

# Execute todos os testes com relatório
pytest -v --html=report.html --self-contained-html

# Abra o relatório
open report.html
```

### 2. Teste Específico
```bash
# Execute apenas o cenário de criação de usuário
pytest -k "criar_usuario" -v

# Execute com output detalhado
pytest -k "listar_usuarios" -s -v
```

### 3. Debug de Problemas
```bash
# Execute com logs detalhados
pytest -s -v --tb=long

# Execute e pare no primeiro erro
pytest -x -v
```

## 🔧 Troubleshooting

### Problema: Ollama não encontrado
```bash
# Verifique se está instalado
ollama --version

# Se não estiver, instale:
# macOS: brew install ollama
# Linux: curl -fsSL https://ollama.ai/install.sh | sh
```

### Problema: Modelo não encontrado
```bash
# Liste modelos disponíveis
ollama list

# Baixe um modelo
ollama pull phi3
# ou
ollama pull llama2
```

### Problema: Dependências não instaladas
```bash
# Reinstale as dependências
pip install -r requirements.txt --force-reinstall

# Ou instale individualmente
pip install pytest pytest-bdd requests ollama
```

### Problema: Testes falhando
```bash
# Execute com debug
pytest -s -v --tb=long

# Verifique se a API está funcionando
curl https://reqres.in/api/users?page=2
```

### Problema: Permissões
```bash
# No Linux/macOS, pode ser necessário:
chmod +x venv/bin/activate
```

## 🎯 Próximos Passos

### Melhorias Sugeridas

1. **Mais Cenários de Teste**
   - Atualização de usuários (PUT)
   - Exclusão de usuários (DELETE)
   - Validação de campos obrigatórios

2. **Integração com CI/CD**
   - GitHub Actions
   - Jenkins Pipeline
   - GitLab CI

3. **Relatórios Avançados**
   - Allure Reports
   - Screenshots em falhas
   - Métricas de performance

4. **Testes de Performance**
   - Load testing
   - Stress testing
   - Monitoramento de tempo de resposta

## 📚 Recursos Adicionais

- [Documentação Pytest](https://docs.pytest.org/)
- [Pytest-BDD](https://pytest-bdd.readthedocs.io/)
- [Ollama Documentation](https://ollama.ai/docs)
- [ReqRes API](https://reqres.in/)
- [Gherkin Syntax](https://cucumber.io/docs/gherkin/)

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

**Desenvolvido com ❤️ para demonstrar a integração de IA com automação de testes**
