import customtkinter as ctk
import Backend

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

ctk.CTkLabel(janela, text="Público-alvo:").grid(row=2, column=0, padx=10, pady=5)
publico_alvo_entry = ctk.CTkEntry(janela)
publico_alvo_entry.grid(row=2, column=1, padx=10, pady=5)

ctk.CTkLabel(janela, text="Mensagem:").grid(row=3, column=0, padx=10, pady=5)
mensagem_entry = ctk.CTkTextbox(janela, height=200, width=200)
mensagem_entry.grid(row=3, column=1, padx=10, pady=5)

def coletar_dados():
    email = email_entry.get()
    senha = senha_entry.get()
    publico_alvo = publico_alvo_entry.get()
    mensagem = mensagem_entry.get("1.0", "end-1c")
    print("Email:", email, ", Senha:", senha, ", Público-alvo:", publico_alvo, ", Mensagem:", mensagem)

    Backend.iniciar_auto(email, senha, publico_alvo, mensagem)


iniciar_button = ctk.CTkButton(janela, text="Iniciar", command=coletar_dados, fg_color="#4C856A")
iniciar_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)


texto_placeholder = "Terminal:"
placeholder_entry = ctk.CTkTextbox(janela, height=300, width=300)
placeholder_entry.insert("1.0", texto_placeholder)
placeholder_entry.configure(state='disabled')  # Configura o CTkTextbox como somente leitura
placeholder_entry.grid(row=5, column=0, columnspan=2, padx=10, pady=5)


janela.mainloop()