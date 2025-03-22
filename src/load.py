# imports
import sqlalchemy
from sqlalchemy import create_engine
import psycopg2
from dotenv import load_dotenv
from extract import data_concat
import os

load_dotenv()

# Construir a string de conexão usando f-string
DB_URI = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

# salvar no postgres
def save_to_postgres(data, table_name):
    engine = create_engine(DB_URI)
    data.to_sql(table_name, engine, if_exists='append', index=False, schema='public')

if __name__ == '__main__':
    save_to_postgres(data_concat, 'commodities')
