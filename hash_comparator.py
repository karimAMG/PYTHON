# -*- coding: utf-8 -*-
import sys

try:
  #var
  btchashfile = sys.argv[1]
  databhashfile = sys.argv[2]
  count = 0
  found = 0
  maxdatab = 0
  Foutput = "hashed.txt"
  status = True
  print '[✇] Wait Processing ...'
  for i in open(databhashfile,'r'):
     maxdatab += 1
  print '[✔] Completed ...'
  for databitem in open(databhashfile,'r'):
    f = open(btchashfile,'r')
    if databitem.split()[0] in f.read():
       status = False
       s= databitem.split()[0]+'\n'
       hashed = open(Foutput,'a')
       hashed.write(s)
       found +=1
       hashed.close()
    per = int(float(count)/maxdatab*100+1)
    count +=1
    prog = 10*count/maxdatab
    sym = '▓'*prog+'░'*(10-prog)
    sys.stdout.write('\r ['+sym+'] '+str(per)+'%  Count : '+str(count))
  print '\n'
  if status == True:
    print '[X] Not found!'
  else:
    print 'found : '+str(found)+' | File : '+Foutput
except:
  print 'python crack.py btc_file database_file'
