# -*- coding: utf-8 -*-
import requests
import sys
import json
import os

#url = 'https://www.videvo.net/videvo_files/converted/2015_01/preview/AMS__Big_Explosion.mov67018.webm'

try:
  print '  Start Over : 1'
  print '  Continue   : 2'
  choise = input('  Input : ')
  print '\n'
except:
  sys.exit()
  print '\n'
if choise == 1:
 try:
    tour = 0
    url = raw_input('Input URL Link Here : ')
    fn = raw_input('\nname Ur file ex: file.zip : ')
    print '\n'
    if 'http' not in url or url == '' or fn == '' or '.' not in fn :
       sys.exit()
    r = requests.get(url,stream=True,allow_redirects=True)
    if len(str(int(r.headers['content-length']))) == 1 or len(str(int(r.headers['content-length']))) == 2 or len(str(int(r.headers['content-length']))) == 3:
        key = 'B'
        zz = str(int(r.headers['content-length']))
    if len(str(int(r.headers['content-length']))) == 4 or len(str(int(r.headers['content-length']))) == 5 or len(str(int(r.headers['content-length']))) == 6:
        key = 'K'
        zz = str(int(r.headers['content-length'])/1024)
    if len(str(int(r.headers['content-length']))) == 7 or len(str(int(r.headers['content-length']))) == 8 or len(str(int(r.headers['content-length']))) == 9:
        key = 'M'
        zz = str(int(r.headers['content-length'])/1024/1024)
    if len(str(int(r.headers['content-length']))) == 10 or len(str(int(r.headers['content-length']))) == 11 or len(str(int(r.headers['content-length']))) == 12:
        key = 'G'
        zz = str(int(r.headers['content-length'])/1024/1024/1024)


    if len(str(int(r.headers['content-length']))) == 1 or len(str(int(r.headers['content-length']))) == 4 or len(str(int(r.headers['content-length']))) == 7 or len(str(int(r.headers['content-length']))) == 10 :
        cut = slice(1)
        cut2 = 1
    if len(str(int(r.headers['content-length']))) == 2 or len(str(int(r.headers['content-length']))) == 5 or len(str(int(r.headers['content-length']))) == 8 or len(str(int(r.headers['content-length']))) == 11 :
        cut = slice(1+1)
        cut2 = 2
    if len(str(int(r.headers['content-length']))) == 3 or len(str(int(r.headers['content-length']))) == 6 or len(str(int(r.headers['content-length']))) == 9 or len(str(int(r.headers['content-length']))) == 12 :
        cut = slice(1+2)
        cut2 = 3
    s = zz+'.'+str(int(r.headers['content-length']))[slice(cut2,cut2+1)]+' '+key
    f = open(fn,'wb')

    for i in r.iter_content(512):
          tour += len(i)
          nisba = str(int(float(tour)/int(r.headers['content-length'])*100))+'%'
          sym = 10*int(tour)/int(r.headers['content-length'])
          progress = '▓'*sym+'░'*(10-sym)
          if len(str(int(tour))) == 1 or len(str(int(tour))) == 2 or len(str(int(tour))) == 3:
               key = 'B'
               zzt = str(int(tour))
          if len(str(int(tour))) == 4 or len(str(int(tour))) == 5 or len(str(int(tour))) == 6:
               key = 'K'
               zzt = str(int(tour/1024))
          if len(str(int(tour))) == 7 or len(str(int(tour))) == 8 or len(str(int(tour))) == 9:
               key = 'M'
               zzt = str(int(tour/1024/1024))
          if len(str(int(tour))) == 10 or len(str(int(tour))) == 11 or len(str(int(tour))) == 12:
               key = 'G'
               zzt = str(int(tour/1024/1024/1024))


          if len(str(int(tour))) == 1 or len(str(int(tour))) == 4 or len(str(int(tour))) == 7 or len(str(int(tour))) == 10 :
               cut = slice(1)
               cut2 = 1
          if len(str(int(tour))) == 2 or len(str(int(tour))) == 5 or len(str(int(tour))) == 8 or len(str(int(tour))) == 11 :
               cut = slice(1+1)
               cut2 = 2
          if len(str(int(tour))) == 3 or len(str(int(tour))) == 6 or len(str(int(tour))) == 9 or len(str(int(tour))) == 12 :
               cut = slice(1+2)
               cut2 = 3
          k = zzt+'.'+str(int(tour))[slice(cut2,cut2+1)]+' '+key
          download = '  Downloading ...'
          if nisba == '100%':
	    download = '  Downloaded Successfully !\n\n'
          sys.stdout.write('\r              '+nisba+'  '+str(progress)+' | File Size : '+k+'/'+s+' | file name : '+fn+' | '+download)
          sys.stdout.flush()
          f.write(i)
 except:
    print '\n\n\n  [!] Download Paused\n'
    fx = open('data.txt','w')
    da = {}
    da['group1'] = []
    da['group1'].append({'cmaxlen':str(r.headers['content-length']),'tours':tour,'url':url,'file':fn})
    json.dump(da,fx)
    print '\n'
