# -*- coding: utf-8 -*- 
import random
import requests
import urllib
import os
from bs4 import BeautifulSoup as bs
import sys

proxies = {"http":"54.156.164.61:80",
"http":"161.35.50.98:3128",
"http":"161.35.130.184:8080",
"http":"03.84.27.209:8080",
"http":"206.81.2.118:1080",
"http":"161.35.114.60:8080",
"http":"157.245.222.183:80",
"http":"52.179.231.206:80",
"http":"38.91.100.171:3128",
"http":"104.196.135.23:80",
"http":"159.203.44.177:3128",
"http":"165.227.216.91:3128",
"http":"148.153.11.58:39593",
"http":"69.162.126.77:5836",
"http":"69.162.123.107:5836",
"http":"169.60.27.163:8080",
"http":"159.89.49.60:31264",
"http":"168.169.146.12:8080",
"http":"206.71.228.129:8841",
"http":"190.103.178.15:8080",
"http":"69.162.84.219:5836",
"http":"18.221.76.31:3128",
"http":"45.55.236.139:2244",
"http":"104.255.168.203:5836",
"http":"185.134.23.197:80",
"http":"104.255.170.175:5836",
"http":"185.134.23.198:80",
"http":"192.41.71.199:3128",
"http":"185.134.23.196:80",
"http":"192.34.62.163:3128",}

Utotal = input('\nHow Many Page U Need For Mining Urls : ')
print '\n'
Utour = 0
hits = 0
Utotal1 = Utotal
Utotal2 = Utotal
f = open('DATA_URL_SQL_DUMP','w')
f.write('[Cleaned] Url DATA_URL_SQL_DUMP :\n')
while not Utotal1 < 1 :


  ran = random.randint(140,33294)
  Ulink = 'https://www.google.com/search?q=inurl+%2Fshop%2Fproduct.php+id%3D'+str(ran)
  Utotal1 -= 1
  Ureq = requests.get(Ulink,proxies=proxies)
  bs4 = bs(Ureq.text,'lxml')
  le = len(bs4.find_all('a'))
  for i in range(le):
     if 'url?q=' in urllib.unquote(bs4.find_all('a')[i]['href']):
        Usplit = urllib.unquote(bs4.find_all('a')[i]['href']).split('q=')[1].split('&')
        if 'id=' in Usplit[0]:
	    hits += 1
            f = open('DATA_URL_SQL_DUMP','a')
            f.write('\n')
            f.write(Usplit[0])
  Utour += 1
  Upercent = str(int((float(Utour))/Utotal2*100))+'%'
  Presult = 30*Utour/Utotal2
  size = os.stat('DATA_URL_SQL_DUMP').st_size
  size2 = os.stat('DATA_URL_SQL_DUMP').st_size

  if len(str(size2)) == 1 or len(str(size2)) == 2 or len(str(size2)) == 3:
      key = 'B'
  if len(str(size2)) == 4 or len(str(size2)) == 5 or len(str(size2)) == 6:
      key = 'K'
  if len(str(size2)) == 7 or len(str(size2)) == 8 or len(str(size2)) == 9:
      key = 'M'
  if len(str(size2)) == 10 or len(str(size2)) == 11 or len(str(size2)) == 12:
      key = 'B'
  if len(str(size2)) == 13 or len(str(size2)) == 14 or len(str(size2)) == 15:
      key = 'T'
  if len(str(size2)) > 15:
      key = 'L'
      cut = slice(8)
      cut2 = 8

  if len(str(size2)) == 1 or len(str(size2)) == 4 or len(str(size2)) == 7 or len(str(size2)) == 10 or len(str(size2)) == 13:
      cut = slice(1)
      cut2 = 1 
  if len(str(size2)) == 2 or len(str(size2)) == 5 or len(str(size2)) == 8 or len(str(size2)) == 11 or len(str(size2)) == 14:
      cut = slice(1+1)
      cut2 = 2
  if len(str(size2)) == 3 or len(str(size2)) == 6 or len(str(size2)) == 9 or len(str(size2)) == 12 or len(str(size2)) == 15:
      cut = slice(1+2)
      cut2 = 3


  sys.stdout.write('\r'+'   '+Upercent+' '+'▓'*Presult+'░'*(30-Presult)+'    |    Hits : ['+str(hits)+']'+'     |      File Size : ['+str(size)[cut]+'.'+str(size)[slice(cut2,cut2+1)]+' '+key+']')
  sys.stdout.flush()

sys.stdout.write('\n')
     