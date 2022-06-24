# courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
# Output: 3

#first sort on basis of last day; then keep trying

# def secondElement(ele):
#     return ele[1]
courses = [[2,5],[2,19],[1,8],[1,3]]
# courses.sort(key=secondElement)
courses.sort(key=lambda c:c[1])

from heapq import heapify,heappop,heappush
max_heap=[]
heapify(max_heap)
total_duration=0
for duration,last_day in courses:
    if duration>last_day:
        continue
    heappush(max_heap, duration*-1)
    total_duration+=duration
    if total_duration>last_day:
        total_duration-=-1 * heappop(max_heap)
    print(f"debug: duration={duration} and last_day={last_day}; total_duration={total_duration}")

print(len(max_heap))

