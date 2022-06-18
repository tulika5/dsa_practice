# N=1; open_bracket=1, close_bracket=1 ans=["()"]
result=[]
def generate_parenthesis_rec(current,open_brace,close_brace):
    if open_brace==0 and close_brace==0:
        result.append(current)
        return
    if open_brace>0:
        generate_parenthesis_rec(current+"(",open_brace-1,close_brace)
    if open_brace<close_brace:
        generate_parenthesis_rec(current+")",open_brace,close_brace-1)

def generate_parenthesis(num):
    return generate_parenthesis_rec("",num,num)    
generate_parenthesis(2)
print(result)


        