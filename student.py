class student:
	def getstudent(self):
		self.sid=int(input("Enter Student ID : "))
		self.sname=input("Enter Student Name : ")
		self.maths=float(input("Enter Student Maths Marks : "))
		self.physics=float(input("Enter Student Physics Marks : "))
		self.chemistry=float(input("Enter Student Chemistry Marks : "))
		self.total=self.maths+self.physics+self.chemistry
		self.average=self.total/3
	
	def findgrade(self):
		if(self.maths<35 or self.physics<35 or self.chemistry<35):
                                                                    self.grade="fail"
		elif(self.average>90):
			self.grade="A+"
		elif(self.average>80) :
			self.grade="A"
		elif(self.average>70):
			self.grade="B"
		elif(self.average>60):
			self.grade="C"
		elif(self.average>50):
			self.grade="D"
		elif(self.average>35):
			self.grade="E"
	def __repr__(self):
		return 'student ID:%d\nstudent Name:%s\nstudent Maths Marks:%f\nstudent Physics Marks:%f\nstudentChemistryMarks:%f\nstudent TotalMarks:%f\nstudent average:%f\nstudent Grade:%s'%(self.sid,self.sname,self.maths,self.physics,self.chemistry,self.total,self.average,self.grade)
if __name__ =='__main__':
	s1=student()
	s1.getstudent()
	s1.findgrade()
	print(s1) 		
