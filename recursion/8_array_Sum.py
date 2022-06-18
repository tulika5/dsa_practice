def func(pointer, arr):
	if pointer==len(arr)-1:
		return arr[pointer]
	return arr[pointer]+func(pointer+1,arr)
	
print(func(0,[3,2,4,5]))