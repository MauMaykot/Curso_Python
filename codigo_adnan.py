from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep


#driver = webdriver.Chrome(executable_path=r"/Users/macbook/python/chromedriver")
#driver.get('https://www.google.com/')

#meunome = driver.find_element_by_name('q').send_keys("Adnan Jebailey")
#sleep(2)
#clicar = driver.find_element_by_xpath('//input[@class="gNO89b"]')
#clicar.click()

## Parte 2 ##

driver = webdriver.Chrome(executable_path=r"/Users/macbook/python/chromedriver")
driver.get('https://www.estantevirtual.com.br/estante')

## Busca Única ##
#sleep(10)
#livro = driver.find_element_by_xpath('//li[@id="best-seller-5"]').text
#print(livro)

## Busca Agregada ##

#precios = driver.find_elements_by_xpath('//a[@class="busca-box m-group ga_tracking_event desktop"]')

#for precio in precios:
    #bairro = precio.find_element_by_xpath('.//h2[@class="busca-title"]').text  
    #print(bairro)

## Paginação ##


while True:

    precios = driver.find_elements_by_xpath('//a[@class="busca-box m-group ga_tracking_event desktop"]')
    
    for precio in precios:
        bairro = precio.find_element_by_xpath('.//h2[@class="busca-title"]').text  
        print(bairro)


    botao = driver.find_element_by_xpath('//a[@aria-label="próxima"]')
    botao.click()

    sleep(8)