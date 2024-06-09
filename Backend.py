#me lembrem de apagar os comentarios depois sksksksksksskskskskksksksksk
"""
termos a mudar:
navegador = driver
instancia = self

"""

from selenium import webdriver # Importa o webdriver do selenium todo mundo sabe, mas foda-se 
from selenium.webdriver.common.keys import Keys # isso serve para conseguirmos dar o ENTER no campo da senha e logar
import time # Importa o time para dar um tempo entre as ações do bot

"""Aqui ele ja faz a chamada do chromedrive automaticamente, caso não tenha o chromedrive instalado, ele irá baixar automaticamente, ou seja não precisa instalar o chromedrive manualmente, o selenium faz isso automaticamente."""

#aqui para a instancia eu coloquei instancia, mas poderia ser qualquer coisa ta, mas eu coloquei instancia para ficar mais facil de entender

class Iniciar: #vou por classes para ficar mais facil para vcs entenderem 
    def __init__(instancia, email, senha, publico_alvo, mensagem): 
        instancia.navegador = webdriver.Chrome() #inicia o webdriver
        instancia.email = email
        instancia.senha = senha
        instancia.publico_alvo = publico_alvo
        instancia.mensagem = mensagem
        #instancia.navegador.maximize_window() #maximiza a janela do webdriver
        
    def open_site(instancia): #função para abrir o site
        time.sleep(2)
        instancia.navegador.get("https://www.linkedin.com/login")
        time.sleep(5)

    def fazer_login_link(instancia):
        email_entry = instancia.navegador.find_element('xpath', '//*[@id="username"]')
        email_entry.send_keys(instancia.email)
        senha_entry = instancia.navegador.find_element('xpath', '//*[@id="password"]')
        senha_entry.send_keys(instancia.senha)
        senha_entry.send_keys(Keys.RETURN)
        time.sleep(5)
    
    def procura_alvos(instancia):
        caixinha = instancia.navegador.find_element('xpath', "//input[contains(@class, 'search-global-typeahead__input')]")
        caixinha.send_keys(instancia.publico_alvo)
        caixinha.send_keys(Keys.RETURN)
        time.sleep(5)

    def mensagem_enviada(instancia):
        print() #isso é so pra n acusar erro na função embaixo
        


def iniciar_auto(email, senha, publico_alvo, mensagem):
    bot = Iniciar(email, senha, publico_alvo, mensagem)
    bot.open_site()
    bot.fazer_login_link()
    bot.procura_alvos()
    bot.mensagem_enviada()


