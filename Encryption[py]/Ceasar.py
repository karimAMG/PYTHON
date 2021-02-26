# variables
key = 13

def encode(msg):
	tx = ''
	for l in msg:
		if ord(l) in range(0,0xff):
			pos = ord(l)
			pos += key
			if pos >= 0xff:
				pos -= 0xff
			if pos < 0:
				pos += 0xff
			tx += chr(pos)
		else:
			tx += l
	return tx
def decode(msg):
	tx = ''
	for l in msg:
		if ord(l) in range(0,0xff):
			pos = ord(l)
			pos -= key
			if pos >= 0xff:
				pos -= 0xff
			if pos < 0:
				pos += 0xff
			tx += chr(pos)
		else:
			tx += l
	return tx
