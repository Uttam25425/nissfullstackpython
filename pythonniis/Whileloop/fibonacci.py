length=int(input("enter your length"))
n1=0
n2=1
print(n1,n2,end=" ")
for i in range(length-2):
	next=n1+n2
	print(next,end=" ")
	n1=n2
	n2=next
