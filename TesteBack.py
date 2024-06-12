import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestCreateUser(unittest.TestCase):
    
    def setUp(self):
        # Configuração do WebDriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()  
        self.driver.implicitly_wait(10)  # Tempo de espera 
        
        # URL  de criação de usuário
        self.url = "http://exemplo.com/criar-usuario"

    def test_create_user(self):
        # página de criação de usuário
        self.driver.get(self.url)
        
        # Preencher os campos do formulário de criação de usuário
        self.driver.find_element_by_id("nome").send_keys("Wanderson")
        self.driver.find_element_by_id("email").send_keys("wansouza49@gmail.com")
        self.driver.find_element_by_id("senha").send_keys("@123Wanderson")
        
        # Enviar o formulário
        self.driver.find_element_by_id("btn-criar-usuario").click()
        
        # Verifica se  página  é exibida
        success_message = self.driver.find_element_by_id("mensagem-sucesso").text
        self.assertEqual(success_message, "Usuário criado com sucesso!")

    def tearDown(self):
        # Fecha o navegador 
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
