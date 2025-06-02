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

  


