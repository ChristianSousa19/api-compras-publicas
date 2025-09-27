1. Justificativa da Escolha do Dataset
Para a construção desta API, foi selecionado o conjunto de dados de "Compras Públicas do Governo Federal" , uma fonte de dados aberta e mantida pelo Governo Federal, disponível para consulta e download no Portal da Transparência.   

A escolha foi motivada pelos seguintes fatores:

Complexidade do Mundo Real: O dataset reflete um cenário de negócio real e complexo, contendo múltiplas entidades inter-relacionadas (Licitações, Contratos, Fornecedores, Órgãos, etc.), o que permitiu a aplicação de conceitos avançados de modelagem de dados.

Riqueza de Relacionamentos: A estrutura dos dados possibilitou a implementação de relacionamentos de banco de dados essenciais, como um-para-muitos (1:N) e muitos-para-muitos (N:N), demonstrando a capacidade do SQLAlchemy ORM em lidar com esses cenários.

Volume e Relevância: A grande quantidade de dados oferece um ambiente ideal para a implementação de funcionalidades avançadas, como paginação, filtragem e ordenação, que são cruciais em APIs de produção.

Disponibilidade e Documentação: Os dados são públicos, de fácil acesso em formato CSV, e acompanhados de um dicionário de dados oficial, que foi fundamental para a etapa de análise e modelagem.   

2. Descrição da Modelagem de Dados
A modelagem do banco de dados foi realizada com base em uma análise exploratória dos arquivos CSV e do dicionário de dados oficial. A implementação foi feita utilizando o ORM (Object-Relational Mapper) do SQLAlchemy, que traduz classes Python em tabelas de um banco de dados relacional.

As principais entidades modeladas foram:

User: Representa os usuários do sistema, com atributos para username, hashed_password e role (perfil, ex: "admin", "leitor").

Licitacao: Armazena as informações centrais de uma licitação.

Contrato: Contém os detalhes dos contratos derivados de uma licitação.

Fornecedor: Modela as empresas ou pessoas físicas que participam dos processos.

Os relacionamentos entre as entidades foram definidos da seguinte forma:

Um-para-Muitos (1:N):

Uma Licitacao pode originar múltiplos Contratos.

Um Fornecedor pode ter múltiplos Contratos.

Muitos-para-Muitos (N:N):

Uma Licitacao pode ter a participação de múltiplos Fornecedores, e um Fornecedor pode participar de múltiplas Licitacoes. Este relacionamento foi implementado através de uma tabela de associação (licitacao_fornecedor_association), que conecta as chaves primárias de ambas as entidades.   

A gestão das versões do esquema do banco de dados é realizada pela ferramenta Alembic, garantindo que as alterações na estrutura das tabelas sejam controladas e aplicadas de forma consistente.   

(Observação: Um diagrama visual Entidade-Relacionamento (DER) é um entregável complementar a este relatório).

3. Explicação da Estrutura da API
A API foi desenvolvida com o framework FastAPI e segue o princípio da Arquitetura em Camadas (Layered Architecture), que promove a separação de responsabilidades (Separation of Concerns), facilitando a manutenção, a testabilidade e a escalabilidade do projeto.   

A estrutura de diretórios reflete essa separação:

app/api/ (Camada de Apresentação): Responsável por definir os endpoints (rotas), receber as requisições HTTP e retornar as respostas. Esta camada é "magra", contendo o mínimo de lógica e delegando o trabalho para as camadas inferiores.   

app/crud/ (Camada de Acesso a Dados): Implementa o Padrão de Repositório (Repository Pattern). Abstrai toda a lógica de comunicação com o banco de dados, oferecendo métodos genéricos de CRUD (Create, Read, Update, Delete).   

app/models/ (Camada de Modelo): Contém as classes Python que mapeiam as tabelas do banco de dados, utilizando o ORM do SQLAlchemy.   

app/schemas/ (Camada de Esquema): Define os "Data Transfer Objects" (DTOs) usando Pydantic. Esses esquemas validam os dados de entrada e formatam os dados de saída da API, servindo como um "contrato" claro de dados.   

app/core/ (Núcleo da Aplicação): Armazena as configurações centrais (.env), a lógica de segurança (hashing de senhas, criação e validação de tokens JWT) e a configuração da conexão com o banco de dados.

A segurança é garantida por um sistema de autenticação baseado em Tokens JWT, com perfis de usuário (roles) que permitem o controle de acesso a rotas específicas (ex: apenas um admin pode criar uma nova licitação).   

4. Evidências de Testes
Os testes funcionais da API foram realizados manualmente utilizando a documentação interativa Swagger UI, gerada automaticamente pelo FastAPI e acessível em http://127.0.0.1:8000/docs.   

O fluxo de teste completo validou com sucesso as seguintes etapas:

Criação de Usuário: Um novo usuário com o perfil de admin foi criado com sucesso através de uma requisição POST para o endpoint /api/v1/users/.

Autenticação: O usuário admin realizou o login com sucesso através de uma requisição POST para /api/v1/login/token, recebendo um access_token e um refresh_token.

Autorização: O access_token obtido foi utilizado para autorizar requisições subsequentes, inserindo-o no cabeçalho Authorization como um Bearer Token.

Acesso a Rota Protegida: Uma requisição POST autenticada para o endpoint /api/v1/licitacoes/ foi realizada com sucesso, confirmando que o controle de acesso por perfil (admin) está funcionando.

Acesso a Rota Pública: Uma requisição GET para /api/v1/licitacoes/ retornou a lista de licitações, confirmando que o acesso público funciona como esperado.