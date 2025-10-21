# pip install pyscopg2 dotenv streamlit fastapi uvicorn requests
import psycopg2
from dotenv import load_dotenv
import os

#Carregar variáveis do .env
load_dotenv()

params = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
}