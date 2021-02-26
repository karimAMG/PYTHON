import subprocess

nums = []

files  = subprocess.check_output('ls')

for i in files.lower().replace('720','').replace('480','').split('mp4'):
   try:
    nums.append(int(filter(str.isdigit,i)))
   except:
     pass

nums.sort()

end = max(nums)

for all in range(1,end):
   if all not in nums:
      print '['+str(all)+'] is Missing'
   
   else:
      print '[+] Good '+str(all)+'.mp4'
      
      

