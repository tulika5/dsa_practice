final_answer=[]

def find_powerset(answer,input_arrray,pointer,last_limit):
    #base condition
    if pointer==last_limit:
        final_answer.append(answer)
        return
    #either add element
    find_powerset(answer,input_arrray,pointer+1,last_limit)
    #or dont add
    find_powerset(answer+ [input_arrray[pointer]],input_arrray,pointer+1,last_limit)

  
input_arrray=[1,2,3]
find_powerset([],input_arrray,0,len(input_arrray))
print(final_answer)