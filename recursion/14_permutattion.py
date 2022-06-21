def permute(a, l, r): 
    if l==r: 
        print (a)
    else: 
        for i in range(l,r): 
            a[l], a[i] = a[i], a[l] 
            permute(a, l+1, r) 
            a[l], a[i] = a[i], a[l] # backtrack 
  
# Driver program to test the above function 
arr = [1,2,3]
n = len(arr) 
a = list(arr) 
permute(a, 0, n)