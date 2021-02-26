# -*- coding: utf-8 -*-
import hashlib
import sys

#variables 
count = 0
tour  = 0
tourclone = 0
tourx = 0
creds = ''
part = 1
inputfilelines = 0

try:
 try:
   inputfile = sys.argv[1]
   dicfile = sys.argv[2]
   outputfile = sys.argv[3]
   fout = open(outputfile,'w')
   fouttx = '[+] inputfile: '+str(inputfile)+' DictionaryFile: '+str(dicfile)+' Outputfile: '+str(outputfile)+'\n'
   fout.write(fouttx)
 except:
   print 'err: Ex: python md5decoder.py inputfile(hashes).txt dic.txt outputfile(result).txt'
   sys.exit()
 print 'Text Content:'
 print '1)Hashes:Email'
 print '2)Email :Hashes'
 hashpos = input('input: ')
 if hashpos == 1:
     hashes = 0
     emails = 1
 if hashpos == 2:
     hashes = 1
     emails = 0
 if str(hashpos) not in '12':
     print '[-] err 1)Hashes:Email  !!'
     print '[-] err 2)Email :Hashes !!'
     sys.exit()

 inputfilelineslen = len(open(inputfile,'r').readlines())
 for i in range(0,inputfilelineslen): 
   if len(open(inputfile,'r').readlines()[i].split()) == 2:
        inputfilelines +=1
 dicfilelines  = len(open(dicfile,'r').readlines())
 
 print '\n'
 for i in open(inputfile,'r'):
  if len(i.split()) == 2:
   for ii in open(dicfile,'r'):
     hashtext = hashlib.md5(ii.split()[0]).hexdigest()
     prog1 = int(float(tour)/dicfilelines*100)
     if tourclone > inputfilelines:
        tourclone = 0
     prog2 = int(float(tourclone)/inputfilelines*100)
     sym1 = 10*tour/dicfilelines
     p1 = '▓'*sym1+'░'*(10-sym1)
     sym2 = 10*tourclone/inputfilelines
     p2 = '▓'*sym2+'░'*(10-sym2)
     prog3 = int(float(tourx)/inputfilelines*100)
     sym3 = 10*tourx/inputfilelines
     p3 = '▓'*sym3+'░'*(10-sym3)
     sys.stdout.write('\r     '+str(prog3)+'% ['+p3+'] '+str(prog1)+'% ['+p1+'] '+str(prog2)+'% ['+p2+'] count : '+str(count)+' tested: '+str(part)+'/'+str(inputfilelines)+' ')
     sys.stdout.flush()
     if i.split()[hashes] == hashtext:
       count += 1
       creds = str(i.split()[emails])+':'+str(ii.split()[0])
       fout = open(outputfile,'a')
       fout.write(creds)
     tourclone +=1
     tour += 1
     if tour > dicfilelines:
        tour = 0
   part +=1
   tourx +=1
     
 print '\n'  
except:
  pass