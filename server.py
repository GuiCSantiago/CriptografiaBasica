import random
import socket

G = 13
N = 31
Y = random.randint(1, N)

serverPort = 1300
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(("192.168.25.205", serverPort))
serverSocket.listen(1)
print('The server is ready to receive')

connectionSocket, addr = serverSocket.accept()

# Recebe r1 do cliente
r1_bytes = connectionSocket.recv(4)
r1 = int.from_bytes(r1_bytes, byteorder='big')

# Calcula a chave de criptografia a partir de r1
key = pow(r1, Y, N)

# Calcula r2 e envia para o cliente
r2 = pow(G, Y, N)
bytes_r2 = r2.to_bytes(4, byteorder='big')
connectionSocket.send(bytes_r2)

# Recebe mensagem criptografada do cliente
encrypted_message = connectionSocket.recv(1024).decode()

# Descriptografa a mensagem
decrypted_message = ""
for letter in encrypted_message:
    decrypted_char = ord(letter) - key
    decrypted_message += chr(decrypted_char)

# Transforma em uppercase
uppercase_message = decrypted_message.upper()

# Criptografa novamente antes de enviar de volta ao cliente
encrypted_response = ""
for letter in uppercase_message:
    encrypted_char = ord(letter) + key
    encrypted_response += chr(encrypted_char)

# Envia a mensagem criptografada de volta para o cliente
connectionSocket.send(bytes(encrypted_response, "utf-8"))
connectionSocket.close()