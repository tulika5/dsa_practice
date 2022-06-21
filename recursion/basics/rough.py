# verify if given array is sorted
# If the array is {2, 4, 8, 9, 9, 15}, then the output should be true.
# If the array is {5, 8, 2, 9, 3}, then the output should be false.

def check_array_sorted(arr,index,max_limit):
    if index==max_limit-1:
        return True
    return check_array_sorted(arr,index+1,max_limit) and arr[index+1]>=arr[index]

arr=[2, 4, 8, 9, 9, 15]
print(check_array_sorted(arr,0,len(arr)))