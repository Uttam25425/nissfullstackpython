no1=int(input("enter your first number"))
no2=int(input("enter your second number"))
if no1<no2:
	small=no1
else:
	small=no2
i=1
while i<=small:
	if no1%i==0 and no2%i==0:
		hcf=i
	i=i+1
print("hcf of a given number is",hcf)
print("lcm of a given number is",(no1*no2)/hcf)