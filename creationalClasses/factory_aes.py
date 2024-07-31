# -----------------------------------------------------------
# Factory Creational class for AES encription
#
# (C) 2024 Ivan Gustavo Ortiz García
# Released under MIT License (MIT)
# GH Repository https://github.com/0zymandia5/encryption_with_python
# -----------------------------------------------------------
from Cryptodome.Cipher import AES
from Crypto.Util import Counter
from Crypto.Random import get_random_bytes
from abc import abstractmethod, property

import random
import string


class aes():
    """
        aes class for data encryption/decryption used as factory creation class pattern.       
            
        *Attributes:
            key [string] \n
            iv  [string] \n
            mode [string] \n
            counter [string] \n
            modes_aes [dict]

        *Methods:
            encrypt(self, data2Encrypt=""); \n
            setMode(self, mode_aes = ""); \n
            getMode(self); \n
            setKey(self); \n
            getKey(self); \n
            setIV(self); \n
            getIV(self); \n
            setCounter(self); \n
            getCounter(self)  \n
            pad(self,data)
    """
    key = "";
    iv = "";
    mode = "";
    counter = "";
    modes_aes = {
        "CBC": AES.MODE_CBC,
        "ECB": AES.MODE_ECB,
        "CFB": AES.MODE_CFB,
        "OFB": AES.MODE_OFB,
        "CTR": AES.MODE_CTR
    }
    
    @abstractmethod
    def encrypt(self, data2Encrypt = ""):
        try:
            print("Raw Data: ",data2Encrypt);
            print("Key: ",self.key);
            print("IV: ",self.iv);
            cipher = AES.new(bytes(self.key,"utf-8"), self.mode, iv=bytes(self.iv,'UTF-8'))
            cipher_text = cipher.encrypt(bytes(self.pad(data2Encrypt),'UTF-8'))
            print("Data encrypted: ",cipher_text.hex());
        except Exception as e: 
            print("Error at [creationalClasses][factory_aes][encrypt].-");
            print(e);
            
    @abstractmethod
    def setMode(self, mode_aes = ""):
        try:
            self.mode = self.modes_aes[mode_aes];
        except Exception as e: 
            print("Error at [creationalClasses][factory_aes][setMode].-");
            print(e);
    
    @abstractmethod
    def getMode(self) -> str:
        return self.mode;
    
    @abstractmethod
    def setKey(self):
        try:
            self.key = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(32));
        except Exception as e: 
            print("Error at [creationalClasses][factory_aes][setKey].-");
            print(e);
    
    
    @abstractmethod
    def getKey(self) -> str:
        return self.key
    
    @abstractmethod
    def setIV(self):
        try:
            self.iv = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(16))
        except Exception as e: 
            print("Error at [creationalClasses][factory_aes][setIV].-");
            print(e);
    
    @abstractmethod
    def getIV(self) -> str:
        return self.iv
    
    @abstractmethod
    def setCounter(self):
        try:
            nonce = get_random_bytes(8)
            self.counter = Counter.new(64, prefix=nonce)
        except Exception as e: 
            print("Error at [creationalClasses][factory_aes][setCounter].-");
            print(e);
    
    @abstractmethod
    def getCounter(self) -> bytes:
        return self.counter;
    
    @abstractmethod
    def pad (self,data):
        try:
            data = ' '*16 + data
            pad = 16 - len(data) % 16
            return data + pad * chr(pad)
        except Exception as e: 
            print("Error at [creationalClasses][factory_aes][pad].-");
            print(e);
            return "";
    
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

class aes_OFB(aes):
    #Output Feedback
    def printmode(self):
        print("Running Encryption AES 256 OFB");

class aes_CTR(aes):
    #Counter
    def printmode(self):
        print("Running Encryption AES 256 CTR");
    
    def encrypt(self, data2Encrypt = ""):
        print("Raw Data: ",data2Encrypt);
        print("Key: ",self.key);
        print("Counter: ",str(self.counter));
        cipher = AES.new(bytes(self.key,"utf-8"), self. mode,counter=self.counter)
        cipher_text = cipher.encrypt(bytes(self.pad(data2Encrypt),'UTF-8'))
        print("Data encrypted: ",cipher_text.hex())