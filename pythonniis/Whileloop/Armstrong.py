num=int(input("enter your number"))
num1=num
num2=num
count=0
while(num!=0):
	count=count+1
	num=num//10
sum=0
while(num1>0):
	lastdigit=num1%10
	sum=sum+(lastdigit**count)
	num1=num1//10
if(num2==sum):
	print(num2,"is an armstrong number")
else:
	print(num2,"is not an armstrong number")
