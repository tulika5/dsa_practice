# #print Name 5 times using recursion
# def func(N):
#     #base condition
#     if N==5:
#         return
#     print("name")
#     func(N+1)
# func(0)

# #print linearly from 1 to N; N=5
# def func(N):
#     if N==6:
#         return
#     print(N)
#     func(N+1)
# func(1)

#print linearly from N to 1; N=5
def func(N):
    if N==6:
        return
    func(N+1)
    print(N) #this print statement will wait for func to be compeleted=>backtracking
func(1)