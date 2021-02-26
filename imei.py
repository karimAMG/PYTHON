
def sumDig( n ): 
	a = 0
	while n > 0: 
		a = a + n % 10
		n = int(n / 10) 
	return a 

# Returns True if n is valid EMEI 
def isValidEMEI(n): 

	# Converting the number into 
	# Sting for finding length 
	s = str(n) 
	l = len(s) 

	# If length is not 15 then IMEI is Invalid 
	if l != 15: 
		return False

	d = 0
	sum = 0
	for i in range(15, 0, -1): 
		d = (int)(n % 10) 
		if i % 2 == 0: 

			# Doubling every alternate digit 
			d = 2 * d 

		# Finding sum of the digits 
		sum = sum + sumDig(d) 
		n = n / 10
	return (sum % 10 == 0) 

# Driver code 
for i in range(1000,9999):
    n = str(86622805437)+str(i)
    if isValidEMEI(int(n)): 
	    print "Valid IMEI Code : "+n 
