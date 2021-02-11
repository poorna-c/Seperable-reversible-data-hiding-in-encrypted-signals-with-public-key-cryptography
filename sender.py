from functions import GenerateKeys, encrypt_img, encrypt_data, encrypt_key

# Generating Keys
rsa_private_key, rsa_public_key, aes_key = GenerateKeys()

# Encrypting Image and saving
encrypt_img('./Images/image.jpg',aes_key)

# Encrypting Image
encrypted_key = encrypt_key(aes_key,rsa_public_key)
