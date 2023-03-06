# Ransomware

## Requisitos
- Python 3.6 ou superior
- Cryptography

## Como instalar
- Clone o repositório: 
```sh
git clone https://github.com/wellintonp/Ransomware.git
```
- Certifique-se de ter instalado o Python 3.6 ou superior em seu computador.
- Instale as dependências: 
```sh 
pip install -r requirements.txt
```

## Como usar
- Abra o arquivo main.py em um editor.
- Defina o caminho para o diretório que você deseja criptografar, substituindo ```directory_to_encrypt``` pela sua pasta desejada.
- Salve as alterações no arquivo.
- Abra o prompt de comando (no Windows) ou o terminal (no Linux/Mac).
- Navegue até o diretório onde o código está salvo.
- Execute o comando para criptografar todos os arquivos do diretório especificado:
```sh 
python main.py
```
- O código irá gerar automaticamente uma chave de descriptografia e salvá-la em um arquivo chamado thekey.key. Certifique-se de mantê-lo em um local seguro, pois é necessário para descriptografar os arquivos posteriormente.

## Nota: 
Este código pode ser perigoso se usado de maneira inadequada. Certifique-se de fazer backup dos arquivos antes de criptografá-los, pois a recuperação de arquivos criptografados pode ser difícil ou impossível em algumas situações.
