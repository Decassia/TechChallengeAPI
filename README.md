# Tech Challenge FASE 01 - API: Vitivinicultura da Embrapa - Curso Pós Tech - Machine Learning Engineering

# 📂 Problema de negócio

Você foi contratado para uma consultoria e seu trabalho envolve analisar os dados de vitivinicultura da Embrapa. A ideia do projeto é a criação de uma API pública de consulta nos dados do site nas respectivas abas:
  - Produção;
  - Processamento;
  - Comercialização;
  - Importação;
  - Exportação.
A API vai servir para alimentar uma base de dados que futuramente será usada para um modelo de Machine Learning.

Objetivos do projeto

Criar uma Rest API em Python que faça a consulta no site da Embrapa.
  -  Criar uma Rest API em Python que faça a consulta no site da Embrapa.
  -  Sua API deve estar documentada.
  - É recomendável (não obrigatório) a escolha de um método deautenticação (JWT, por exemplo).
  - Criar um plano para fazer o deploy da API, desenhando a arquiteturado projeto desde a ingestão até a alimentação do modelo (aqui não é necessário elaborar um modelo de ML, mas é preciso que vocês escolham um cenário interessante em que a API possa ser utilizada).
  -  Fazer um MVP realizando o deploy com um link compartilhável e um repositório no github.


# 📡 API de Dados da Vitivinicultura Embrapa

Este projeto tem como objetivo criar uma **API pública RESTful**, com autenticação via JWT, que realiza a extração, tratamento e disponibilização de dados da vitivinicultura brasileira. A API está pronta para alimentar modelos de Machine Learning, com dados estruturados e limpos, extraídos diretamente do site da Embrapa (Vitibrasil).

---

## 🧱 Arquitetura do Projeto

A seguir, apresentamos a arquitetura completa do sistema desenvolvido:

[Arquitetura do Projeto] <img width="1223" alt="image" src="https://github.com/user-attachments/assets/8a22867c-a3e3-4388-b013-af7bee1a8a31" />


### 🔄 Etapas da Arquitetura:

1. **Extração de Dados – Web Scraping**  
   - Utiliza **Selenium** e **BeautifulSoup** para extrair dados de páginas HTML com conteúdo dinâmico.
   - Scripts Python acessam periodicamente as abas de Produção, Processamento, Comercialização, Importação e Exportação.

2. **Limpeza e Processamento – Pandas**  
   - Os dados brutos são transformados com `pandas`, eliminando ruídos como rodapés, cabeçalhos duplicados, e valores nulos.
   - Os dados são convertidos para formatos numéricos e padronizados para persistência.

3. **Persistência – PostgreSQL**  
   - Os dados tratados são salvos em tabelas normalizadas em um banco relacional PostgreSQL.
   - A modelagem segue boas práticas de integridade referencial, pronta para uso por sistemas externos ou pipelines de ML.

4. **Lógica de Negócio – FastAPI + JWT**  
   - API construída com **FastAPI**, oferece endpoints segmentados e protegidos por **autenticação JWT**.
   - Estrutura modular, fácil de escalar e manter.

5. **Versionamento – GitHub**  
   - Todo o código está versionado em repositório Git, com organização por módulos (scraping, modelos, rotas, schemas, etc).

6. **Deploy – Render + Streamlit**  
   - O backend (API) é hospedado na **Render**.
   - O frontend é construído com **Streamlit**, fornecendo visualização interativa dos dados (gráficos, filtros, login, etc).


## 📁 Estrutura do Projeto

A estrutura do projeto foi organizada para garantir **modularidade**, **clareza** e **escalabilidade**:

