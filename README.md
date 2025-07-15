# Rest-API de Alunos

API REST para cadastro, atualização, listagem e acompanhamento de progresso de alunos, desenvolvida com Django Ninja.

## Funcionalidades

- Cadastro de alunos com validação de e-mail único
- Listagem de todos os alunos cadastrados
- Consulta de progresso do aluno (aulas concluídas e faltantes para graduação)
- Registro de aulas concluídas
- Atualização dos dados do aluno com validação de faixa e idade

## Endpoints

### Criar Aluno

- **POST** `/api/`
- **Body (JSON):**
  ```json
  {
    "nome": "caio",
    "email": "caio@email.com",
    "faixa": "B",
    "data_nascimento": "2025-02-14"
  }
  ```
- **Respostas:**
  - `200 OK`: Retorna os dados do aluno cadastrado
  - `400 Bad Request`: E-mail já cadastrado

### Listar Alunos

- **GET** `/api/aluno/`
- **Respostas:**
  - `200 OK`: Lista de alunos cadastrados

### Progresso do Aluno

- **GET** `/api/progresso_aluno/?email_aluno=caio@email.com`
- **Respostas:**
  - `200 OK`: Dados de progresso do aluno

### Registrar Aulas Concluídas

- **POST** `/api/aulas_concluidas/`
- **Body (JSON):**
  ```json
  {
    "quantidade": 2,
    "email_aluno": "caio@email.com"
  }
  ```
- **Respostas:**
  - `200 OK`: Mensagem de sucesso

### Atualizar Aluno

- **PUT** `/api/alunos/{aluno_id}/`
- **Body (JSON):**
  ```json
  {
    "nome": "novo nome",
    "email": "novo@email.com",
    "faixa": "AZ",
    "data_nascimento": "2000-01-01"
  }
  ```
- **Respostas:**
  - `200 OK`: Dados atualizados
  - `404 Not Found`: Aluno não encontrado
  - `400 Bad Request`: Validação de faixa/idade

## Tecnologias

- Python
- Django
- Django Ninja
- APIREST

> Projeto desenvolvido para fins de estudo.