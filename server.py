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
            d = f.read()
            l = str(len(d)).ljust(20).encode('utf8')
            print(l)
            conn.send(l)
            conn.send(d)
            print("Sent Encrypted Image...")
        with open('encrypted_key.aes','rb') as f:
            d = f.read()
            conn.send(d)
            print("Sent AES Key...")
        with open('rsa_key.pem','rb') as f:
            d = f.read()
            print(len(d))
            l = str(len(d)).ljust(20).encode('utf8')
            conn.send(l)
            conn.send(d)
