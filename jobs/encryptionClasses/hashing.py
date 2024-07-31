# -----------------------------------------------------------
# HAshing Class for data encryption/decryption
#
# (C) 2024 Ivan Gustavo Ortiz García
# Released under MIT License (MIT)
# GH Repository https://github.com/0zymandia5/encryption_with_python
# -----------------------------------------------------------

from creationalClasses.factory_hashing import hashing_SHA_256, hashing_MD5, hashing_SHA_1, hashing_SHA_512

class hashing:
    """
        hashing class for data encryption/decryption
        
        *Attributes:
            modes [dict]\n
        *Methods:
            encryptHashing(self, jsonSetup={}): Executes the Hashing data encryption for Hashing Mode such as SHA-256, MD5, SHA-1, etc.\n
    """
    
    modes = {
        "SHA-256": hashing_SHA_256(),
        "MD5": hashing_MD5(),
        "SHA-1": hashing_SHA_1(),
        "SHA-512": hashing_SHA_512()
    }
    
    def encryptHashing(self, jsonSetup = {}):
        try:
            # Get Data from Json config
            mode = jsonSetup["mode"];
            data2Encrypt = jsonSetup["data2Encrypt"];
            #Instance of class needed
            dynamic_Klass = self.modes[mode];
            # Setup needed before to Encrypt
            dynamic_Klass.setup_Hash_Instance();
            # Encryption Process
            dynamic_Klass.update_Data2Encrypt(data2Encrypt);
            print(f"Data Encrypted: {dynamic_Klass.get_Hexadecimal()}");
        except Exception as e: 
            print("Error at [jobs][encryptionClasses][encryptHashing].-");
            print(e);