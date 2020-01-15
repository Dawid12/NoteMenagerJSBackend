import hashlib
import random
from base64 import b64encode

def generate_salted_hash(password, salt):
    text = password+salt
    return b64encode(hashlib.sha256(text.encode()).digest()).decode("utf-8") 
    
def get_salt():
    salt = []
    for i in range(32):
        salt.append(random.randrange(1,255))
    return b64encode(salt).decode("utf-8") 