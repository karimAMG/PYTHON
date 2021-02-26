import os
import sys
import random
import time
t1=time.time()
ran = str(random.randint(10,10000))


pcap = raw_input("Enter Name of pCAP file : ")
file = pcap+ran+".txt"
dic = raw_input("Enter Name of Dictionary File : ")
dic += ".txt"
pcap += ".cap"
#file = "cat.txt"
pol = "#"*80+"\n\n"

os.system("aircrack-ng %s -w %s -l %s " % (pcap,dic,file))
f = open(file,"a")
f.write("   : Password Found!");
f.write("\n");
f.write("\n");
f.write("%s"%pol);


t2 = time.time()
re = t2 - t1
s1 = re / 60
s2 = int(s1) / 60

a1 = str(s1)
a2 = str(s2)
f.write("-------====Seconds:====-------\n\n")
f.write(a1)
f.write(" : Minutes\n\n")
f.write(a2)
f.write(" :  Hours\n\n")
f.write("%s"%pol);
f.close();
os.system("aircrack-ng %s | grep -i 'wpa' >> %s " % (pcap,file))
#os.system("shutdown -h now")