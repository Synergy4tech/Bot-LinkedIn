#me lembrem de apagar os comentarios depois sksksksksksskskskskksksksksk
"""
termos a mudar:
navegador = driver
instancia = self

"""

from selenium import webdriver # Importa o webdriver do selenium todo mundo sabe, mas foda-se 

import time # Importa o time para dar um tempo entre as ações do bot

"""Aqui ele ja faz a chamada do chromedrive automaticamente, caso não tenha o chromedrive instalado, ele irá baixar automaticamente, ou seja não precisa instalar o chromedrive manualmente, o selenium faz isso automaticamente."""

#aqui para a instancia eu coloquei instancia, mas poderia ser qualquer coisa ta, mas eu coloquei instancia para ficar mais facil de entender

class Iniciar: #vou por classes para ficar mais facil para vcs entenderem 
    def __init__(instancia): 
        instancia.navegador = webdriver.Chrome() #inicia o webdriver 
        #instancia.navegador.maximize_window() #maximiza a janela do webdriver
        
    def open_site(instancia): #função para abrir o site
        time.sleep(2)
        instancia.navegador.get("https://www.linkedin.com/login")
        time.sleep(5)

    def email(instancia): #função para colocar o email
        email_entry = instancia.navegador.find_element('xpath', '//*[@id="username"]') #encontra o campo de email
        email_entry.send_keys("dsafdsfasd@gmail.com")

    def senha(instancia):
        senha_entry = instancia.navegador.find_element('xpath', '//*[@id="password"]')
        senha_entry.send_keys("asdasdasd")
        

bot = Iniciar() #inicia o bot
bot.open_site() #abre o site
bot.email() #coloca o email
bot.senha() #coloca a senha