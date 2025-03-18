import mysql.connector
from mysql.connector import Error

db_config = {"host": "localhost", "user": "root", "password": "", "database": "sra_tlp"}


def create_connection():
    try:
        conn = mysql.connector.connect(**db_config)
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
