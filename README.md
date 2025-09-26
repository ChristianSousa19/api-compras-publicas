API de Compras Públicas - FastAPI
!(https://www.google.com/search?q=https://img.shields.io/badge/SQLAlchemy-2.0-red%3Fstyle%3Dfor-the-badge%26logo%3Dsqlalchemy)

API RESTful para consulta de dados de licitações e contratos do Governo Federal, construída com FastAPI, SQLAlchemy e SQLite. Este projeto serve como um backend robusto para aplicações que necessitam consumir dados públicos de forma estruturada, seguindo as melhores práticas de arquitetura de software.

✨ Funcionalidades
Autenticação JWT: Sistema de segurança completo com tokens de acesso, tokens de atualização e perfis de usuário (admin, leitor).

Arquitetura em Camadas: Separação clara de responsabilidades (rotas, serviços, repositórios) para facilitar a manutenção e escalabilidade.

Operações CRUD: Endpoints completos para gerenciar Licitacoes, Contratos, Fornecedores e Users.

Migrações de Banco de Dados: Uso do Alembic para versionar o esquema do banco de dados de forma segura e consistente.

Documentação Automática: Geração automática de documentação interativa da API com Swagger UI (/docs) e ReDoc (/redoc).

Configuração Centralizada: Gestão de configurações e segredos através de variáveis de ambiente com Pydantic.

🛠️ Tecnologias Utilizadas
Backend: Python 3.10+

Framework: FastAPI

ORM: SQLAlchemy 2.0

Banco de Dados: SQLite

Migrações: Alembic

Segurança: Passlib (Hashing), Python-JOSE (JWT)

Servidor ASGI: Uvicorn

📂 Estrutura do Projeto
O projeto segue uma arquitetura em camadas para garantir a separação de responsabilidades e a manutenibilidade.
/
├── alembic/              # Scripts de migração do Alembic
├── app/                  # Código fonte principal da aplicação
│   ├── api/              # Camada de Apresentação (API)
│   │   └── v1/
│   │       ├── endpoints/  # Módulos de rotas (users.py, login.py, etc.)
│   │       ├── dependencies.py
│   │       └── router.py   # Agregador dos roteadores da v1
│   ├── core/             # Lógica central: config, database, security
│   ├── crud/             # Camada de Acesso a Dados (Repository Pattern)
│   ├── models/           # Modelos do ORM SQLAlchemy
│   └── schemas/          # Esquemas Pydantic (DTOs)
├──.env                  # Arquivo de variáveis de ambiente (NÃO VERSIONADO)
├──.env.example          # Arquivo de exemplo para as variáveis de ambiente
├──.gitignore
├── alembic.ini           # Configuração do Alembic
├── main.py               # Ponto de entrada da aplicação FastAPI
└── requirements.txt


## 🚀 Instalação e Execução

Siga os passos abaixo para configurar e executar o projeto localmente.

#### 1. Pré-requisitos

-   [Python 3.10 ou superior](https://www.python.org/downloads/)
-   [Git](https://git-scm.com/downloads)

#### 2. Clone o repositório

```bash
git clone [https://github.com/ChristianSousa19/api-compras-publicas.git](https://github.com/ChristianSousa19/api-compras-publicas.git)
cd api-compras-publicas
3. Crie e ative o ambiente virtual
Bash

# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\Activate.ps1

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
4. Instale as dependências
Bash

pip install -r requirements.txt
5. Configure as variáveis de ambiente
Crie uma cópia do arquivo .env.example e renomeie para .env.

Bash

# Windows
copy.env.example.env

# macOS / Linux
cp.env.example.env
Abra o arquivo .env e gere uma nova SECRET_KEY segura. Você pode usar o comando abaixo no terminal para gerar uma:

Bash

python -c "import secrets; print(secrets.token_hex(32))"
Cole a chave gerada no seu arquivo .env, substituindo o valor existente.

6. Execute as migrações do banco de dados
Este comando criará o arquivo compras_publicas.db e todas as tabelas necessárias com base nos modelos definidos.

Bash

alembic upgrade head
7. Inicie a aplicação
Bash

uvicorn main:app --reload
A API estará disponível em http://127.0.0.1:8000.

📚 Endpoints da API e Testes
A documentação completa e interativa é gerada automaticamente pelo FastAPI e está disponível nos seguintes endereços:

Swagger UI: http://127.0.0.1:8000/docs (Permite interagir e testar os endpoints)

ReDoc: http://127.0.0.1:8000/redoc (Documentação visual alternativa)

Fluxo de Teste Rápido:
Acesse http://127.0.0.1:8000/docs.

Use o endpoint POST /api/v1/users/ para criar um novo usuário com a role de "admin".

Use o endpoint POST /api/v1/login/token com as credenciais do usuário criado para obter um access_token.

Clique no botão "Authorize" no topo da página e cole o token no formato Bearer <seu_token>.

Agora você está autenticado e pode testar as rotas protegidas, como POST /api/v1/licitacoes/.

🌿 Modelo de Branches (GitFlow)
Este projeto utiliza o modelo de branches GitFlow para organizar o desenvolvimento de forma profissional e segura:    

main: Contém o código de produção estável. Cada merge nesta branch representa uma nova versão.

develop: Branch principal de desenvolvimento. Integra todas as novas funcionalidades que foram finalizadas e testadas. É a branch base para futuras releases.

feature/*: Branches para o desenvolvimento de novas funcionalidades. São criadas a partir da develop e, ao serem concluídas, são mescladas de volta na develop.