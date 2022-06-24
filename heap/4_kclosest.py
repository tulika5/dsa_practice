#find k closest numbers to given target
from heapq import heapify, heappop, heappush

nums=[3,4,5,6,7,8,9,1]
target=7
k=5
# if i find diff of elements from 7: diff=>[4,3,2,1,0,1,2,6], 5 numbers with least diff will be my ans
#so i should keep max. diff. on top, so i can pop them away
#so use maxheap
#python by default provides minheap, so multiply your key by -1
heap=[]
heapify(heap)
count=0
for num in nums:
    diff=abs(target-num)
    heappush(heap,[-1*diff,num])
    count+=1
    if count>k:
        heappop(heap)
        count-=1

for num in heap:
    print(num[1]," ")

