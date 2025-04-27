from dotenv import load_dotenv
import os

# Carrega variáveis de ambiente do arquivo .env
load_dotenv('.env')

class Config:
    """Configurações globais da aplicação."""

    APP_SECRET = os.getenv("APP_SECRET")
    DATABASE_URL = os.getenv("DATABASE_URL")

config = Config()