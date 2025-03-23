# Pipeline ETL Python - Monitoramento de preços de Commodities com SQL e dbt-core (Data Warehouse)

## Como Usar

1. Execute o script de extração para coletar dados do Yahoo Finance:
```bash
python3 src/extract.py
```

2. Execute o script de carga para salvar os dados no PostgreSQL:
```bash
python3 src/load.py
```

3. Execute as transformações dbt:
```bash
cd dbcommodities
dbt run
```

## Estrutura de Dados

### Fonte de Dados
- Yahoo Finance API
- Commodities monitoradas:
  - CL=F (Petróleo Bruto)
  - GC=F (Ouro)
  - SI=F (Prata)

### Banco de Dados
- PostgreSQL no AWS RDS
- Tabela principal: `commodities`
  - Colunas:
    - Close: Preço de fechamento
    - ticker: Nome do ativo

### Transformações DBT
- Modelo bronze: Renomeia as colunas para português e realiza limpeza inicial dos dados

## Manutenção

- Os scripts podem ser executados diariamente para atualizar os preços
- O dbt deve ser executado após a carga dos dados para atualizar as transformações

## Contribuição

1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/AmazingFeature`)
3. Faça o Commit das suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Faça o Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.