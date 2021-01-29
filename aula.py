from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(executable_path=r'C:\Users\mauricio.gomes\Desktop\Aula_Python\chromedriver.exe')
driver.get('https://www.estantevirtual.com.br/estante')

texto = driver.find_element_by_name('q').send_keys("Guerra")
sleep(2)
clicar = driver.find_element_by_xpath('//i[@class="icon-search js-search"]')
clicar.click()

while True:

    dados = driver.find_elements_by_xpath('//a[@class="livro"]')

    for dado in dados:
        
        nome = dado.find_element_by_xpath('.//h2[@itemprop="name"]').text
        preco = dado.find_element_by_xpath('.//div[@class="precos"]').text  
        print(nome)
        print(preco)

    proximo = driver.find_element_by_xpath('//a[@aria-label="proxima"]')
    proximo.click()

    sleep(10)
