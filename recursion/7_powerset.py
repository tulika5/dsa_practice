#powerset means all subsets of given set
# eg: powerset([1,2])=>[[], [1], [2], [1, 2]]
input_set=[1,2,2,3]
output_set=[[]]
for element in input_set:
    print(f"debug: element={element} & output_set={output_set}")
    for intial_set in output_set:
        output_set=output_set+[intial_set+[element]]

print(output_set)

#start with []
#start with 1: keep the copy of original; and add 1 to existing set => [],[1]
#add 2: keep copy of original & make new results by adding 2=> [],[1],[2],[1,2]
