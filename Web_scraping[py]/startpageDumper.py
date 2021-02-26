import urls
import sys
page = 0


try:
 cmax = int(input("Number Of Pages : "))
except:
 print "Please Only numbers here!!"
#what = "inurl+id%3D+ site+.pk"
for i in range(1,cmax+1):
  page += 1
  x = 'inurl php?id='+str(i)
  urls.search(x)
  sys.stdout.write("\r    [+] urlcount : %d  | page %d /%d max" % (len(urls.store),page,cmax))
  sys.stdout.flush()
  

print '\n\n'
fw = open(urls.sfile,'a')      
for i in urls.store:
  fw.write(i)
  fw.write('\n')

fw.close()

