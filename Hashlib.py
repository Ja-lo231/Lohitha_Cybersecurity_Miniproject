import requests
import hashlib

# Assigning the GET URL response to response
response = requests.get("https://letsdefend.io/robots.txt")

if response.status_code == 200:
    file_content = response.text.encode()
    
    sha256_hash = hashlib.sha256()
    sha256_hash.update(file_content)
    
    sha256_value = sha256_hash.hexdigest()
    print(sha256_value)
