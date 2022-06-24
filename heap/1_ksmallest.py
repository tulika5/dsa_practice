#find 3rd smallest number in array
# kth smallest=>max heap

nums=[7,10,3,4,20,15]
k=3
# nums.sort() #normal sort: O(NlogN)
# print(nums[2]) #Ans should be 7
from heapq import heapify,heappush,heappop
heap=[]
heapify(heap)
counter=0
#we are making max heap; so multiply each element with -1 before pushing
for num in nums:
    heappush(heap,-1*num)
    counter+=1
    #if size of heap has already reached what we wanted to calculate; so its done now
    if counter>k:
        heappop(heap)
        counter-=1

#pop topmost element; that will be your answer
final_answer=-1* heappop(heap)
print(final_answer)