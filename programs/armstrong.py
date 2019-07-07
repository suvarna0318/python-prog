# def armstrong(n):
# 	i=len(str(n))
# 	sum=0
# 	temp=n

# 	while temp>0:
# 		rem=temp%10
# 		sum=sum+rem**i
# 		temp=temp//10

# 	if n==sum:
# 		print("armstrong")
# 	else:
# 		print("not")
	

#armstrong number in given range
for num in range(100,160):  
   sum = 0  
   temp = num  
   while temp > 0:  
       digit = temp % 10  
       sum += digit ** 3  
       temp //= 10  
       if num == sum:  
            print(num)  