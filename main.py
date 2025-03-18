from fastapi import FastAPI
from datetime import datetime, timedelta
import mysql.connector

app = FastAPI()

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "sra_tlp",
}


@app.get("/")
def home():
    return {"Minha API esta no ar!"}


@app.get("/soma")
def soma(a: int, b: int, c: int):
    return {"resultado": a + b + c}


@app.get("/funcionarios/contratados")
def get_funcionarios_contratados():
    # Data de 30 dias atrás
    data_limite = (datetime.today() - timedelta(days=30)).strftime("%Y-%m-%d")

    # Conectar ao banco
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    # Consulta SQL para pegar funcionários contratados nos últimos 30 dias
    query = """
    SELECT * FROM funcionario 
    WHERE RA_ADMISSA >= %s
    ORDER BY RA_ADMISSA DESC
    """

    cursor.execute(query, (data_limite,))
    resultado = cursor.fetchall()

    # Fechar conexão
    cursor.close()
    conn.close()

    return {"funcionarios": resultado}
