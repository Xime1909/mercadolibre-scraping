import scraper
from database.database_controller import insertar_carro,cerrar_conexion

#Funcion para separar el texto que tomamos desde la pagina web en una lista
def separar_info(carro):
    nuevo_carro = carro.text.split('\n')
    return nuevo_carro


#-------------------------------------------------------Ejecución principal-----------------------------------------------

scraper.abrir_pagina()

#en el buscadro escribe 'carros'
scraper.buscar_carros()

#le da click donde dice 'Chevrolet'
scraper.elegir_marca()

#Click donde dice 'SparkGt'
scraper.elegir_modelo()

#Toma la lista de resultados de la primera pagina
carros = scraper.obtener_carros()

#cerrar el browser
scraper.cerrar_pagina()

carros_listas = []

#separamos el texto de todos los carros en listas
for carro in carros:
    carros_listas.append(separar_info(carro))

#ingresamos los carros a la base de datos
for carro in carros_listas:
    print('Insertando...')
    insertar_carro(marca=carro[5] if not None else '',
                   año= carro[3] if not None else 0,
                   precio = float(carro[2].replace('.','')) if not None else 0
                   )

#cerrar la conexion de la base de datos  
cerrar_conexion()






