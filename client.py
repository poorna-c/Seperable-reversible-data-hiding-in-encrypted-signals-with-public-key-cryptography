import socket

HOST = '127.0.0.1'
PORT = 5555

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    with open('img_encrypted1.bin','wb') as f:
        f.write(s.recv(10000))
    with open('encrypted_key1.aes','wb') as f:
        f.write(s.recv(10000))
    with open('rsa_key1.pem','wb') as f:
        f.write(s.recv(10000))