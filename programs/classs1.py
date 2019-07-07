#class methods and static methods
class Emp:
	raise_amount=1
	no_of_emp=0
	def __init__(self,fname,lname,pay):
		self.fname=fname
		self.lname=lname
		self.pay=pay
		self.email=fname + "."+lname+"@gmail.com"
		Emp.no_of_emp+=1
	def fullname(self):#regular method pass self as first argument in the method
		return f'{self.fname} {self.lname}'
	def apply_raise(self,raise_amount):
		self.pay=self.pay*self.raise_amount #here i can apply instance(self) or class(Emp) t change raise_amt
		return self.pay

	@classmethod#class method pass cls as first argument
	def set_raise_amt(cls,amt):
		cls.raise_amount=amt
	@classmethod
	def from_string(cls,emp_str):
		fname,lname,pay=emp_str_1.split("-")
		return cls(fname,lname,pay)
	@staticmethod#static metho doesn't pass any argument
	def is_workday(day):
		if day.weekday==5 or day.weekday==6:
			return Flase
		return True
import datetime
my_date=datetime.date(2019,7,2)
print(Emp.is_workday(my_date))

# Emp.set_raise_amt(4) or e1.set_raise_amt(5) # both are same 
emp_str_1="john-maddy-50000"
emp_str_2="johny-bruno-50000"


t=Emp.from_string(emp_str_1)
print(t.fname)
# e1=Emp("suvarna","patil",3000)
# e2=Emp("aarav","Ramnor",1200)

# print(e1.raise_amount)
# print(e2.raise_amount)
# print(e1.__dict__)