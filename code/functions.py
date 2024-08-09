# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# servico = Service(ChromeDriverManager().install())
# driver = webdriver.Chrome(service=servico)

import project as pj

def conversao_moeda (valor): # Função para converter um valor para real
    valor = f'{valor:,.2f}' # Formatando com divisor de milhares e separador de casas decimais
    valor = valor.replace(',', 'X').replace('.', ',').replace('X', '.') # Substituindo , por . e . por ,
    return valor

def extracao_texto (xpath):
    texto = pj.driver.find_element(By.XPATH, xpath).text
    return texto