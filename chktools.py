import sys
import commands
import os
import time



def touch():
  if os.path.isfile('names.txt') == False :
    os.system('> names.txt')
  else:
    pass
touch()
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
def clr():
   os.system('clear')
clr()

def wlc():
      f1 = open('names.txt','r')
      name1 = f1.readlines()
      name1 = name1[0].split('\n')[0]
      print col.RED+":: "+col.EN+col.LBB+"Welcome"+col.EN+" "+col.CRR+" "+name1+" "+col.EN
      print ''
      print col.RED+":: "+col.EN
      

def set1():
     f = open('names.txt','r')
     if len(f.readlines()) > 0:    
         wlc()
     else:
         name1 = raw_input("What's Your Name: ")
         f= open('names.txt','a')
         f.write(name1)
         f.write('\n')
         f.close()

set1()
def err():
  print col.RED+'Error:'+col.EN+col.GRY+' Somethin Went Wrong!'+col.EN
def rtype():
  tp = os.name
  if tp == "posix":
    print col.GBB+"[+]"+col.EN+col.GYY+" You are Using "+col.EN+col.GBB+"Linux"+col.EN

def chk1():
  try:
    if put == 1:
      clr()
      time.sleep(4)
      try:
        if sys.argv[1] == 'run':
            chk_system_commands()
        if sys.argv[1] == 'start':
            Request1()
      except:
        clr()
        usage()
  except:
    err()
    exit()

def chk2():
  try:
    if put == 2:
      clr()
      exit()
  except:
    err()
    exit()

def prs():
  flasm = 'http://www.nowrap.de/flasm.html '
  aircrack = '''
  wget https://download.aircrack-ng.org/aircrack-ng-1.4.tar.gz
  tar -zxvf aircrack-ng-1.4.tar.gz
  cd aircrack-ng-1.4
  autoreconf -i
  ./configure --with-experimental
  make
  make install 

  ----------OR------------
  git clone https://github.com/aircrack-ng/aircrack-ng
  cd aircrack-ng
  autoreconf -i
  ./configure --with-experimental
  make
  make install
  '''
  bootiso = '''
  git clone https://github.com/jsamr/bootiso.git
  $ cd bootiso/
  $ chmod +x bootiso 


  sudo bootiso -d /dev/sdb ~/Templates/eXternOS.iso  
  '''
  ftp = '''
  Direct ftp site -> http://ftp.gnu.org/gnu/inetutils/

  cd inetutils-1.9.4
  ./configure
  make
  sudo make install
  telnet x.x.x.x port
  '''
  python = 'python 2.6.7+ - http://python.org/download/'
  gcc = 'gcc 4.7.3+ - http://gcc.gnu.org/install/'
  cmake = 'cmake 2.8.9+ - http://www.cmake.org/cmake/help/install.html'
  pip = 'pip 1.2.1+ - http://pip.readthedocs.org/en/latest/installing.html'
  screenfetch = '''
  #installl
  mkdir ~/screenfetch
  cd ~/screenfetch
  wget -O screenfetch 'https://raw.github.com/KittyKatt/screenFetch/master/screenfetch-dev'
  chmod +x screenfetch
  sudo cp screenfetch /usr/local/bin

  '''
  print col.RED+":: "+col.EN
  print col.RED+":: "+col.EN
  print col.RED+":: "+col.EN+col.GYY+" Your Request Number :"+col.EN
  print col.RED+":: "+col.EN
  try:
    num = input(':: > ')
    clr()
    while num > 0:
     print col.RED+":: "+col.EN
     print col.RED+":: "+col.EN+col.GYY+" Please Type Ur Program Name : "+col.EN
     print col.RED+":: "+col.EN
     pr1 = input(':: > ')
     if pr1:
         clr()
         num -= 1
         f1 = open('names.txt','r')
         name1 = f1.readlines()
         name1 = name1[0].split('\n')[0]
         print col.YLL+pr1+col.EN
         print col.RED+"::"*40+col.EN
         print col.RED+":: "+col.EN
         print col.RED+":: "+col.EN+col.GGG+' Thank U '+col.EN+col.CRR+" "+name1+" "+col.EN+col.GGG+' For UR Trust'+col.EN
         print col.RED+":: "+col.EN
         print col.RED+":: "+col.EN
         print col.RED+":: "+col.EN+col.LLL+' Try Again : '+col.EN+col.RED+'left ['+str(num)+']'+col.EN
         
    
  except:
    f1 = open('names.txt','r')
    name1 = f1.readlines()
    name1 = name1[0].split('\n')[0]
    clr()
    print col.RED+'[-]Err'+col.EN+col.GRY+':'+col.EN+col.LBB+' Not Found! '+col.EN+col.CRR+" "+name1+" "+col.EN+col.LBB+' Please Try again!'+col.EN
