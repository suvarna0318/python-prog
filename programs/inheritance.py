class Emp:
	def __init__(self,name,sal):
		self.name=name
		self.sal=sal

class Dev(Emp):
	def __init__(self,name,sal,lang):
		super().__init__(name,sal)
		self.lang=lang

class Manager(Emp):
	def __init__(self,name,sal,employees=None):
		super().__init__(name,sal)
		if employees is None:
			self.employees=[]
		else:
			self.employees=employees

	def add_emps(self,emp):
		if emp  not in self.employees:
			self.employees.append(emp)

	def remove_emps(self):
		if emp  in self.employees:
			self.employees.remove(emp)

	def print_emp(self):
		for emp in self.employees:
			print(emp)
d1=Dev("su",2500,"py")
print(d1.name)
mgr=Manager("aarav",8000,[d1,d1])
print(mgr.name)