```
VineEmprabaAPI/
│
├── api/
│   └── v1/
│       ├── endpoints/
│       │   ├── comercializacao.py
│       │   ├── exportacao.py
│       │   ├── importacao.py
│       │   ├── processamento.py
│       │   ├── producao.py
│       │   └── user.py
│       └── api.py
│
├── core/
│   ├── auth.py
│   ├── database.py
│   ├── deps.py
│   ├── security.py
│   └── settings.py
│
├── models/
│   ├── __all_models__.py
│   ├── comercializacao_model.py
│   ├── exportacao_model.py
│   ├── importacao_model.py
│   ├── processamento_model.py
│   ├── producao_model.py
│   └── user_model.py
│
├── process_data/
│   ├── comercializacao_clear.py
│   ├── exportacao_clear.py
│   ├── importacao_clear.py
│   ├── processamento_clear.py
│   ├── producao_clear.py
│   ├── web_scraping.py
│   ├── load_all.py
│   └── teste_scraping/
│
├── schemas/
│   ├── comercializacao_schema.py
│   ├── exportacao_schema.py
│   ├── importacao_schema.py
│   ├── processamento_schema.py
│   ├── producao_schema.py
│   └── user_schema.py
│
├── create_tables.py
├── main.py
├── requirements.txt
└── README.md
```

### 🔍 Organização por responsabilidades

