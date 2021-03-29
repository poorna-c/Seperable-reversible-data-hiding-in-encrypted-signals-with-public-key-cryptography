import socket

HOST = '127.0.0.1'
PORT = 5555

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    with open('img_encrypted.bin','wb') as f:
        l = int(s.recv(20).decode('utf8'))
        print(l)
        d = s.recv(l)
        f.write(d)
        print("Recieved Encrypted Image")
    with open('encrypted_key.aes','wb') as f:
        # l = int(s.recv(1024).decode('utf8'))
        d = s.recv(256)
        f.write(d)
        print("Recieved AES Key...")
    with open('rsa_key.pem','wb') as f:
        l = int(s.recv(20))
        d = s.recv(l)
        f.write(d)
        print("Recieved Public Key...")