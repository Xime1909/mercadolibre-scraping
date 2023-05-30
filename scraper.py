from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager
import sys

driver = webdriver.Chrome(ChromeDriverManager().install())



def abrir_pagina():
    driver.get('https://www.mercadolibre.com.co/')

#Buscar carros
def buscar_carros():
    try:
        input_area = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "cb1-edit"))
        )
        input_area.send_keys('carros')
        input_area.send_keys(Keys.ENTER)
    except Exception as e:
        print(e)
        driver.quit()
        sys.exit()

def elegir_marca():
    try:
        link_marca = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root-app"]/div/div[2]/aside/section/div[3]/ul/li[1]/a/span[1]'))
        ).click()
    except Exception as e:
        print(e)
        driver.quit()
        sys.exit()

def elegir_modelo():
    try:
        link_modelo = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root-app"]/div/div[2]/aside/section[2]/div[3]/ul/li[6]/a/span[1]'))
        ).click()
    except Exception as e:
        print(e)
        driver.quit()
        sys.exit()

def obtener_carros():
    try:
        carros_info = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'ui-search-layout__item'))
        )
        return carros_info
    except Exception as e:
        print(e)
        driver.quit()
        sys.exit()

def cerrar_pagina():
    driver.quit()

    

