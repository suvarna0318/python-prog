
fibonacci series
def fib(n):
	result=[]
	a,b=0,1
	while a<n:
		result.append(a)
		a,b=b,a+b
	print(result)

fib(50)

factorial of given number
def fact(num):
	if num==0 or num==1:
		return 1
	else:
		return num*fact(num-1)

print(fact(5))

	


