Tech Challenge FASE 01 - API: Vitivinicultura da Embrapa - Curso Pós Tech - Machine Learning Engineering

Problema de negócio

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


# 📡 API de Dados da Vitivinicultura Brasileira

Este projeto tem como objetivo criar uma **API pública RESTful**, com autenticação via JWT, que realiza a extração, tratamento e disponibilização de dados da vitivinicultura brasileira. A API está pronta para alimentar modelos de Machine Learning, com dados estruturados e limpos, extraídos diretamente do site da Embrapa (Vitibrasil).

---

## 🧱 Arquitetura do Projeto

A seguir, apresentamos a arquitetura completa do sistema desenvolvido:

![Arquitetura do Projeto](./2a6086eb-49b9-49bc-8463-0672d3a49926.png)

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

---

## 🤖 Preparação para Machine Learning

A estrutura foi pensada para garantir:

- Consistência e padronização nos dados;
- Disponibilidade via API RESTful;
- Segurança com autenticação JWT;
- Facilidade de ingestão para pipelines de ML.

---

  
  


