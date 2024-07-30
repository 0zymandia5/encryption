# -----------------------------------------------------------
# Factory Creational class for AES encription
#
# (C) 2024 Ivan Gustavo Ortiz García
# Released under MIT License (MIT)
# GH Repository https://github.com/0zymandia5/encryption_with_python
# -----------------------------------------------------------
from Cryptodome.Cipher import AES
from abc import abstractmethod

import random
import string


class aes():
    
    key = "";
    iv = "";
    mode = "";
    modes_aes = {
        "CBC": AES.MODE_CBC,
        "ECB": AES.MODE_ECB,
        "CFB": AES.MODE_CFB
    }
    
    @abstractmethod
    def encrypt(self, data2Encrypt = ""):
        print("Raw Data: ",data2Encrypt);
        print("Key: ",self.key);
        print("IV: ",self.iv);
        cipher = AES.new(bytes(self.key,"utf-8"), self.mode, iv=bytes(self.iv,'UTF-8'))
        cipher_text = cipher.encrypt(bytes(self.pad(data2Encrypt),'UTF-8'))
        print("Data encrypted: ",cipher_text.hex())
    
    @abstractmethod
    def setMode(self, mode_aes = ""):
        self.mode = self.modes_aes[mode_aes];
    
    @abstractmethod
    def getMode(self) -> str:
        return self.mode;
    
    @abstractmethod
    def setKey(self):
        self.key = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(32))
    
    @abstractmethod
    def getKey(self) -> str:
        return self.key
    
    @abstractmethod
    def setIV(self):
        self.iv = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(16))
    
    @abstractmethod
    def getIV(self) -> str:
        return self.iv
    
    @abstractmethod
    def pad (self,data):
        data = ' '*16 + data
        pad = 16 - len(data) % 16
        return data + pad * chr(pad)
    
class aes_CBC(aes):
    def printmode(self):
        print("Running Encryption AES 256 CBC");
        
class aes_ECB(aes):
    #Electronic CodeBook
    def printmode(self):
        print("Running Encryption AES 256 ECB");
    
    def encrypt(self, data2Encrypt = ""):
        print("Raw Data: ",data2Encrypt);
        print("Key: ",self.key);
        cipher = AES.new(bytes(self.key,"utf-8"), self.mode)
        cipher_text = cipher.encrypt(bytes(self.pad(data2Encrypt),'UTF-8'))
        print("Data encrypted: ",cipher_text.hex())
    
class aes_CFB(aes):
    #Cipher FeedBack
    def printmode(self):
        print("Running Encryption AES 256 CFB");