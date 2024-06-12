import unittest
from selenium import webdriver

class TestBrowserCompatibility(unittest.TestCase):
    
    def setUp(self):
        
        self.driver_chrome = webdriver.Chrome()
        self.driver_chrome.maximize_window()
        
        #  WebDriver para o Firefox
        self.driver_firefox = webdriver.Firefox()
        self.driver_firefox.maximize_window()

    #falta concluir
