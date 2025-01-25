import os
import pyaes
from tkinter import Tk, filedialog

# Função para selecionar o arquivo
def selecionar_arquivo():
    Tk().withdraw()  # Oculta a janela principal do Tkinter
    file_path = filedialog.askopenfilename(
        title="Selecione o arquivo para descriptografar",
        filetypes=[("Arquivos criptografados", "*.ransomwaretroll"), ("Todos os arquivos", "*.*")]
    )
    return file_path

# Seleciona o arquivo a ser descriptografado
file_name = selecionar_arquivo()

if file_name:  # Verifica se o usuário selecionou um arquivo
    try:
        # Abre o arquivo criptografado
        with open(file_name, "rb") as file:
            file_data = file.read()

        # Chave para descriptografia
        key = b"testeransomwares"
        aes = pyaes.AESModeOfOperationCTR(key)
        decrypt_data = aes.decrypt(file_data)

        # Remove o arquivo criptografado
        os.remove(file_name)

        # Cria o arquivo descriptografado
        new_file_name = file_name.replace(".ransomwaretroll", "")
        with open(new_file_name, "wb") as new_file:
            new_file.write(decrypt_data)

        print(f"Arquivo descriptografado com sucesso: {new_file_name}")
    except Exception as e:
        print(f"Erro ao descriptografar o arquivo: {e}")
else:
    print("Nenhum arquivo foi selecionado.")
