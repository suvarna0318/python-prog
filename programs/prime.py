
def prime_or_not(n):
	for i in range(2,n):
		for j in range(2,i):
			if i%j==0:
				print("not a prime number",i)
				break
		else:
			print(" prime number",i)

prime_or_not(20)