import socket
HOST = '127.0.0.1'
PORT = 5555

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Connected with", addr)
        with open('img_encrypted.bin','rb') as f:
            conn.send(f.read())
        with open('keys/encrypted_key.aes','rb') as f:
            conn.send(f.read())
        with open('keys/rsa_key.pem','rb') as f:
            conn.send(f.read())
