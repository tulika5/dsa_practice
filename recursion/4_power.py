#find Nth power of a number num
# 2^3=>2*(2^2)=>2*2*(2^1)=>2*2*2
def power_num(num,N):
    if N==0:
        return 1
    else:
        return num * power_num(num,N-1)
print(power_num(2,5))

#if we find recursion tree: 2^3=>2^2=>2^1=>2^0
# so, time complexity=no. of nodes=>O(N)
# space complexity=height of tree=>O(N)

#we can try to optimize this solution
# so, 2^4=(2^2)*(2^2) ie. we can half the tree
# 2 cases:
#1. when power is even: 2^4=(2^2)*(2^2) {4//2 =2}
#2. when power is odd: 2^5=2(2^2)*(2^2) {5//2=2, but remainder=1}
# continue till power=0, then return 1
def power_num_optimized(num,N):
    if N==0: return 1    
    temp=power_num_optimized(num,N//2)
    if (N%2 ==1): return num*temp*temp
    return temp*temp
print(power_num_optimized(2,5))

# now the recursion tree goes like: eg to find for N=64: 64->32->16->8->4->2->1->0
# so: N->N/2->N/4->N/8......1 => N/(2^0)->N/(2^1)->N/(2^2).....N/(2^k)
# so this is a geometric series & we need to find the kth step where N/(2^k) will become=1
#=>N=2^k =>K=logN
# hence, height of tree & no. of nodes here is O(logN)
#so, we optimized the solution to have space complexity=time complexity=O(logN)
