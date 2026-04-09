n=int(input("enter your row"))
for i in range(n):
	for j in range(n-i):
		print(n-j,end="\t")
	print()
