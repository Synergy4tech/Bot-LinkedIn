from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time 

class Iniciar: 
    def __init__(self, email, senha, publico_alvo, mensagem): 
        self.driver = webdriver.Chrome() 
        self.email = email
        self.senha = senha
        self.publico_alvo = publico_alvo
        self.mensagem = mensagem
        
    def open_site(self): 
        time.sleep(2)
        self.driver.get("https://www.linkedin.com/login")
        time.sleep(2)

    def fazer_login_link(self):
        email_entry = self.driver.find_element('xpath', '//*[@id="username"]')
        email_entry.send_keys(self.email)
        senha_entry = self.driver.find_element('xpath', '//*[@id="password"]')
        senha_entry.send_keys(self.senha)
        senha_entry.send_keys(Keys.RETURN)
        time.sleep(2)
    
    def procura_alvos(self):
        caixinha = self.driver.find_element('xpath', "//input[contains(@class, 'search-global-typeahead__input')]")
        caixinha.send_keys(self.publico_alvo)
        caixinha.send_keys(Keys.RETURN)
        time.sleep(2)
        mais = self.driver.find_element('xpath', '/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/div[2]/a')
        mais.click()
        time.sleep(2)
        # Identificar a lista de conexões
        connections_list_xpath = "/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/ul"
        # Pegar todos os botões de conectar na página
        connect_buttons = self.driver.find_elements('xpath', f"{connections_list_xpath}//button[contains(@class, 'artdeco-button--2')]")
        
        # Loop para clicar em cada botão de conectar e enviar uma mensagem
        for index, button in enumerate(connect_buttons):
            try:
                # Clicar no botão "Conectar"
                button.click()
                time.sleep(2)
                # Encontrar a caixa de mensagem e inserir a mensagem personalizada
                add_note_button = self.driver.find_element('xpath', '//button[@aria-label="Adicionar nota"]')
                add_note_button.click()
                time.sleep(1)

                message_box = self.driver.find_element('xpath', '//*[@id="custom-message"]')
                message_box.send_keys(self.mensagem)
                message_box.send_keys(Keys.RETURN)

                time.sleep(5)

                send_button = self.driver.find_element('xpath', '//button[@aria-label="Enviar convite"]')
                send_button.click()
                time.sleep(5)

            except Exception as e:
                print(f"Ocorreu um erro ao processar o botão {index + 1}: {e}")

        
def iniciar_auto(email, senha, publico_alvo, mensagem):
    bot = Iniciar(email, senha, publico_alvo, mensagem)
    bot.open_site()
    bot.fazer_login_link()
    bot.procura_alvos()