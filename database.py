from config import Config
import psycopg2
import os

# Conecta ao banco de dados Postgres (Neon)
con = psycopg2.connect(Config.DATABASE_URL)

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
    color TEXT,
    user_id TEXT
)
'''
cur.execute(sql)

# Confirma as mudanças
con.commit()

# Fecha a conexão
con.close()

def get_connection():
    return psycopg2.connect(Config.DATABASE_URL)
