import hashlib
import random
from base64 import b64encode
from datetime import datetime, timedelta

def generate_salted_hash(password, salt):
    if password is None:
        password=''
    text = password+salt
    return b64encode(hashlib.sha256(text.encode()).digest()).decode("utf-8") 
    
def get_salt():
    salt = []
    for i in range(32):
        salt.append(random.randrange(1,255))
    return b64encode(bytearray(salt)).decode("utf-8") 
    
def getIntDate(date):
    t0 = datetime(1970, 1, 1)
    if date == None:
        return 0
    seconds = (date - t0).total_seconds()
    return int(seconds*1000)
    
def convertToDate(time):
    t0 = datetime(1970, 1, 1)
    dt = timedelta(seconds=int(time)/1000)
    return t0+dt