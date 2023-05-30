from .database_connection import cursor,connection

def insertar_carro(marca,año,precio):
    cursor.execute(
        f"""INSERT INTO carro (marca, anio, valor)
        VALUES ('{marca}', {año}, {precio})"""
    )
    connection.commit()

def cerrar_conexion():
    cursor.close()
    connection.close()
    
   