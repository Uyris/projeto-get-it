import psycopg2
import os
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

# Pega a URL do banco
DATABASE_URL = os.getenv('DATABASE_URL')

# Conecta ao banco de dados Postgres (Neon)
con = psycopg2.connect(DATABASE_URL)

# Cria um cursor
cur = con.cursor()

# Remove a tabela se já existir
cur.execute("DROP TABLE IF EXISTS notes")

# Cria a tabela notes
sql = '''
CREATE TABLE notes (
    id SERIAL PRIMARY KEY,
    title TEXT,
    details TEXT,
    position INTEGER,
    color TEXT
)
'''
cur.execute(sql)

# Confirma as mudanças
con.commit()

# Fecha a conexão
con.close()

def get_connection():
    return psycopg2.connect(DATABASE_URL)
