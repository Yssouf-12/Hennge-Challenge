import time
import hmac
import hashlib
import struct
import base64
import requests
import json

def generate_totp(secret: str, digits=10, time_step=30, algo=hashlib.sha512):
    key = secret.encode()
    timestep = int(time.time() // time_step)
    message = struct.pack(">Q", timestep)
    hmac_hash = hmac.new(key, message, algo).digest()
    offset = hmac_hash[-1] & 0x0F
    code = struct.unpack(">I", hmac_hash[offset:offset + 4])[0] & 0x7FFFFFFF
    return str(code % (10 ** digits)).zfill(digits)

# === 1. Configuration ===
email = "yssoufouedraogo175@gmail.com"
secret = email + "HENNGECHALLENGE004"  # Secret partagé complet

# === 2. Générer mot de passe TOTP ===
totp_password = generate_totp(secret)

# === 3. Créer l'en-tête d'autorisation Basic ===
credentials = f"{email}:{totp_password}"
auth_header = base64.b64encode(credentials.encode()).decode()

# === 4. Construire les headers HTTP ===
headers = {
    "Authorization": f"Basic {auth_header}",
    "Content-Type": "application/json",
    "Accept": "*/*"
}

# === 5. Construire le JSON de soumission ===
payload = {
    "github_url": "https://gist.github.com/Yssouf-12/97174040e8bfc839f5900f0cd773220f",
    "contact_email": "yssoufouedraogo175@gmail.com",
    "solution_language": "python"
}

# === 6. Faire la requête POST ===
url = "https://api.challenge.hennge.com/challenges/backend-recursion/004"
response = requests.post(url, headers=headers, data=json.dumps(payload))

# === 7. Afficher le résultat ===
print("Status Code:", response.status_code)
print("Response:", response.text)
print("response: ", response)
