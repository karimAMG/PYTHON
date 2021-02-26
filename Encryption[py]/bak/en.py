import os
import random
import c
def encode(filename):
	fileSize = str(os.path.getsize(filename)).zfill(20)
	encFile = filename+'.enc'
	blockSize = 64*1024
	iva = ''
	for i in range(20):
		iva += chr(random.randint(0,0xff))
	with open(filename,'rb') as filein:
		with open(encFile,'wb') as fileout:
			fileout.write(fileSize)
			fileout.write(iva)
			while True:
				chunk = filein.read(blockSize)
				if len(chunk) == 0:
					break
				elif len(chunk)%20 != 0:
					chunk += ' '*(20-len(chunk)%20)
				fileout.write(c.encode(chunk))
			
def decode(filename):
	encFile = filename[:-4]
	blockSize = 64*1024
	with open(filename,'rb') as filein:
		fileSize = long(filein.read(20))
		iva  = filein.read(20)
		with open(encFile,'wb') as fileout:
			while True:
				chunk = filein.read(blockSize)
				if len(chunk) == 0:
					break
				fileout.write(c.decode(chunk))
			
def main():
	print 'Choose Mode:'
	print '1.encrypt\n2.decrypt\n'
	try:
		choice = input('Input>> ')
	except:
		print 'Err: Only Numbers !! Try Again'
	print 'FileName : '
	fname = raw_input("Input>> ")
	if choice == 1:
		encode(fname)
	elif choice == 2:
		decode(fname)
		
main()
