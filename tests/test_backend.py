import pytest
from unittest.mock import MagicMock
from src.models.backend import start

@pytest.fixture
def mock_driver():
    # Cria um mock para o WebDriver
    mock = MagicMock()
    return mock

@pytest.fixture
def mock_log_func():
    # Cria um mock para a função de log
    return MagicMock()

def test_open_site_success(mock_driver, mock_log_func):
    # Testa o método open_site com sucesso
    bot = start("email_teste", "senha_teste", "Python Developer", "Mensagem de teste", mock_log_func)
    bot.driver = mock_driver
    mock_driver.get.return_value = None
    bot.open_site()
    mock_log_func.assert_any_call("Iniciando...")
    mock_log_func.assert_any_call("Site aberto com sucesso.")

def test_open_site_exception(mock_driver, mock_log_func):
    # Testa o método open_site lançando uma exceção
    bot = start("email_teste", "senha_teste", "Python Developer", "Mensagem de teste", mock_log_func)
    bot.driver = mock_driver
    mock_driver.get.side_effect = Exception("Erro ao abrir o site.")
    bot.open_site()
    mock_log_func.assert_any_call("Iniciando...")
    mock_log_func.assert_any_call("Erro ao abrir o site.")
    assert bot.error_occurred is True
 
def test_do_login_success(mock_driver, mock_log_func):
    # Testa o método do_login com sucesso
    bot = start("email_teste", "senha_teste", "Python Developer", "Mensagem de teste", mock_log_func)
    bot.driver = mock_driver
    mock_email_entry = MagicMock()
    mock_senha_entry = MagicMock()
    mock_driver.find_element.side_effect = [mock_email_entry, mock_senha_entry]
    mock_driver.current_url = "https://www.linkedin.com/feed"
    bot.do_login()
    mock_email_entry.send_keys.assert_called_with("email_teste")
    mock_senha_entry.send_keys.assert_any_call("senha_teste")
    mock_log_func.assert_any_call("Login feito com sucesso.")

def test_do_login_failure(mock_driver, mock_log_func):
    # Testa o método do_login com falha no login
    bot = start("email_teste", "senha_teste", "Python Developer", "Mensagem de teste", mock_log_func)
    bot.driver = mock_driver
    mock_email_entry = MagicMock()
    mock_senha_entry = MagicMock()
    mock_driver.find_element.side_effect = [mock_email_entry, mock_senha_entry]
    mock_driver.current_url = "https://www.linkedin.com/login"
    bot.do_login()
    mock_email_entry.send_keys.assert_called_with("email_teste")
    mock_senha_entry.send_keys.assert_any_call("senha_teste")
    mock_log_func.assert_any_call("Erro ao fazer login. Verifique suas credenciais.")
    assert bot.error_occurred is True

def test_do_login_exception(mock_driver, mock_log_func):
    # Testa o método do_login lançando uma exceção
    bot = start("email_teste", "senha_teste", "Python Developer", "Mensagem de teste", mock_log_func)
    bot.driver = mock_driver
    mock_driver.find_element.side_effect = Exception("Erro ao fazer login")
    bot.do_login()
    mock_log_func.assert_any_call("Erro ao fazer login")
    assert bot.error_occurred is True

def test_search_targets_success(mock_driver, mock_log_func):
    # Testa o método search_targets com sucesso
    bot = start("email_teste", "senha_teste", "Python Developer", "Mensagem de teste", mock_log_func)
    bot.driver = mock_driver
    mock_search_box = MagicMock()
    mock_more_button = MagicMock()
    mock_connect_buttons = [MagicMock() for _ in range(3)]
    mock_driver.find_element.side_effect = [mock_search_box, mock_more_button, mock_connect_buttons[0]]
    mock_driver.find_elements.return_value = mock_connect_buttons
    mock_note_button = MagicMock()
    mock_message_box = MagicMock()
    mock_send_button = MagicMock()
    mock_driver.find_element.side_effect = [mock_search_box, mock_more_button, mock_connect_buttons[0], mock_note_button, mock_message_box, mock_send_button, mock_connect_buttons[1], mock_note_button, mock_message_box, mock_send_button, mock_connect_buttons[2], mock_note_button, mock_message_box, mock_send_button]

    bot.search_targets()

    mock_search_box.send_keys.assert_any_call("Python Developer")
    mock_more_button.click.assert_called_once()
    for button in mock_connect_buttons:
        button.click.assert_called()
    mock_log_func.assert_any_call("Alvos encontrados com sucesso")
    mock_log_func.assert_any_call("Mensagem enviada com sucesso para o alvo 1.")
    mock_log_func.assert_any_call("Mensagem enviada com sucesso para o alvo 2.")
    mock_log_func.assert_any_call("Mensagem enviada com sucesso para o alvo 3.")

def test_search_targets_exception(mock_driver, mock_log_func):
    # Testa o método search_targets lançando uma exceção
    bot = start("email_teste", "senha_teste", "Python Developer", "Mensagem de teste", mock_log_func)
    bot.driver = mock_driver
    mock_driver.find_element.side_effect = Exception("Erro ao encontrar alvos")
    bot.search_targets()
    mock_log_func.assert_any_call("Erro ao encontrar alvos")
    assert bot.error_occurred is True
