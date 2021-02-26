import os, random 
from Crypto.Cipher import AES 
from Crypto.Hash import SHA256 
    
def encrypt(key, filename): 
    chunk_size = 64*1024 
    output_file = filename+".enc" 
    file_size = str(os.path.getsize(filename)).zfill(16) 
    IV = '' 
    for i in range(16): 
        IV += chr(random.randint(0, 0xFF)) 
        print IV
    encryptor = AES.new(key, AES.MODE_CBC, IV) 
    with open(filename, 'rb') as inputfile:
        chunk = inputfile.read(chunk_size) 
        print 'CODE: '+encryptor.encrypt(chunk)
    print 'key: '+key

                
def getKey(password): 
    hasher = SHA256.new(password) 
    return hasher.digest() 
    

encrypt(getKey('karimamougay'), 'file.txt')
