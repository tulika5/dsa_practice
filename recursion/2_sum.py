# find sum of N natural numbers using recursion
# eg. sum of 3 numbers= 3+(sum of 2 numbers)=3+(2+(sum of 1 numbers)); 
# where sum of 1 numbers=1, so that becomes breakingpoint

def natural_sum(num):
    if num>1:
        return num + natural_sum(num-1)
    elif num==1:
        return 1
    else:
        raise Exception("Please enter valid natural number ie. 1,2,....")

print(natural_sum(5))

# if we draw recursion tree for this code eg. find sum of 5 numbers
#below are nodes of the tree

# sum(5) =5+sum(4)      =5+10=15=>final answer
# |                         |
#sum(4) = 4+ sum(3) =4+6=10--
# |                         |
#sum(3)= 3 + sum(2) =3+3=6--
# |                       |
# sum(2)=2 + sum(1)=2+1=3--
# |                 |
# sum(1)=1-----------

#space complexity =number of function calls=height of tree=> O(N)
#time complexity = no. of nodes of tree=> O(N)