f = open ("emals.txt","r").read ()
h = [i for i in f.split() if "@" not in i]
for c in h:
    if len (c) == 32:
      print c