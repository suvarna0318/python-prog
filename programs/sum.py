# sum of natural numbers

def sum(num):
	sum=0
	for i in range(1,num+1):
		sum=sum+i
	print(sum)
sum(10)

#fibonacci numbers

def fibonaci(n):
	a,b=0,1
	print(a)
	result=[]
	while(a<n):
		a,b=b,a+b
		print(a)
		result.append(a)
	print(result)



fibonaci(10)




