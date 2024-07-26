from Cryptodome.Cipher import AES
import random
import string

class aes:
    def encryptAES256(self):
        data = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(16))
        key = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(32))
        iv = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(16))
        print("Raw Data: ",data)
        print("Key: ",key)
        print("IV: ",iv)
        #iv = b"61c48ca34d2d5082"
        cipher = AES.new(bytes(key,"utf-8"), AES.MODE_CBC, iv=bytes(iv,'UTF-8'))
        cipher_text = cipher.encrypt(bytes(self.pad(data),'UTF-8'))
        print("Data encrypted: ",cipher_text.hex())
        
    def pad (self,data):
        data = ' '*16 + data
        pad = 16 - len(data) % 16
        return data + pad * chr(pad)