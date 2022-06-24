#find 3 largest numbers
nums=[5,7,8,13,2,4]
k=3
# nums.sort(reverse=True)
# print(nums[:3])
from heapq import heapify,heappop,heappush
#kth largest number so min heap
heap=[]
heapify(heap)
counter=0
for num in nums:
    heappush(heap,num)
    counter+=1
    if counter>k:
        heappop(heap)
        counter-=1

for j in heap:
    print(j,end=" ")

#NOTE THAT there wont be a guarantee of ordering internally; we will for sure get top 3 largest numbers; 