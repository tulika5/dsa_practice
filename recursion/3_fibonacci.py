# find Nth term of fibonacci sequence using recursion
# fibonacci seq: 1,1 (first 2 terms are given),2(then keep adding 2 previous terms),3(2+1),5(3+2),8(5+3)
# so seq:1,1,2,3,5,8,13,21.....

def fibonacci_generator(num):
    if num==1 or num==2:
        return 1
    else:
        return fibonacci_generator(num-1)+fibonacci_generator(num-2)

print(fibonacci_generator(8))

# RECURSION TREE for this approach eg. find fibonacci 5th term
# 5th term= 4th + 3rd term
# |                      |
#4th term=3rd+2nd       3rd term=2nd + 1st term
# |
# 3rd term=2nd+1st term
#|
# 2nd term + 1st term => base conditions, so solved

# space complexity=height of tree; for N=5, height=4, approx. O(N) for larger terms
# time complexity= number of nodes => each node is expanding to 2, so each level=> 2^N 
# -> looks like geometric progression; so, sum of GP=A(r^n -1)/(r-1); here r=2; Sum=2^n-1 => O(2^N)
#=> very expensive time complexity, will learn how to optimize this using dynamic programming
# because if u notice some of the terms were recalculated, if we could save them somehow, we wont need to recompute them
