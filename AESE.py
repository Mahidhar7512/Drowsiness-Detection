from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
from os import listdir
from os.path import isfile, join
import getpass

class Encryptor:
  def __init__(self, key):
      self.key = key

  def pad(self, s):
      return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

  def encrypt(self, message, key, key_size=256):
      message = self.pad(message)
      iv = Random.new().read(AES.block_size)
      cipher = AES.new(key, AES.MODE_CBC, iv)
      return iv + cipher.encrypt(message)
      
  def encrypt_file(self, file_name):
      with open(file_name, 'rb') as fo:
          plaintext = fo.read()
      enc = self.encrypt(plaintext, self.key)
      with open(file_name + ".enc", 'wb') as fo:
          fo.write(enc)
      os.remove(file_name)
      print("{} is encrypted!".format(file_name))

key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
enc = Encryptor(key)
os.chdir('D:\Drowsiness detection\CapturedImages')

patth = "D:\Drowsiness detection\CapturedImages\image"

f = open("D:\Drowsiness detection\count.txt", "r")
c = int(f.read())
f.close()

for i in range(1,c+1):
    enc.encrypt_file(patth+str(i)+".png")