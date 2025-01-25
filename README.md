Descriptografar e Criptografar Arquivos
Este repositório contém dois scripts Python para criptografar e descriptografar arquivos com criptografia AES (CTR mode). Ambos os scripts agora incluem a funcionalidade para selecionar o arquivo a ser processado através de uma interface gráfica simples.

Funcionalidades
Criptografar Arquivo:

Permite ao usuário escolher um arquivo para criptografar com a chave AES.
O arquivo criptografado recebe a extensão .ransomwaretroll.
O arquivo original é removido após a criptografia.
Descriptografar Arquivo:

Permite ao usuário escolher um arquivo criptografado .ransomwaretroll para descriptografar.
O arquivo descriptografado é criado com o mesmo nome do arquivo original, mas sem a extensão .ransomwaretroll.
O arquivo criptografado é removido após a descriptografia.
Requisitos
Python 3.x
Bibliotecas:
pyaes
tkinter (para a interface gráfica)
Instalação das dependências:
bash
Copy
Edit
pip install pyaes
Nota: O tkinter geralmente já está incluído na instalação padrão do Python.

Como Usar
1. Criptografar Arquivo:
Execute o script encrypt.py.
Escolha o arquivo que deseja criptografar usando o diálogo gráfico.
O arquivo original será removido e um arquivo criptografado com a extensão .ransomwaretroll será gerado.
2. Descriptografar Arquivo:
Execute o script decrypt.py.
Escolha o arquivo criptografado com a extensão .ransomwaretroll usando o diálogo gráfico.
O arquivo descriptografado será gerado e o arquivo criptografado será removido.
Mudanças Realizadas
Seleção de Arquivos: Agora, os scripts permitem que o usuário selecione o arquivo a ser criptografado ou descriptografado através de um diálogo gráfico, utilizando o módulo tkinter.
Criptografia e Descriptografia: Ambos os scripts utilizam a biblioteca pyaes no modo AES CTR para criptografar e descriptografar arquivos.
Remoção e Criação de Arquivos: Após a criptografia ou descriptografia, o arquivo original é removido e um novo arquivo criptografado/descriptografado é gerado automaticamente.
Exemplo de Execução
Para criptografar um arquivo:

bash
Copy
Edit
python encrypt.py
Para descriptografar um arquivo:

bash
Copy
Edit
python decrypt.py
