from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad,unpad

def GenerateKeys():
    rsa_key = RSA.generate(2048)
    encrypted_key = rsa_key.export_key()
    with open("./keys/rsa_key.pem", "wb") as f:
        f.write(encrypted_key)
    with open("./keys/pub_rsa_key.pem", "wb") as f:
        f.write(rsa_key.publickey().export_key())
    
    aes_key = b"mysecretpassword"

    return rsa_key, rsa_key.publickey(), aes_key

def encrypt_key(key,public_key,write_to_file=True):
    encryptor = PKCS1_OAEP.new(public_key)
    encrypted_key = encryptor.encrypt(key)
    if write_to_file:
        with open('./keys/encrypted_key.aes', 'wb') as f:
            f.write(encrypted_key)
    return encrypted_key

def decrypt_key(private_key, encrypted_key=None, read_from_file=None,):
    decryptor = PKCS1_OAEP.new(private_key)
    if read_from_file:
        with open(read_from_file,'rb') as f:
            encrypted_key = f.read()
    key = decryptor.decrypt(encrypted_key)
    return key

def encrypt_data(plaintext,aes_key, write_to_file=True):
    chiper = AES.new(aes_key,AES.MODE_CBC)
    chipertext = chiper.encrypt(pad(plaintext,AES.block_size))
    if write_to_file:
        with open('encrypted_data.bin','wb') as f:
            f.write(chiper.iv)
            f.write(chipertext)
    return chipertext,chiper.iv

def decrypt_data(aes_key, chipertext=None, iv=None, read_from_file=None):
    if read_from_file:
        with open(read_from_file,'rb') as f:
            iv = f.read(16)
            chipertext = f.read()
    chiper = AES.new(aes_key,AES.MODE_CBC,iv)
    return unpad(chiper.decrypt(chipertext),AES.block_size)

def encrypt_img(path,aes_key):
    with open(path,'rb') as f:
        img_data = f.read()
    chiper = AES.new(aes_key,AES.MODE_CBC)
    encrypted_image_data = chiper.encrypt(pad(img_data,AES.block_size))
    with open('img_encrypted.bin','wb') as f:
        f.write(chiper.iv)
        f.write(encrypted_image_data)


def decrypt_img(path,aes_key):
    with open(path,'rb') as f:
        iv = f.read(16)
        encrypted_image_data = f.read()
    chiper = AES.new(aes_key, AES.MODE_CBC,iv)
    img_data = unpad(chiper.decrypt(encrypted_image_data),AES.block_size)
    with open('img_decrypted.jpg','wb') as f:
        f.write(img_data)


def read_key(path):
    with open(path,'rb') as f:
        key = RSA.import_key(f.read())
    return key