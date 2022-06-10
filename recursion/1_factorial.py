#recursion is method of making function to call itself
#using this we split a problem to smaller problems until we reach a smallest problem whose answer is easy to find.

# eg factorial
# 5!=5*4*3*2*1=> 5 * 4!=5*(4*3!) etc.
from subprocess import CalledProcessError


def factorial(num):
    #keep making problem smaller
    if num>1:
        return num* factorial(num-1)
    # but at one point you need to solve the problem
    elif num==1 or num==0:
        return 1
    else:
        raise Exception("Please enter positive numbers. We don't know how to get answer for negative numbers")

if __name__=="__main__":
    print(factorial(5))

#FUNCTION CALL STACK
# recursive functions occupy variable space depending on no. of calls.
# and each call will be saved in a stack until it has been solved. eg. you are solving factorial 3,
# ur stack will look like below:

#Please note that stack is first in-last out, so newer calls will go on stacking over old calls

# <bottom> main function call : where factorial(3) is called; it will stay in memory until fact(3) is solved
# factorial(3) call : which will wait for fact(2) to be executed
# factorial(2) call : which will wait for fact(1)
# factorial(1) call: it solves answer=1 and starts returning values to above functions & memory starts getting freed