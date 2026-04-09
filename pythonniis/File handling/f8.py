import pickle
#create class
class student:
	def__init__(self,roll,name,mark):
		self,roll=roll
		self.name=name
		self.mark=mark
	def show(self):
		print(self,roll,self.name,self.mark)
#write objects to binary file
f=open("student.dat","wb")
s1=student(101,"amit",85)
s2=student2(102,"ravi",90)
s3=student3(103,"sita",88)
pickle.dump(s1,f)
pickle.dump(s2,f)
pickle.dump(s3,f)
f.close()
