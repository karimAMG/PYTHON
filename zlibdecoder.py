import zlib
import sys
import os

try:
  inputfile = sys.argv[1]
  outputfile = sys.argv[2]
except:
  print 'err: EX: Inputfile.bin Outputfile.o'
  sys.exit()
print '1) Encode\n'
print '2) Decode\n'
n = input('type here: ')
if str(n) not in '12':
  print 'err Enter the fllowing construction'
def encode(i,c,o):
  f = open(i,'rb').read()
  content =  zlib.compress(f,c)
  print '1) Save file\n2) Skip'
  if input('Input: ') == 1:
     fw = open(o,'wb')
     fw.write(content)
     print content
     print '\n[+] File Compressed '+str(o)

  else:
     pass
     print content
     print '\n[+] File Compressed '
def decode(i,o):
  f = open(i,'rb').read()
  content = zlib.decompress(f)
  print '1) Save file\n2) Skip'
  if input('Input: ') == 1:
     fw = open(o,'wb')
     fw.write(content)
     print content
     print '\n[+] File Decompressed '+str(o)
  else:
     pass
     print content
     print '\n[+] File Decompressed '
if n == 1:
   print '\n78 01 - No Compression/low\n78 9C - Default Compression\n78 DA - Best Compression'
   print '\n#define Z_NO_COMPRESSION         0\n#define Z_BEST_SPEED             1\n#define Z_BEST_COMPRESSION       9\n#define Z_DEFAULT_COMPRESSION  (-1)'
   comptype = input('\nEnter Type Of Compression Level from 1-9: ')
   encode(inputfile,comptype,outputfile)
if n == 2:
   decode(inputfile,outputfile)

