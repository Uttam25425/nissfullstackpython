f=open("data.txt","r")
l=f.readlines()
for i in l:
	print(i,end="")
f.close()