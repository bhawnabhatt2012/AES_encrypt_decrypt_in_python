import base64
import Crypto
from Crypto import Random
from Crypto.Cipher import AES

key=b''
message="secretive msg"
Cipher = AES.new(key)
def pad(s):
    return s+((16-len(s)% 16)*'{')
def encrypt(plaintext):
    global Cipher,key
    return Cipher.encrypt(pad(plaintext))
def decrypt(Ciphertext):
    global Cipher
    dec=Cipher.decrpyt(c=Ciphertext).decode('utf-8')
    l=dec.count('{')
    return dec[:len(dec)-1]
print("message:",message)
encrypted = encrypt(message)
decrypted= decrypt(encrypted)
print("ENCRPYTED :",encrypted)
print("DECRYPTED :",decrypted)
