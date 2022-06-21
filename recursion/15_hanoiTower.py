answer=[]
def helperHanoi(n,src,dest,help):
    if n==0:
        return 
    helperHanoi(n-1,src,help,dest)
    answer.append((src,dest))
    print("Move disk",n,"from rod",src,"to rod",dest)
    helperHanoi(n-1,help,dest,src)
        
def towerOfHanoi(n):
    helperHanoi(n,'A','B','C')
towerOfHanoi(3)
print(answer)