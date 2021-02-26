import os

class b:
  bl = '\033[92m'
  en = '\033[0m'

room = []


num = input("Enter num of Folders u have: ")

while True:
 name = raw_input("Enter The Folder Name: ")
 room.append(name)
 num -= 1
 if num <=0:
   break


for put in room:
    sm = os.system("find / -name '"+put+"' >> find.log")


for i in open('find.log','r'):
    print b.bl+i+b.en
    
os.system("rm find.log")