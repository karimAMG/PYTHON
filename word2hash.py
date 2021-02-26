# -*- coding: utf-8 -*-
import hashlib as md5
import sys

try:
    #var
    count = 0
    dicmax = 0
    dicfile = sys.argv[1]
    hashfile = 'word2hash.txt'

    for dicm in open(dicfile,'r'):
        dicmax +=1

    def progress():
        global count
        count += 1
        per = int(float(count)/dicmax*100)
        preg = 10*count/dicmax
        sym = '▓'*preg+'░'*(10-preg)
        sys.stdout.write('\r  ['+sym+'] '+str(per)+'%')
        sys.stdout.flush
        
    for dicitem in open(dicfile,'r'):
        progress()
        try:
            hashed = md5.md5(dicitem.split()[0]).hexdigest()+':'+dicitem.split()[0]+'\n'
            f = open(hashfile,'w')
            f.write(hashed)
            f.close()
        except:
            pass  
    print '[+] '+dicfile+' Done!'
except:
  print 'python word2hash.py dic.txt'
