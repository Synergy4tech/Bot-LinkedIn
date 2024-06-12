import unittest
import time
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
    unittest.main();


class TestReadUser(unittest.TestCase):
    
    def setUp(self):
       
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()  
        self.driver.implicitly_wait(10) 
        
        #essa parte aqui não soube o que colocar. O link do linkedin serviria ?
        self.url = "http://exemplo.com/listar-usuarios"

    def test_read_user(self):
        
        self.driver.get(self.url)
        
        
        user_list = self.driver.find_elements_by_class_name("Wanderson")
        self.assertGreater(len(user_list), 0, "Nenhum usuário encontrado na lista.")
        
        
        user_list[0].click()
        
        
        user_details = self.driver.name("Wanderson")
        self.assertTrue(user_details.is_displayed(), "Página de detalhes do usuário não foi exibida.")

    def tearDown(self):
        
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()


class TestUpdateUser(unittest.TestCase):
    
    def setUp(self):
        # Configuração do WebDriver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()  
        self.driver.implicitly_wait(3)  
        
        
        self.url = ""

    def test_update_user(self):
        
        self.driver.get(self.url)
        
        #  campos do formulário de edição de usuário
        self.driver.find_element_by_id("nome").clear()
        self.driver.find_element_by_id("nome").send_keys("Novo Nome")
        
        # Enviar o formulário 
        self.driver.find_element_by_id("btn-atualizar-usuario").click()
        
        
        success_message = self.driver.find_element_by_id("Cliente encontrado").text
        self.assertEqual(success_message, "Usuário atualizado com sucesso!")

    def tearDown(self):
        
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()


class TestDeleteUser(unittest.TestCase):
    
    def setUp(self):
        
        self.driver = webdriver.Chrome()
        self.driver.maximize_window() 
        self.driver.implicitly_wait(10)  

        self.url = " "

    def test_delete_user(self):
       
        self.driver.get(self.url)
        
        
        user_list = self.driver.find_elements_by_class_name("Wanderson")
        self.assertGreater(len(user_list), 0, "Nenhum usuário encontrado na lista para exclusão.")

        delete_button = self.driver.find_element_by_css_selector("button.excluir-usuario")
        delete_button.click()
        
        
        confirmation_dialog = self.driver.switch_to.alert
        confirmation_dialog.accept()
        
        # checagem de exclusão
        success_message = self.driver.find_element_by_id("mensagem-sucesso").text
        self.assertEqual(success_message, "Usuário excluído com sucesso!") 

    def tearDown(self):
        # Fechar o navegador após o teste
        self.driver.quit()


class TestValidation(unittest.TestCase):
    
    def setUp(self):
        
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()  
        self.driver.implicitly_wait(5)  
        
       
        self.url = " "

    def test_required_fields_validation(self):
        
        self.driver.get(self.url)
        
        
        create_button = self.driver.find_element_by_id("btn-criar-usuario")
        create_button.click()
        
        
        error_messages = self.driver.find_elements_by_class_name("campo-obrigatorio-erro")
        self.assertGreater(len(error_messages), 0, "Mensagens de erro não foram exibidas para campos obrigatórios.")
        
        # Verificar se os campos específicos têm mensagens de erro
        expected_errors = {
            "nome": "Campo obrigatório",
            "email": "Campo obrigatório",
            "senha": "Campo obrigatório"
        }
        for field, expected_error in expected_errors.items():
            field_error = self.driver.find_element_by_id(f"{field}-erro").text
            self.assertEqual(field_error, expected_error, f"Mensagem de erro incorreta para o campo {field}.")

    def tearDown(self):
        
        self.driver.quit()



class TestNavigation(unittest.TestCase):
    
    def setUp(self):
        
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()  
        self.driver.implicitly_wait(3)  
        
        
        self.url = "http://exemplo.com/"

    def test_page_navigation(self):
       
        self.driver.get(self.url)
        
        
        login_link = self.driver.find_element_by_link_text(" ")
        login_link.click()
        
        # Verificar se a URL foi redirecionada corretamente para a página de login
        self.assertEqual(self.driver.current_url, " ")

    def tearDown(self):
       
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()


class TestPerformance(unittest.TestCase):
    
    def setUp(self):
        
        self.driver = webdriver.Chrome()
        
        
        
        self.url = " "

    def test_page_loading_time(self):
        
        start_time = time.time()
        
        
        self.driver.get(self.url)
        
        #  o tempo final
        end_time = time.time()
        
        #  tempo de carregamento da página
        load_time = end_time - start_time
        
        # Verificar se o tempo de carregamento está dentro de um limite 
        self.assertLessEqual(load_time, 5, "Tempo de carregamento da página excedeu o limite de 5 segundos.")

    def tearDown(self):
        # Fechar o navegador após o teste
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

