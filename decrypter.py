# Importar os modulos
import os
import pyaes

# Abrir o arquivo criptografado
file_name = 'teste.txt.encrypt'
file = open(file_name, 'rb')
# Armazena conteudo do arquvi em memoria
file_data = file.read()
file.close

# Chave de descriptografia
key = b'0123456789abcdef'
aes = pyaes.AESModeOfOperationCTR(key)
decrypt_data = aes.decrypt(file_data)

# Remover o arquivo criptografado
os.remove(file_name)

# Criar um novo arquivo descriptografado
new_file = 'teste.txt'
new_file = open(f'{new_file}', 'wb')
new_file.write(decrypt_data)
new_file.close()
