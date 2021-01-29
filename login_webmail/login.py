from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome(executable_path=r'C:\Users\mauricio.gomes\Desktop\Aula_Python\chromedriver.exe')
driver.get('http://webmail.acifranca.com.br/')

nome = driver.find_element_by_name('user').send_keys("mauricio.gomes@acifranca.com.br")
senha = driver.find_element_by_name('pass').send_keys("Mudar@123")
clicar = driver.find_element_by_xpath('//button[@name="login"]')
clicar.click()

sleep(2)

abrir = driver.find_element_by_xpath('//button[@id="launchActiveButton"]')
abrir.click()

sleep(2)

abrir_email = driver.find_element_by_xpath('//td[@class="subject"]')
abrir_email.click()

sleep(5)

download_drop = driver.find_element_by_xpath('//span[@class="attachment-size"]')
download_drop.click()