#how to reverse array using recursion
#original ip: 1,2,3,4,5
#first turn: swap 1st and last element of substring; pass between substring to recursion func: 5,[2,3,4],1
#second turn:[2,3,4]=>4[3]2
# 3rd turrn: 432; start returning answer to previous turn
#2nd turn ans: 432
#1st turn ans: 54321

def reverseArrayHelper(nums, l, r):
    if(l >= r): return
    nums[r], nums[l] = nums[l], nums[r]
    return reverseArrayHelper(nums, l+1, r-1)

def reverseArray(nums):
    return reverseArrayHelper(nums, 0, len(nums)-1)

nums =[1,2,3,4,5]
reverseArray(nums)
print(nums)

#shortcut-python list slicing
print( nums[::-1])
#list slicing: [ <first element to include> : <first element to exclude> : <step> ]