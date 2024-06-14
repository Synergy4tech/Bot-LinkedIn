import unittest
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from unittest.mock import MagicMock
from Backend import iniciar_auto

class TestInit(unittest.TestCase):
    def test_init(Iniciar):
        # Dados de exemplo para inicialização
        email = "example@example.com"
        senha = "example_password"
        publico_alvo = "example_target"
        mensagem = "example_message"

        # Teste da inicialização
        instance = Iniciar(email, senha, publico_alvo, mensagem)

        # Verificação se os atributos foram definidos corretamente
        Iniciar.assertIsInstance(instance.driver, webdriver.Chrome)
        Iniciar.assertEqual(instance.email, email)
        Iniciar.assertEqual(instance.senha, senha)
        Iniciar.assertEqual(instance.publico_alvo, publico_alvo)
        Iniciar.assertEqual(instance.mensagem, mensagem)

if __name__ == '__main__':
    unittest.main()



class Iniciar(unittest.TestCase):
    def setUp(self):
        # Configuração do driver
        self.driver = webdriver.Chrome()

    def test_open_site(self):
        # Teste de abertura do site
        instance = Iniciar(email="example@example.com", senha="example_password", publico_alvo="example_target", mensagem="example_message")
        instance.open_site()

        # Verifica se o site foi aberto corretamente
        self.assertEqual(instance.driver.current_url, "https://www.linkedin.com/login")

    def tearDown(self):
        # Limpeza após o teste
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


class TestFazerLogin(unittest.TestCase):
    def setUp(self):
        # Configuração do driver
        self.driver = webdriver.Chrome()

    def test_fazer_login_link(self):
        # Teste de login
        instance =Iniciar(email="example@example.com", senha="example_password", publico_alvo="example_target", mensagem="example_message")
        instance.open_site()
        instance.fazer_login_link()

        # Verifica se o login foi feito corretamente
        self.assertIn("feed", instance.driver.current_url)

    def tearDown(self):
        # Limpeza após o teste
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()




class TestProcuraAlvos(unittest.TestCase):
    def setUp(self):
        # Configuração do driver
        self.driver = webdriver.Chrome()

    def test_procura_alvos(self):
        # Teste de procura de alvos
        instance =Iniciar(email="example@example.com", senha="example_password", publico_alvo="example_target", mensagem="example_message")
        instance.open_site()
        instance.fazer_login_link()
        instance.procura_alvos()

        
    def tearDown(self):
        # Limpeza após o teste
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()




class TestIniciarAuto(unittest.TestCase):
    def test_iniciar_auto(self):
        # Criar um objeto mock para a classe e seus métodos
        bot_mock = MagicMock(spec=Iniciar)
        bot_mock.open_site.return_value = None
        bot_mock.fazer_login_link.return_value = None
        bot_mock.procura_alvos.return_value = None

        # Chamar a função iniciar_auto com os argumentos necessários
        email = "example@example.com"
        senha = "example_password"
        publico_alvo = "example_target"
        mensagem = "example_message"
        iniciar_auto(email, senha, publico_alvo, mensagem)

        # Verificar se os métodos foram chamados corretamente
        bot_mock.open_site.assert_called_once()
        bot_mock.fazer_login_link.assert_called_once()
        bot_mock.procura_alvos.assert_called_once()

if __name__ == '__main__':
    unittest.main()



