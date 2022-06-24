nums=[6,5,3,2,8,10,9]
k=3
#k-sorted array
# means number which should come at right place is within 3 numbers, right or left of the index
# we should take min heap; so minimum number will always be at top
# as soon as we reach k, we will pop topmost element and set it in our sorted ans
from heapq import heapify, heappop, heappush
heap=[]
heapify(heap)
sorted_ans=[]
count=0
for num in nums:
    heappush(heap,num)
    count+=1
    if count>k:
        sorted_ans.append(heappop(heap))
        count-=1
for j in heap:
    sorted_ans.append(j)
print(sorted_ans)