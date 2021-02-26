import os, random 
import Ceasar as c

def encrypt(filename): 
    chunk_size = 64*1024 
    output_file = filename+".enc" 
    file_size = str(os.path.getsize(filename)).zfill(16) 
    IV = '' 
    for i in range(16): 
        IV += chr(random.randint(0, 0xFF)) 
    with open(filename, 'rb') as inputfile: 
        with open(output_file, 'wb') as outf: 
            outf.write(file_size) 
            outf.write(IV) 
            while True: 
                chunk = inputfile.read(chunk_size) 
                if len(chunk) == 0: 
                    break 
                elif len(chunk) % 16 != 0: 
                    chunk += ' '*(16 - len(chunk)%16) 
                outf.write(c.encode(chunk)) 
    
def decrypt(filename): 
        chunk_size = 64*1024 
        output_file = filename[:-4] 
        with open(filename, 'rb') as inf: 
            filesize = long(inf.read(16)) 
            IV = inf.read(16)
            with open(output_file, 'wb') as outf: 
                while True: 
                    chunk = inf.read(chunk_size) 
                    if len(chunk)==0: 
                        break 
                    outf.write(c.decode(chunk)) 
                outf.truncate(filesize) 

    
def main(): 
    choice = raw_input("Select One of the following\n> 1. Encrypt \n> 2. Decrypt\n>>> ") 
    if choice == "1": 
        filename = raw_input("Enter the name of file to be encrypted >> ") 
        encrypt(filename) 
        print "Done!\n%s ==> %s"%(filename, filename+".enc") 
    elif choice == "2": 
        filename = raw_input("File to be decrypted > ") 
        decrypt(filename) 
        print "Done\n%s ==> %s"%(filename, filename[:-4]) 
    else: 
        print "No option Selected" 
    
if __name__ == "__main__": 
    main() 
