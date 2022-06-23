# courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
# Output: 3

courses =  [[5,5],[4,6],[2,6]]
# Output: 0

def secondElement(ele):
    return ele[0]
courses.sort(key=secondElement)
total_Day=0
total_Courses=0
for course in courses:
    if total_Day+course[0]>course[1]:
        break
    if course[0]>course[1]:
        pass
    else:
        total_Courses+=1
        total_Day+=course[0]

print(total_Day)
print(total_Courses)

#NOT CORRECT SOLUTION; REVISIT AFTER LEARNING HEAP + GREEDY

