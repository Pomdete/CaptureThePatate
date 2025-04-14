import json
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from Crypto.Hash import HMAC, SHA256

# Charger le contenu de output.txt
with open("output.txt", "r") as f:
    data = json.load(f)

iv = bytes.fromhex(data["iv"])
ciphertext = bytes.fromhex(data["c"])
expected_hmac = data["h"]

#Itérer ligne par ligne dans le fichier rockyou.txt
with open("rockyou.txt", "r", encoding="latin-1") as f:
    for line in f:
        # Enlever les espaces et les sauts de ligne
        password = line.strip()
        print(f"Essai : {password}")
        password_bytes = password.encode()
        
        # Vérifier le HMAC
        h = HMAC.new(password_bytes, digestmod=SHA256)
        h.update(b"FCSC2022")
        if h.hexdigest() == expected_hmac:
            print(f"Mot de passe trouvé : {password}")
            
            # Recréer la clé et déchiffrer
            key = SHA256.new(password_bytes).digest()
            cipher = AES.new(key, AES.MODE_CBC, iv)
            plaintext = unpad(cipher.decrypt(ciphertext), 16)
            
            print(f"Flag : {plaintext.decode()}")
            break
        else:
            print("Mot de passe non trouvé.")