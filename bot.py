

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

		#  1º Selecionar as bolinhas verdes do whatsapp
		bolinha = driver.find_element(By.CLASS_NAME, 'aumms1qt')
		bolinha = driver.find_elements(By.CLASS_NAME, 'aumms1qt')
		# Fim da correção
		clica_bolinha = bolinha[-1]  # Pega a última mensagem que chegou 
		acao_bolinha = webdriver.common.action_chains.ActionChains(driver)
		acao_bolinha.move_to_element_with_offset(clica_bolinha, 0 , -20)

		## 2º Chamar evento click duplo na bolinha verde do whatsapp
		acao_bolinha.click()
		acao_bolinha.perform()
		acao_bolinha.click()
		acao_bolinha.perform()
		

		## 3º Pegar o contato do cliente que enviou a msg do whatsapp
		telefone_cliente = driver.find_element(By.XPATH, '//*[@id="main"]/header/div[2]/div/div/span')
		telefone_final = telefone_cliente.text

		## 4º PEgar as mensagens do cliente (a última) do whatsapp
		todas_as_msg =  driver.find_elements(By.CLASS_NAME, '_1Gy50')
		#  São várias msg, mas só quero pegar a última
		todas_as_msg_texto = [e.text for e in todas_as_msg]
		msg = todas_as_msg_texto[-1]
		print(msg)


		# 5º Responder a mensagem:
		campo_de_texto = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
		campo_de_texto.click()
		time.sleep(2)

		campo_de_texto.send_keys('oi..isso é um teste. Favor não responder', Keys.ENTER)


		# 6º Fixar um contato padrão de retorno.
		contato_padrao = driver.find_elements(By.CLASS_NAME,'_2XH9R')
		acao_contato = webdriver.common.action_chains.ActionChains(driver)
		print('Algorítimo concluído. ')
		acao_contato.move_to_element_with_offset(contato_padrao,0,-20)
		acao_contato.click()
		acao_contato.perform()
		acao_contato.click()
		acao_contato.perform()



	except BaseException as err:
		print('buscando novas mensagens')
		time.sleep(3)



#executa a função acia
while True:
	bot()








