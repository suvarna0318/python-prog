class Emp:
	raise_amount=0
	no_of_emp=0
	def __init__(self,fname,lname,pay):
		self.fname=fname
		self.lname=lname
		self.pay=pay
		self.email=fname + "."+lname+"@gmail.com"
		Emp.no_of_emp+=1
	def fullname(self):
		return f'{self.fname} {self.lname}'
	def apply_raise(self,raise_amount):
		self.pay=self.pay*self.raise_amount #here i can apply instance(self) or class(Emp) t change raise_amt
		return self.pay

print(Emp.no_of_emp)
e1=Emp("suvarna","patil",3000)
e2=Emp("aarav","Ramnor",1200)
print(Emp.no_of_emp)
e3=Emp("aarav","Ramnor",1200)
# print(e1.fullname()) #calling fun with instance
# print(e2.fullname())
# print(Emp.fullname(e1))#passing instance
# e1.raise_amount=4
# print(e2.raise_amount)
# print(e1.raise_amount)
# print(e1.apply_raise(3))
print(Emp.no_of_emp)