def Request1():
    wlc()
    try:
      
      prs()
    except:
        err()

def chk_system_commands():
    a = ['flasm','aircrack-ng','python','gcc','cmake','pip','ftp','screenfetch','bootiso']

    b1 = 0
    for ib in a:
       if len(ib) > b1:
          b1 = len(ib)

    for i in a:
        fix = "command -v "+i
        status, output = commands.getstatusoutput(fix)
        if len(i) < b1:
            spc = int(b1 - len(i))
        if len(i) == b1:
           spc = 0
        if status == 0:  
           print col.GBBb+'[+]'+col.EN+col.BLL+' '+i+' '+col.EN+col.GBB+' '*spc+' [Installed ----%100]'+col.EN
        else:
           print col.REDb+'[-]'+col.EN+col.YLL+' '+i+' '+col.EN+col.RED+' '*spc+' [Not Installed]'+col.EN
def inp():
 clr()
 try:
   print col.GBBb+"[+]"+col.EN+col.GBB+" Python chktools.py "+sys.argv[1]+col.EN
 except:
   print col.REDb+"[-]"+col.EN+col.RED+" Python chktools.py ??????"+col.EN

def wait():
  time.sleep(2)
def usage():
   clr()
   print col.RED+":: "+col.EN+col.PLL+"Usage:"+col.EN
   print col.RED+":: "+col.EN
   print col.RED+":: "+col.EN+col.YLL+"Check Programs:"+col.EN
   print col.RED+":: "+col.EN
   print col.RED+":: "+col.EN+"  System~#> "+col.GBB+"python chktools.py run"+col.EN
   print col.RED+":: "+col.EN
   print col.RED+":: "+col.EN+col.YLL+"Install:"+col.EN
   print col.RED+":: "+col.EN
   print col.RED+":: "+col.EN+"  System~#> "+col.GBB+"python chktools.py start"+col.EN
   print col.RED+":: "+col.EN
   print col.RED+":: "+col.EN+col.YLL+"Creator:"+col.EN
   print col.RED+":: "+col.EN
   print col.RED+":: "+col.EN+col.GBB+"Autor"+col.EN+"    : "+col.GBB+"karim amougay"+col.EN
   print col.RED+":: "+col.EN+col.GYY+"github   : "+col.GYY+"https://github.com/karimAMG"+col.EN
   print col.RED+":: "+col.EN+col.BL+"Facebook"+col.EN+" : "+col.BL+"https://www.facebook.com/karim.amouglife"+col.EN
   
usage()
print col.RED+"::"*44+col.EN
print col.RED+":: "+col.EN+col.GYY+" Choose :"+col.EN
print col.RED+"::"+col.EN
print col.RED+":: "+col.EN+col.YLL+" 1./"+col.EN+col.BBB+"Start:"+col.EN
print col.RED+":: "+col.EN+col.YLL+" 2./"+col.EN+col.GRY+"Exit:"+col.EN
print ""
try:
  put = input(':: > ')
except:
  err()
  pass
chk2()
inp()
print col.RED+"::"+col.EN
wait()
print col.REDb+"::"+col.EN+col.GYY+" Processing Your Request: "+col.EN+str(put)
wait()
print col.RED+"::"+col.EN
wait()
print col.REDb+"::"+col.EN
wait()
print ""
rtype()
print ""
wait()
print col.REDb+"::"+col.EN
wait()
print col.RED+"::"+col.EN
wait()
print col.REDb	+":: "+col.EN
chk1()
 