import re

f1 = open('dic.txt','r')
f1readed = f1.read()

def isEnglish(msg):
    msg1 = ''.join(re.findall('[a-zA-Z\s]',msg))
    msgS = msg1.split()
    Wcount = 0
    for haha in msgS:
        for word in f1readed.split():
            if(word == haha.upper()):
                Wcount += 1
    p = int(Wcount/float(len(msgS))*100)
    if p >= 50:
        return True
    else:
        return False