- **api/**: Define os endpoints REST e o roteamento geral da API.
- **core/**: Contém configurações centrais, autenticação, dependências e segurança.
- **models/**: Define os modelos ORM (SQLAlchemy) correspondentes às tabelas no banco de dados.
- **schemas/**: Schemas Pydantic usados para validação e serialização de dados.
- **process_data/**: Scripts responsáveis por limpar, transformar e carregar os dados.
- **data_scraping/**: Pasta que armazenda os dados que foram extraídos via selenium e beatifulsoap .
- **main.py**: Ponto de entrada da aplicação FastAPI e também pela criaçao e persitencia das tabelas no banco de dados.
- **requirements.txt**: Lista de dependências do projeto.
  
---

## 🤖 Preparação para Machine Learning

A estrutura foi pensada para garantir:

- Consistência e padronização nos dados;
- Disponibilidade via API RESTful;
- Segurança com autenticação JWT;
- Facilidade de ingestão para pipelines de ML.

---


## 📊 Interface de Visualização

O projeto conta com um **frontend desenvolvido em Streamlit**, que permite:

- Login autenticado com token JWT
- Escolha da categoria (Produção, Importação, etc.)
- Filtros por ano, produto ou país
- Visualização por:
  - Tabela interativa
  - Gráficos de barras, linhas, top 5 e comparações
- Exportação dos dados filtrados em CSV, Excel ou JSON

### Exemplo da interface:

![Dashboard de Importação](<img width="1621" alt="image" src="https://github.com/user-attachments/assets/dd02279f-1adb-4146-9227-ceef4f411b4e" />
)

## 📈 Análise Exploratória dos Dados (EDA)

Antes de alimentar os dashboards e modelos de machine learning, foi realizada uma **Análise Exploratória de Dados (EDA)**, utilizando bibliotecas como `pandas`, `matplotlib` e `plotly`.

A EDA teve como objetivos principais:

- Verificar **distribuições temporais** (ex: volume de importação por ano)
- Identificar **outliers** e possíveis inconsistências
- Analisar **tendências por tipo de produto e país**
- Medir **ausência de dados** (valores nulos) e corrigir colunas incompletas
- Preparar os dados com agregações e filtros otimizados para os dashboards

### Exemplo de visualização da EDA:

![Gráfico de Importação - Quantidade por Ano](<img width="1621" alt="image" src="https://github.com/user-attachments/assets/a7f1e7ef-bd91-4c06-9b7d-a7372acc4b34" />)

Essas análises permitiram decisões fundamentadas sobre:
- Quais colunas manter e transformar
- Como estruturar os filtros no frontend
- E como garantir consistência dos dados entre os diferentes endpoints da API

## 📈 Análise Exploratória de Dados (EDA)

Antes da construção dos dashboards interativos e da preparação para Machine Learning, foi realizada uma **análise exploratória de dados (EDA)** com o objetivo de:

- Identificar padrões temporais (sazonalidade, tendências por ano);
- Verificar a distribuição dos dados por país e produto;
- Detectar dados faltantes, valores nulos ou inconsistentes;
- Avaliar correlações entre quantidade e valor por produto ou origem;
- Facilitar a definição de filtros úteis para visualização e modelagem futura.

### Exemplo de gráfico gerado durante a EDA:

![Gráfico EDA - Importação](<img width="1621" alt="image" src="https://github.com/user-attachments/assets/c059e397-bf89-4c44-a365-efeac74e60f6" />)


Esses insights orientaram:
- A escolha de filtros por **ano**, **produto** e **país**;
- A separação das abas no dashboard;
- A modelagem dos dados para futura análise preditiva e agrupamentos.

---

## 🧭 Endpoints Disponíveis

A API oferece múltiplos endpoints organizados por módulos, todos protegidos por autenticação JWT:

### 🔐 Autenticação & Usuários (`/api/v1/users`)
| Método | Rota             | Descrição                    |
|--------|------------------|-------------------------------|
| POST   | `/login`         | Login do usuário              |
| POST   | `/signup`        | Criação de novo usuário       |
| GET    | `/`              | Lista todos os usuários       |
| GET    | `/by-id/{user_id}` | Busca usuário por ID        |
| GET    | `/logado`        | Retorna usuário logado        |
| PUT    | `/{user_id}`     | Atualiza dados do usuário     |
| DELETE | `/{user_id}`     | Deleta usuário                |

### 🍇 Produção (`/api/v1/producoes`)
| Método | Rota                        | Descrição                   |
|--------|-----------------------------|------------------------------|
| GET    | `/`                         | Retorna todos os dados       |
| GET    | `/get_prod_ano_min_max`     | Retorna o menor e maior ano  |
| GET    | `/get_producao_by_ano`      | Produção agrupada por ano    |

### 🏭 Processamento (`/api/v1/processamentos`)
| Método | Rota                                | Descrição                   |
|--------|-------------------------------------|------------------------------|
| GET    | `/`                                 | Retorna todos os dados       |
| GET    | `/get_processamento_ano_min_max`    | Retorna o menor e maior ano  |

ℹ️ **Rotas de importação, exportação e comercialização seguem estrutura semelhante.**

### 🔑 Segurança
- Todas as rotas (exceto login e signup) exigem **autenticação via JWT Bearer Token**.
- Use o botão `"Authorize"` na documentação Swagger para testar os endpoints autenticados.

---

### 📦 Importação (`/api/v1/importacoes`)
| Método | Rota                        | Descrição                       |
|--------|-----------------------------|----------------------------------|
| GET    | `/`                         | Lista todos os dados de importação |
| GET    | `/get_importacao_ano_min_max` | Ano mínimo e máximo disponível   |
| GET    | `/get_importacao_by_ano`     | Importação agrupada por ano      |

### 🚢 Exportação (`/api/v1/exportacoes`)
| Método | Rota                        | Descrição                       |
|--------|-----------------------------|----------------------------------|
| GET    | `/`                         | Lista todos os dados de exportação |
| GET    | `/get_exportacao_ano_min_max` | Ano mínimo e máximo disponível   |
| GET    | `/get_exportacao_by_ano`     | Exportação agrupada por ano      |

### 🛒 Comercialização (`/api/v1/comercializacoes`)
| Método | Rota                              | Descrição                          |
|--------|-----------------------------------|-------------------------------------|
| GET    | `/`                               | Lista todos os dados de comercialização |
| GET    | `/get_comercializacao_ano_min_max`| Ano mínimo e máximo disponível       |
| GET    | `/get_comercializacao_by_ano`     | Comercialização agrupada por ano     |

---

## 🧪 Como testar a API

### 📘 Swagger UI
Acesse a [documentação interativa Swagger](https://techchallengeapi.onrender.com/docs) para testar cada rota diretamente no navegador.  
Use o botão **"Authorize"** para inserir o token JWT.

### 🧰 Exemplo de Login (via `curl`)
```bash
curl -X POST http://localhost:8000/api/v1/users/login \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "username=usuario@email.com&password=suasenha"
```

### 📤 Exemplo de resposta com token JWT
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI...",
  "token_type": "bearer"
}
```

### 🔐 Como usar o token
Copie o `access_token` retornado e inclua no cabeçalho das requisições autenticadas:

```http
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

### 🧪 Testando com Postman
1. Importe o link `/openapi.json` no Postman.
2. Configure o token em **Authorization > Bearer Token**.
3. Teste as rotas protegidas como `GET /producoes`.

---
