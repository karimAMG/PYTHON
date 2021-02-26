import datetime
from playsound import playsound
import os



status = False
a =0
b =0
c =0
d =0
e =0
f =0
j =0
while not status:
  cur = datetime.datetime.now()
  if cur.day == 4 and cur.hour == 4 and cur.minute == 16 and cur.month == 5:
     a +=1
     if a < 2 :
       print cur.strftime("%Y-%m-%d %H:%M:%S")
       #playsound('1.wav')
       try:
	os.system('pkill smplayer')
       except:
	 pass
     
