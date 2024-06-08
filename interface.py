import customtkinter as ctk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



def iniciar():
    print("Iniciando...")

def coletar_dados():
    email = email_entry.get()
    senha = senha_entry.get()
    publico_alvo = publico_alvo_entry.get()
    mensagem = mensagem_entry.get()
    print("Email:", email)
    print("Senha:", senha)
    print("Público-alvo:", publico_alvo)
    print("Mensagem:", mensagem)
    iniciar_auto(email, senha, publico_alvo, mensagem)

def iniciar_auto(username, password):
    driver = webdriver.Chrome(executable_patch="path/to/chromedriver")
    driver.get("https://www.linkedin.com/login")

    email_element = driver.find_element(By.ID, "username")
    email_element.send_keys(username)
    password_element = driver.find_element(By.ID, "password")
    password_element.send_keys(password)
    password_element.send_keys(Keys.RETURN)

    time.sleep(10)

    search_box = driver.find_element(By.XPATH, "//input[contains(@class, 'search-global-typeahead__input')]")
    search_box.send_keys(publico_alvo) # type: ignore
    search_box.send_keys(Keys.RETURN)

    time.sleep(10)
    
    profiles = driver.find_elements(By.XPATH, "//a[@class='search-result__result-link ember-view']")
    for profile in profiles:
        profile.click()

        time.sleep(5)
        
        try:
            connect_button = driver.find_element(By.XPATH, "//button[contains(@class, 'pv-s-profile-actions--connect')]")
            connect_button.click()
            time.sleep(3)
            add_notas = driver.find_element(By.XPATH, "//button[@aria-label='Add a note']")
            add_notas.click()
            time.sleep(3)
            message_box = driver.find_element(By.XPATH, "//textarea[@name='message']")
            message_box.send_keys(mensagem) # type: ignore
            send_button = driver.find_element(By.XPATH, "//button[@aria-label='Send now']")
            send_button.click()
        except Exception as e:
            print("Erro ao conectar ao perfil:", e)
        driver.back()

        time.sleep(5)

    driver.quit()
            





janela = ctk.CTk()
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
janela.title("Bot-LinkedIn")
janela.iconbitmap("./assets/logo.ico")


ctk.CTkLabel(janela, text="Email:").grid(row=0, column=0, padx=10, pady=5)
email_entry = ctk.CTkEntry(janela)
email_entry.grid(row=0, column=1, padx=10, pady=5)

ctk.CTkLabel(janela, text="Senha:").grid(row=1, column=0, padx=10, pady=5)
senha_entry = ctk.CTkEntry(janela, show="*")
senha_entry.grid(row=1, column=1, padx=10, pady=5)

# Campo para o público-alvo
ctk.CTkLabel(janela, text="Público-alvo:").grid(row=2, column=0, padx=10, pady=5)
publico_alvo_entry = ctk.CTkEntry(janela)
publico_alvo_entry.grid(row=2, column=1, padx=10, pady=5)

# Campo para a mensagem
ctk.CTkLabel(janela, text="Mensagem:").grid(row=3, column=0, padx=10, pady=5)
mensagem_entry = ctk.CTkTextbox(janela, height=200, width=200) 
mensagem_entry.grid(row=3, column=1, padx=10, pady=5)

# Botão Iniciar
iniciar_button = ctk.CTkButton(janela, text="Iniciar", command=coletar_dados,  fg_color="#4C856A")
iniciar_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)


janela.mainloop()
