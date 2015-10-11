def invest(amount, rate, time):
	print "principal amount: ", amount
	print "annual rate of return: ", rate
	print "number of years: ", time
	si = amount
	for i in range(1, time+1):
		si = si * (1 + rate)
		print "year ", i, ": ", si


invest(100, 0.05, 8)