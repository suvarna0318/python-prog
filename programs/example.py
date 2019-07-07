#removing duplicate words from given string
# def rem_dup(string):
# 	str=string.split(" ")
# 	print(str)
# 	result=[]
# 	for i in str:
# 		if i not in result:
# 			result.append(i)


# 	print(result)
# rem_dup("enter the string: : the")

#count the number of digits
# def func(num):
	
# 	count=0
# 	for i in str(num):
# 		count=count+1
# 	print(count)
# func(165478996301)
# prime numbers between two intervals
#prime numbers between interval

# result=[]

# for num in range(12,35):
# 	for i in range(2,num):
# 		if num%i==0:
# 			break
# 	else:
# 		result.append(num)
# print(result)

#counting duplicate in string

# str="hello heloo"
# count=0
# for i in str:
# 	print(i,str(count(i)))


#calendar
# import calendar

# print(calendar.month(2019,7))
# print(calendar.prcal(2019))


import array as a
a1=a.array('i',[1,2,3,4,5])
a2=a1
print(a2.sorted(reverse=True))