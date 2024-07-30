# -----------------------------------------------------------
# AES Class for data encryption/decryption
#
# (C) 2024 Ivan Gustavo Ortiz García
# Released under MIT License (MIT)
# GH Repository https://github.com/0zymandia5/encryption_with_python
# -----------------------------------------------------------

from creationalClasses.factory_aes import aes_CBC, aes_ECB, aes_CFB

class aes:
    """
        AES class for data encryption/decryption
        
        Attributes:
            modes [dict]\n
        Methods:
            encryptAES256(self, jsonSetup={}): Executes the AES data encryption for AES Mode such as CBC, ECB, CFB, etc.\n
    """
    
    modes = {
        "CBC": aes_CBC(),
        "ECB": aes_ECB(),
        "CFB": aes_CFB()
    }
    
    def encryptAES256(self, jsonSetup = {}):
        try:
            # Get Data from Json config
            mode = jsonSetup["mode"];
            data2Encrypt = jsonSetup["data2Encrypt"];
            #Instance of class needed
            dynamic_Klass = self.modes[mode];
            # Setup needed before to Encrypt
            dynamic_Klass.setMode(mode);
            dynamic_Klass.setKey();
            dynamic_Klass.setIV();
            # Encryption Process
            dynamic_Klass.printmode();
            dynamic_Klass.encrypt(data2Encrypt);
        except Exception as e: 
            print("Error at [jobs][encryptionClasses][encryptAES256].-");
            print(e);