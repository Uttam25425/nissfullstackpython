for no in range(10,21,1):
	c=0
	i=1
	while i<=no:
		if no%i==0:
			c=c+1
		i=i+1
	if c==2:
		print(no,"is a prime no")
	else:
		print(no,"is not a prime no")
