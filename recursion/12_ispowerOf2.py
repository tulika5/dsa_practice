class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # base condition
        if n==1:
            return True
        if n % 2==1 or n==0:
            #already not possible
            return False
        if n%2==0:
            #investigate further
            return self.isPowerOfTwo(n/2)


print(Solution().isPowerOfTwo(5))

#FURTHER TO CHECK:
# As we know, a number is power of two or a multiple of two if it has only one bit set in its binary representation, so if I do N & (N-1) then the result should be 0 for a number to be a power of 2.
# Example : N = 5 (not a power of 2)
# 5 in binary = 101
# 5-1 => 4 in binary = 100
# now, (5 & (4)) => will not be equal to 0, thats why N = 5 is not a power of 2.
# similarly you can check for other numbers also.