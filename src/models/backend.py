from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class start:
    """
    Classe para automatizar interações no LinkedIn.
    
    Attributes:
        email (str): E-mail usado para login.
        senha (str): Senha associada ao e-mail.
        publico_alvo (str): Termo de busca para encontrar conexões.
        mensagem (str): Mensagem personalizada a ser enviada.
        log_func (function): Função para registrar mensagens de log.
    """

    def __init__(self, email, senha, publico_alvo, mensagem, log_func):
        """
        Inicializa a classe start com os parâmetros necessários.

        Args:
            email (str): E-mail usado para login.
            senha (str): Senha associada ao e-mail.
            publico_alvo (str): Termo de busca para encontrar conexões.
            mensagem (str): Mensagem personalizada a ser enviada.
            log_func (function): Função para registrar mensagens de log.
        """
        self.driver = webdriver.Chrome()  
        self.email = email
        self.senha = senha
        self.publico_alvo = publico_alvo
        self.mensagem = mensagem
        self.log_func = log_func
        self.error_occurred = False  # Flag para rastrear erros

    def open_site(self):
        """
        Abre o site do LinkedIn no navegador.

        Raises:
            Exception: Se ocorrer um erro ao abrir o site.
        """
        self.log_func("Iniciando...")
        try:
            time.sleep(2)
            self.driver.get("https://www.linkedin.com/login")
            time.sleep(2)
            self.log_func("Site aberto com sucesso.")
        except Exception as e:
            self.log_func(f"Erro ao abrir o site.")
            self.error_occurred = True

    def do_login(self):
        """
        Realiza o login no LinkedIn com as credenciais fornecidas.

        Raises:
            Exception: Se ocorrer um erro ao fazer login.
        """
        if self.error_occurred:
            return
        
        try:
            email_entry = self.driver.find_element('xpath', '//*[@id="username"]')
            email_entry.send_keys(self.email)
            senha_entry = self.driver.find_element('xpath', '//*[@id="password"]')
            senha_entry.send_keys(self.senha)
            senha_entry.send_keys(Keys.RETURN)
            time.sleep(2)

            current_url = self.driver.current_url
            if "feed" in current_url:
                self.log_func("Login feito com sucesso.")
            else:
                self.log_func("Erro ao fazer login. Verifique suas credenciais.")
                self.error_occurred = True

        except Exception as e:
            self.log_func(f"Erro ao fazer login")
            self.error_occurred = True

    def search_targets(self):
        """
        Busca por conexões relacionadas ao público-alvo e envia mensagens.

        Raises:
            Exception: Se ocorrer um erro ao procurar alvos ou enviar mensagens.
        """
        if self.error_occurred:
            return
        
        try:
            box = self.driver.find_element('xpath', "//input[contains(@class, 'search-global-typeahead__input')]")
            box.send_keys(self.publico_alvo)
            box.send_keys(Keys.RETURN)
            time.sleep(2)

            more= self.driver.find_element('xpath', '/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/div[2]/a')
            more.click()
            time.sleep(2)
            self.log_func("Alvos encontrados com sucesso")

            connections_list_xpath = "/html/body/div[5]/div[3]/div[2]/div/div[1]/main/div/div/div[2]/div/ul"
            connect_buttons = self.driver.find_elements('xpath', f"{connections_list_xpath}//button[contains(@class, 'artdeco-button--2')]")

            for index, button in enumerate(connect_buttons):
                try:
                    button.click()
                    time.sleep(2)

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

                    self.log_func(f"Mensagem enviada com sucesso para o alvo {index + 1}.")

                except Exception as e:
                    self.log_func(f"Erro ao processar o botão {index + 1}: {str(e)}")

        except Exception as e:
            self.log_func(f"Erro ao encontrar alvos")
            self.error_occurred = True

def start_auto(email, senha, publico_alvo, mensagem, log_func):
    """
    Função principal para iniciar a automação.

    Args:
        email (str): E-mail usado para login.
        senha (str): Senha associada ao e-mail.
        publico_alvo (str): Termo de busca para encontrar conexões.
        mensagem (str): Mensagem personalizada a ser enviada.
        log_func (function): Função para registrar mensagens de log.
    """
    bot = start(email, senha, publico_alvo, mensagem, log_func)
    bot.open_site()
    if not bot.error_occurred:
        bot.do_login()
        if not bot.error_occurred:
            bot.search_targets()

    log_func("Aplicação finalizada.")
