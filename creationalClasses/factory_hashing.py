# -----------------------------------------------------------
# Factory Creational class for Hashing encription
#
# (C) 2024 Ivan Gustavo Ortiz García
# Released under MIT License (MIT)
# GH Repository https://github.com/0zymandia5/encryption_with_python
# -----------------------------------------------------------
import hashlib
from abc import abstractmethod

class hashing():
    """
        hashing class for data encryption/decryption used as factory creation class pattern.       
            
        *Attributes:
            key [string] \n

        *Methods:
            encrypt(self, data2Encrypt=""); \n
    """
    hashInstance = {}
    
    @abstractmethod
    def setup_Hash_Instance(self):
        self.hashInstance = {};
        
    @abstractmethod
    def update_Data2Encrypt(self, data2Encrypt = ""):
        data_bytes = data2Encrypt.encode()
        self.hashInstance.update(data_bytes)
        
    @abstractmethod
    def get_Hexadecimal(self, data2Encrypt = ""):
        return self.hashInstance.hexdigest()
        
class hashing_SHA_256(hashing):
    def setup_Hash_Instance(self):
        self.hashInstance = hashlib.sha256();

class hashing_MD5(hashing):
    def setup_Hash_Instance(self):
        self.hashInstance = hashlib.md5();

class hashing_SHA_1(hashing):
    def setup_Hash_Instance(self):
        self.hashInstance = hashlib.sha1();
        
class hashing_SHA_512(hashing):
    def setup_Hash_Instance(self):
        self.hashInstance = hashlib.sha512();