if choise == 2:
  try:
    fx = open('data.txt','r')
    da = json.load(fx)
    for ix in da['group1']:
      tour = int(ix['tours'])
      cm = int(ix['cmaxlen'])
      url = str(ix['url'])
      fn = str(ix['file'])
    ctinue = {'Range':'bytes=%s-' % tour}
    r = requests.get(url,headers=ctinue,stream=True,allow_redirects=True)
    if len(str(cm)) == 1 or len(str(cm)) == 2 or len(str(cm)) == 3:
        key = 'B'
        zz = str(cm)
    if len(str(cm)) == 4 or len(str(cm)) == 5 or len(str(cm)) == 6:
        key = 'K'
        zz = str(cm/1024)
    if len(str(cm)) == 7 or len(str(cm)) == 8 or len(str(cm)) == 9:
        key = 'M'
        zz = str(cm/1024/1024)
    if len(str(cm)) == 10 or len(str(cm)) == 11 or len(str(cm)) == 12:
        key = 'G'
        zz = str(cm/1024/1024/1024)


    if len(str(cm)) == 1 or len(str(cm)) == 4 or len(str(cm)) == 7 or len(str(cm)) == 10 :
        cut = slice(1)
        cut2 = 1
    if len(str(cm)) == 2 or len(str(cm)) == 5 or len(str(cm)) == 8 or len(str(cm)) == 11 :
        cut = slice(1+1)
        cut2 = 2
    if len(str(cm)) == 3 or len(str(cm)) == 6 or len(str(cm)) == 9 or len(str(cm)) == 12 :
        cut = slice(1+2)
        cut2 = 3
    s = zz+'.'+str(cm)[slice(cut2,cut2+1)]+' '+key
    f = open(fn,'ab')
    for i in r.iter_content(512):
          tour += len(i)
          nisba = str(int(float(tour)/int(cm)*100))+'%'
          sym = 10*int(tour)/int(cm)
          progress = '▓'*sym+'░'*(10-sym)
          if len(str(int(tour))) == 1 or len(str(int(tour))) == 2 or len(str(int(tour))) == 3:
               key = 'B'
               zzt = str(int(tour))
          if len(str(int(tour))) == 4 or len(str(int(tour))) == 5 or len(str(int(tour))) == 6:
               key = 'K'
               zzt = str(int(tour/1024))
          if len(str(int(tour))) == 7 or len(str(int(tour))) == 8 or len(str(int(tour))) == 9:
               key = 'M'
               zzt = str(int(tour/1024/1024))
          if len(str(int(tour))) == 10 or len(str(int(tour))) == 11 or len(str(int(tour))) == 12:
               key = 'G'
               zzt = str(int(tour/1024/1024/1024))


          if len(str(int(tour))) == 1 or len(str(int(tour))) == 4 or len(str(int(tour))) == 7 or len(str(int(tour))) == 10 :
               cut = slice(1)
               cut2 = 1
          if len(str(int(tour))) == 2 or len(str(int(tour))) == 5 or len(str(int(tour))) == 8 or len(str(int(tour))) == 11 :
               cut = slice(1+1)
               cut2 = 2
          if len(str(int(tour))) == 3 or len(str(int(tour))) == 6 or len(str(int(tour))) == 9 or len(str(int(tour))) == 12 :
               cut = slice(1+2)
               cut2 = 3
          k = zzt+'.'+str(int(tour))[slice(cut2,cut2+1)]+' '+key
          download = '  Downloading ...'
          if nisba == '100%':
	    download = '  Downloaded Successfully !\n\n'
	    try:
	      os.system('rm data.txt')
	    except:
	      sys.exit()
          sys.stdout.write('\r              '+nisba+'  '+str(progress)+' | File Size : '+k+'/'+s+' | file name : '+fn+' | '+download)
          sys.stdout.flush()
          f.write(i)
  except:
    print '\n\n\n  [!] Download Paused\n'
    fx = open('data.txt','w')
    da = {}
    da['group1'] = []
    da['group1'].append({'cmaxlen':cm,'tours':tour,'url':url,'file':fn})
    json.dump(da,fx)
    print '\n'
if str(choise) not in '12':
  print '\n\n\n  [-] err Respect the fllowing Inputs\n'