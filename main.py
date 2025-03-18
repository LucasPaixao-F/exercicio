from fastapi import FastAPI
from database import create_connection  # Importando a função de conexão
import mysql.connector

app = FastAPI()


@app.get("/")
def home():
    return {"Minha API está no ar!"}


@app.get("/soma")
def soma(a: int, b: int, c: int):
    return {"resultado": a + b + c}


@app.get("/funcionarios/contratados")
def get_funcionarios_contratados():
    # Usando a função de conexão
    conn = create_connection()

    if conn:
        cursor = conn.cursor(dictionary=True)

        query = """
          SELECT * FROM sra_tlp.funcionarios 
          WHERE STR_TO_DATE(RA_ADMISSA, '%d/%m/%Y') >= CURDATE() - INTERVAL 30 DAY
          ORDER BY STR_TO_DATE(RA_ADMISSA, '%d/%m/%Y') ASC;
        """

        cursor.execute(query)
        resultado = cursor.fetchall()

        cursor.close()
        conn.close()

        return {"funcionarios": resultado}
    else:
        return {"erro": "Falha na conexão com o banco de dados"}
