import random
try:
 inputs = int(random.randint(1,11111111))
except:
 print '[-] Err: Only Nambers!'
 exit()

def do(x):
 if len(str(x)) == 4 or len(str(x)) == 5 or len(str(x)) == 6:
   key = 'K'
 if len(str(x)) == 7 or len(str(x)) == 8 or len(str(x)) == 9:
   key = 'M'
 if len(str(x)) == 10 or len(str(x)) == 11 or len(str(x)) == 12:
   key = 'B'
 if len(str(x)) == 13 or len(str(x)) == 14 or len(str(x)) == 15:
   key = 'T'
 if len(str(x)) > 15:
   key = 'L'
   cut = slice(8)
   cut2 = 8

 if len(str(x)) == 4 or len(str(x)) == 7 or len(str(x)) == 10 or len(str(x)) == 13:
   cut = slice(1)
   cut2 = 1
 if len(str(x)) == 5 or len(str(x)) == 8 or len(str(x)) == 11 or len(str(x)) == 14:
   cut = slice(1+1)
   cut2 = 2
 if len(str(x)) == 6 or len(str(x)) == 9 or len(str(x)) == 12 or len(str(x)) == 15:
   cut = slice(1+2)
   cut2 = 3



 print str(x)[cut]+'.'+str(x)[slice(cut2,cut2+1)]+' '+key


do(inputs)
