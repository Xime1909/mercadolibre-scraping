# Documentación:  
Este programa abre la pagina web de mercado libre y busca los carros con marca chevrolet, luego filtra por SparkGt, toma los datos los separa y los guarda en una base de datos mysql montada en un contenedor de docker  

## Requisitos:
Python 3.10  
Docker o mysql directamente en la maquina

## Configuración

Instalamos los modulos de python requeridos  

>pip install -r requirements.txt  

>docker pull mysql  
>docker run --name mysql -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 -d mysql  

Luego entrar al cmd del contenedor y ejecutar mysql  

>mysql -u root -p root  

Creamos la base de datos    

>create database ml_scraping;  

## Ejecución  
>python main.py



