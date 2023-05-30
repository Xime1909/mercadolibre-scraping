import mysql.connector

# Conexión al contenedor de mysql que está corriendo local
connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="root",
    database="ml_scraping"
)

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS carro(
id INT AUTO_INCREMENT PRIMARY KEY,
marca VARCHAR(100),
anio INT,
valor FLOAT
);""")

connection.commit()




