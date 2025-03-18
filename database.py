import mysql.connector

# Configurar conexão
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="sra_tlp",
)

cursor = conn.cursor()

# Testar conexão
cursor.execute("SHOW TABLES")
for tabela in cursor:
    print(tabela)

# Fechar conexão
cursor.close()
conn.close()
