from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(executable_path=r'C:\Users\mauricio.gomes\Desktop\Aula_Python\chromedriver.exe')
driver.get('https://imoveisfranca.com.br/alugar')

while True:

    dados = driver.find_elements_by_xpath('//div[@class="infoThumb col-md-7 col-lg-8 col-sm-12"]')

    for dado in dados:
        try:
            bairro = dado.find_element_by_xpath('.//div[@class="thumb-titulo-nova"]').text
        except:
            pass
        try:
            tipo = dado.find_element_by_xpath('.//div[@class="thumb-tipo-nova ng-binding"]').text
        except:
            pass
        try:
            valor = dado.find_element_by_xpath('.//div[@class="locacao-nova-valor ng-binding"]').text
        except:
            pass
        try:
            dorm = dado.find_element_by_xpath('.//strong[@class="ng-binding"]').text
        except:
            pass
        print(bairro)
        print(tipo)
        print(valor)
        print("dormitórios: " + dorm)

    proximo = driver.find_element_by_xpath('//a[@ng-click="pag=pag+1;mudaPag(pag);alterarURL();"]')
    proximo.click()

    sleep(10)
