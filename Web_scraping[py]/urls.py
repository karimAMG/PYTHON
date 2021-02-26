import requests
from bs4 import BeautifulSoup as bs
import sys
import urllib

# Variables
store = []
urlcount = 0
page = 0
sfile = "store.txt"
bhr = "\n"+"#"*10+"Start"+"#"*10+"\n\n"
ehr = "\n\n"+"#"*10+"End"+"#"*10+"\n\n"
url = "https://www.startpage.com/sp/search"

px = {
"http":"64.227.19.111:3128",
"http":"198.50.177.44:44699",
"http":"67.207.83.225:80",
"http":"149.56.1.48:8181",
"http":"70.35.213.226:4153",
"http":"72.10.97.201:8080",
"http":"167.99.156.77:8080",
"http":"168.169.146.12:8080",
"http":"168.169.96.2:8080",
"http":"51.161.116.223:3128",
"http":"205.202.38.126:8080",
"http":"38.142.63.146:31596",
"http":"50.205.119.150:32482",
"http":"52.249.208.188:9300",
"http":"201.149.34.167:8080",
"http":"83.96.237.121:80",
"http":"188.166.94.118:8080",
"http":"51.254.98.24:80",
"http":"192.109.165.162:80",
"http":"85.14.243.31:3128",
"http":"191.101.39.76:80",
"http":"148.251.160.242:80",
"http":"24.37.245.42:51056",
"http":"198.73.227.176:80",
"http":"74.56.229.191:4145",
"http":"81.169.225.85:3128",
"http":"206.189.22.139:8080",
"http":"185.134.23.197:80",
"http":"51.83.231.21:3128",
"http":"38.133.200.94:31596",
}

def search(what):
        global a,r
        data = "query="+what+"&abp=1&language=english&lui=english&cat=web&sc=G6PwDfDSE3aC20&abp=1"
        ldata = len(data)
        h1={
        'Host': 'www.startpage.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.startpage.com/',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': str(ldata),
        'Origin': 'https://www.startpage.com',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Sec-GPC': '1',
        }
        try:
          r = requests.post(url,proxies=px,headers=h1,data=data)
        except:
          pass
        a = bs(r.text,"html.parser")
        for i in range(len(a.find_all('a'))):
           try:
             if ("id=" in str(a.find_all('a')[i]["href"])): 
               if('query=inurl' not in str(a.find_all('a')[i]["href"]) ): 
                 if( not str(a.find_all('a')[i]["href"]) in store):
                   store.append(str(a.find_all('a')[i]["href"]))
                   urlcount +=1
                   # Disply results
                   #sys.stdout.write("\r    [+] urlcount : %d  | page %d" % (urlcount,page))
                   #sys.stdout.flush()
                 else:
                    pass
               else:
                    pass
             else:
                  pass
           except:
             pass


