no=121
s=0
temp=no
while no!=0:
	r=no%10
	s=s*10+r
	no=no//10
if trmp==s:
	print(temp,"is pd no")
else:
	print(temp,"is not a pd no")