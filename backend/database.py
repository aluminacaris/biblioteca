import psycopg2 as pg
from psycopg2 import Error
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
import os

load_dotenv()

def conn():
    try:
        pwd = os.getenv("DB_PASSWORD") 
        connect = pg.connect (

            user="postgres",
            password=pwd,
            host="127.0.0.1",
            port="5432",
            database="Abiblioteca",
            cursor_factory=RealDictCursor ) 

        print("conectado com sucesso")

        return connect

    except Error as e:
        print(f"ocorreu um erro ao tentar conectar no banci de dadis {e}")

def encerra_conn(connect):
    if connect:
        connect.close()