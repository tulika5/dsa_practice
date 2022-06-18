
class Solution:   
    def myPow(self, x: float, n: int) -> float:
        #base condition
        if n==1:
            return x
        if n==0:
            return 1
        #positive power
        pass
        #negative power
        if n<0:
            x=1/x
            n=-1 *n
        
        ans=self.myPow(x, n//2)
        #even power
        if n % 2==0:            
            return ans * ans
        #odd power
        else:
            return x * ans *ans
    
print(Solution().myPow(0.0000001,213248235235))

