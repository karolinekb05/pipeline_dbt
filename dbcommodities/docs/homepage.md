{% docs __overview__ %}

# Pipeline de Dados de Commodities

## Visão Geral
Este projeto consiste em um pipeline de dados que coleta e transforma informações de preços de commodities do mercado financeiro. Os dados são obtidos através da API do Yahoo Finance, armazenados em um banco de dados PostgreSQL e transformados usando dbt.

## Arquitetura do Projeto

### Camadas de Dados
1. **Raw (Fonte)**
   - Dados brutos coletados do Yahoo Finance
   - Commodities monitoradas:
     - CL=F (Petróleo Bruto)
     - GC=F (Ouro)
     - SI=F (Prata)

2. **Bronze**
   - Primeira camada de transformação
   - Padronização de nomes de colunas
   - Limpeza inicial dos dados

### Fluxo de Dados
```mermaid
graph LR
    A[Yahoo Finance] --> B[Python/yfinance]
    B --> C[PostgreSQL]
    C --> D[dbt Bronze]
```

## Modelos DBT

### Bronze
- **script.sql**
  - Objetivo: Padronização inicial dos dados
  - Transformações:
    - Renomeação de colunas para português
    - Seleção das colunas relevantes
  - Colunas resultantes:
    - valor_fechamento (Close)
    - ticker (Nome do ativo)

## Fontes de Dados

### Tabela: commodities
- **Descrição**: Preços de fechamento diários das commodities
- **Atualização**: Diária
- **Colunas**:
  - `Close`: Preço de fechamento do ativo
  - `ticker`: Identificador da commodity

## Testes e Qualidade de Dados
- Verificação de valores nulos
- Validação de tipos de dados
- Consistência de nomes de colunas

## Manutenção e Operação
- **Frequência de Atualização**: Diária
- **Ordem de Execução**:
  1. Extração via Python (extract.py)
  2. Carga no PostgreSQL (load.py)
  3. Transformações dbt (dbt run)

## Contatos e Suporte
Para questões relacionadas a:
- **Pipeline de Dados**: [Seu Nome/Email]
- **Infraestrutura**: [Responsável/Email]
- **Dúvidas Gerais**: [Email de Suporte]

## Links Úteis
- [Documentação do dbt](https://docs.getdbt.com/)
- [Yahoo Finance API](https://pypi.org/project/yfinance/)
- [Repositório do Projeto](link-do-seu-repositorio)

{% enddocs %}