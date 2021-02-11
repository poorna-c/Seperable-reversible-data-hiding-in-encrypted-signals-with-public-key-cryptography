from functions import read_key, decrypt_key, decrypt_img

# Reading Encrypted Key
rsa_private_key = read_key('./keys/rsa_key.pem')

# Decrypting AES Key
key = decrypt_key(rsa_private_key,read_from_file='./keys/encrypted_key.aes')

# Decrypting Image
decrypt_img('img_encrypted.bin',key)