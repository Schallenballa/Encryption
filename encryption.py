import urllib.request
from cryptography.fernet import Fernet
import base64
import time
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

msg = "";
f = open('key.txt','r')
password = f.read().encode()
while (msg != "exit"):
    msg=str(input('Enter your message : '))

    salt = b'salt_'
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())

    key = base64.urlsafe_b64encode(kdf.derive(password))
    urllib.request.urlopen
    msg=msg.encode()
    f = Fernet(key)
    msg=f.encrypt(msg)
    msg=str(msg)
    print("Message Sent!")
    b=urllib.request.urlopen('https://api.thingspeak.com/update?api_key=M0EFAIMXXCZPY7T8&field1='+msg)
    print("Reconnecting to server...")
    time.sleep(15);
    clearConsole();
