#powerset means all subsets of given set
# eg: powerset([1,2])=>[[], [1], [2], [1, 2]]
final_ans=[]

def func(input_Arr,index_to_add,result_seq):
    if index_to_add==len(input_Arr):
        final_ans.append(result_seq)
        return
    #won't add
    func(input_Arr,index_to_add+1,result_seq)
    #let me add
    func(input_Arr,index_to_add+1,result_seq+[input_Arr[index_to_add]])

func([1,2],0,[])
print(final_ans)
#[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

#start with []
#start with 1: keep the copy of original; and add 1 to existing set => [],[1]
#add 2: keep copy of original & make new results by adding 2=> [],[1],[2],[1,2]
