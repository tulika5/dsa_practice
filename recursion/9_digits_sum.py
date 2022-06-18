def func(num):
	if num==0:
		return 0
	return func(num//10)+num%10
print(func(235))
