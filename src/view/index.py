import sys
sys.path.append("..")  # Fix the string conversion
import threading
import customtkinter as ctk
from models.backend import start_auto  # Fix the import statement

janela = ctk.CTk()
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")
janela.title("Bot-LinkedIn")
janela.iconbitmap("../assets/logo.ico")

def clear_terminal():
    """Limpa o conteúdo do terminal na interface."""
    placeholder_entry.configure(state='normal')
    placeholder_entry.delete("1.0", "end")
    placeholder_entry.insert("1.0", "Terminal:")
    placeholder_entry.configure(state='disabled')

def data_collection():
    """Coleta os dados da interface e inicia o bot em uma nova thread."""
    clear_terminal()

    email = email_entry.get()
    senha = senha_entry.get()
    publico_alvo = publico_alvo_entry.get()
    mensagem = mensagem_entry.get("1.0", "end-1c")

    # Altera a cor do botão ao ser clicado
    iniciar_button.configure(fg_color="#1155cc")

    # Desabilita o botão após o clique
    iniciar_button.configure(state='disabled')

    thread = threading.Thread(target=start_auto_thread, args=(email, senha, publico_alvo, mensagem, log_message, on_thread_complete))
    thread.start()

def start_auto_thread(email, senha, publico_alvo, mensagem, log_func, callback):
    """Função de thread para iniciar a automação."""
    try:
        start_auto(email, senha, publico_alvo, mensagem, log_func)
    finally:
        # Chama o callback quando a função terminar
        callback()

def log_message(message):
    """Adiciona uma mensagem ao terminal da interface."""
    placeholder_entry.configure(state='normal')
    placeholder_entry.insert("end", "\n" + message)
    placeholder_entry.see("end")
    placeholder_entry.configure(state='disabled')

def on_thread_complete():
    """Função callback chamada quando a thread é concluída."""
    # Reativa o botão
    iniciar_button.configure(state='normal')
    # Restaura a cor original do botão
    iniciar_button.configure(fg_color="#4C856A")

# Componentes da interface

ctk.CTkLabel(janela, text="Email:").grid(row=0, column=0, padx=10, pady=5)
email_entry = ctk.CTkEntry(janela)
email_entry.grid(row=0, column=1, padx=10, pady=5)

ctk.CTkLabel(janela, text="Senha:").grid(row=1, column=0, padx=10, pady=5)
senha_entry = ctk.CTkEntry(janela, show="*")
senha_entry.grid(row=1, column=1, padx=10, pady=5)

ctk.CTkLabel(janela, text="Público-alvo:").grid(row=2, column=0, padx=10, pady=5)
publico_alvo_entry = ctk.CTkEntry(janela)
publico_alvo_entry.grid(row=2, column=1, padx=10, pady=5)

ctk.CTkLabel(janela, text="Mensagem:").grid(row=3, column=0, padx=10, pady=5)
mensagem_entry = ctk.CTkTextbox(janela, height=200, width=200)
mensagem_entry.grid(row=3, column=1, padx=10, pady=5)

iniciar_button = ctk.CTkButton(janela, text="Iniciar", command=data_collection, fg_color="#4C856A")
iniciar_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

texto_placeholder = "Terminal:"
placeholder_entry = ctk.CTkTextbox(janela, height=300, width=300)
placeholder_entry.insert("1.0", texto_placeholder)
placeholder_entry.configure(state='disabled')
placeholder_entry.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

janela.mainloop()
