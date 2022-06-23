my_list=[(1,0),(4,2),(3,4)]
#sort based on 1st element of each tuple
my_list.sort()
print(my_list)

def return_second_element(arr):
    return arr[1]

my_list1=[(1,5),(4,2),(3,4)]
#sort based on 2nd element of each tuple
my_list1.sort(key=return_second_element)
print(my_list1)
