-- import
WITH source AS (
    SELECT "Close", ticker FROM {{ source('dbcommodities', 'commodities') }}
),

-- renamed
RENAMED AS (
    SELECT 
        "Close" AS valor_fechamento,
        ticker AS ticker
    FROM source
)

-- querys

SELECT * FROM RENAMED