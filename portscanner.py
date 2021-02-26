# -*- coding: utf-8 -*-
import sys
import socket

#variables :
tour = 0
maxprog = 10
ports = []
p = ''
typ = ''
portcount = 0

#from user:
print '     Host IP Here'
print '1) 192.168.1.1'
print '2) Add'
choise = input('Input: ')
print '\n'
if choise == 2:
  ip = raw_input('Enter Host IP      : ')
  print '\n'
if choise == 1:
  ip = '192.168.1.1'
  print '\n'
print '     Maxtour ports Here'
print '1) 100'
print '2) Add'
choise = input('Input: ')
print '\n'
if choise == 2:
  maxtour = input('Enter Maxtour ports: ')
  print '\n'
if choise == 1:
  maxtour = 100
  print '\n'
# socket
for i in reversed(range(maxtour+1)):
  s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  # float(mintoor)/maxtour
  percent = int(float(tour)/maxtour*100)
  mptourmt = int(float(maxprog*tour)/maxtour)
  progress = '▓'*mptourmt+'░'*(maxprog-mptourmt)
  # 0 no err
  if s.connect_ex((ip,i)) == 0:
    ports.append(i)
    portcount += 1
    p = str(i)
    try:
      typ = '['+str(socket.getservbyport(int(p)))+']'
    except:
      typ = '[Unkown]'
  # End of tour:
  tour += 1
  if percent == 100:
    p = str(ports)
    typ = ''
  sys.stdout.write('\r           '+str(percent)+'% ['+str(progress)+']  |  [OK] Port: '+p+' '+str(typ)+' Open  |  Ports Count : '+str(portcount)+'  |  ports In Range: '+str(i))
print '\n'
for port in ports:
  try:
    typ = str(socket.getservbyport(port))
  except:
    typ = 'Unkown'
  print '[OK] Port: '+str(port)+" "*(len(str(maxtour))-len(str(port)))+' Open ['+typ+'] '
