# verify if a string is palindrome ie. original string=reverse string
# eg. RADAR, NOON is palindrome; CAR is not
#let's implement it first using 2-pointer techinque

#give index to the letters eg RADAR:0,1,2,3,4
#So, move left pointer from 0, move right pointer from 4; increment/decrement until they meet OR left pointer moves to right side
# eg NOON: [left=0, R=3]->[L=1,R=2](so all letters are tested till here)->[L=2,R=1] no need to run this becoz already checked

def check_palindrome(test_string):
    left_pointer=0
    right_pointer=len(test_string)-1    
    while True:
        if left_pointer>=right_pointer:
            return True
        if test_string[left_pointer]!=test_string[right_pointer]:
            return False
        left_pointer+=1
        right_pointer-=1
print(check_palindrome("NOON"))
print(check_palindrome("radar"))
print(check_palindrome("CAR"))

#now solve it using recursion
# each time we will compare first & last letters only, if they are equal then find again for substring, leaving first and last letter of previous turn
#keep doing this until length of string becomes less than 1'in that case also it'is a palindrome becoz we already scanned everything
def check_palindrome_rec(test_string):
    if len(test_string)<1:
        return True
    if test_string[0]==test_string[-1]:
        #continue to check
        return check_palindrome_rec(test_string[1:-1])
    else:
        return False
print(check_palindrome_rec("NOON"))
print(check_palindrome_rec("radar"))
print(check_palindrome_rec("CAR"))

# here, at worst case we will have to reach upto half of the string.
# so, time compelxity=space complexity=O(N)

#note that in the 2 pointer method, time complexity was O(N),<same logic: worst case u scan upto half of the string>
# but space complexity=O(1) ie constant; so 2 pointer is better aproach

    
