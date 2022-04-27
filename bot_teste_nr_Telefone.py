

# Iniício do projeto
# 1º Baixar o chromedriver e instalar na pasta do projeto( https://chromedriver.chromium.org/downloads)
# 2º instalar o selenium em c:\usuarios\meu usuário 
# 3º criar o programa .py e importar o selenium para manipular o driver(Testar se o navegador abre, se não abrir,
#  baixar outra versão do chromedriver). Se der erro de arquivo bloqieado, só alterar as propriedades do arq


import os
import sys
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests


driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
# Tempo para capturar o QR Code do Whatsapp
time.sleep(10)

def bot():
	try:    # Pega a coleção de  mensagens que chegaram(bolinha verde)

        ## Deu erro neste parte do código
		# bolinha  = driver.find_element_by_class_name('l7jjieqr')
		# bolinha  = driver.find_elements_by_class_name('l7jjieqr')

		# Aplicando a correção com  Novo código corrigido:
		# Precisou import o BY do Selenium e utilizar find_element(By.CLASS_NAME, name) 

		bolinha = driver.find_element(By.CLASS_NAME, 'aumms1qt')
		bolinha = driver.find_elements(By.CLASS_NAME, 'aumms1qt')
		# Fim da correção
		clica_bolinha = bolinha[-1]  # Pega a última mensagem que chegou 
		acao_bolinha = webdriver.common.action_chains.ActionChains(driver)
		acao_bolinha.move_to_element_with_offset(clica_bolinha, 0 , -20)
		## chamar evento click duplo
		#acao_bolinha.click()
		#acao_bolinha.perform()
		#acao_bolinha.click()
		#acao_bolinha.perform()
		
		print ('buscando o telefone 1 ')  #   '//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/div/section/div[1]/div[2]/div/span/span'
		nome = '//*[@id="app"]/div/div/div[2]/div[3]'
		telefone_cliente = driver.find_element(By.XPATH, nome)
		print(telefone_cliente.text)
		telefone_cliente = driver.find_elements(By.XPATH, nome)
		fone_cliente = telefone_cliente[-1]
		print(fone_cliente	)
			##      '//*[@id="app"]/div/div/div[2]/div[3]/span/div/span/div/div/section/div[1]/div[2]/div/span/span')
		#telefone_final = telefone_cliente.text


	except:
		print("saindo com erro....")
		



#executa a função acia
while True:
	bot()










