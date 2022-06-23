# # # Input: nums = [2,7,11,15], target = 9
# # # Output: [0,1]
# # # Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# # #bruteforce
# # def bruteforce(nums,target):
# #     for i in range(0,len(nums)):        
# #         for j in range(i+1,len(nums)):
# #             if nums[i]+nums[j]==target:
# #                 return [i,j]
# #     return []
# # print(bruteforce( [2,7,11,15],9))
# # #time complexity=O(N), space complexity=O(1)
# # #RESULT:
# # # Runtime: 5843 ms, faster than 13.39% of Python3 online submissions for Two Sum.
# # # Memory Usage: 15 MB, less than 76.80% of Python3 online submissions for Two Sum.

# # #introduce memory component; to reduce time; hashtable in python=>dictionary
# # #save {number:index}
# def using_hashtable(nums,target):
#     lookup_dict={}
#     for i in range(len(nums)):
#         print(lookup_dict)        
#         try:
#             return [lookup_dict[target-nums[i]],i]
#         except:
#             pass
#         lookup_dict[nums[i]]=i
#     return []
# print(using_hashtable( [3,2,4],6))

# #time complexity: O(N)(for loop)+O(N) (for insert/scan in hashtable)
# #hashtable; avg case: O(1); worst case: when 2 many elements have been hashed using same key=>O(N)
# #space complexity:O(N)
# #RESULT:
# # Runtime: 75 ms, faster than 79.43% of Python3 online submissions for Two Sum.
# # Memory Usage: 15.2 MB, less than 49.90% of Python3 online submissions for Two Sum.

# #approach3=>not so good here, but good to learn 2-pointer method
def two_pointer(nums,target):
    proc_list=[]
    for i in range(len(nums)):
        proc_list.append((nums[i],i))
    proc_list.sort()
    L=0
    R=len(nums)-1
    while True:
        if L>=R:
            return []
        if proc_list[L][0]+proc_list[R][0]==target:
            return [proc_list[L][1],proc_list[R][1]]
        elif proc_list[L][0]+proc_list[R][0]<target:
            L=L+1
        elif proc_list[L][0]+proc_list[R][0]>target:
            R=R-1

            

print(two_pointer([2,3,5,8,4],20))
