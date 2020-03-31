import sys
num_of_cases = int(input())
def get_pest(indexs , arrays):
    Max = -1
    index =-1 
    for i in range(len(arrays)):
        if indexs[i] < len(arrays[0]):
            if arrays[i][indexs[i]] > Max :
                index = i
                Max = arrays[i][indexs[i]]
    return index


for case in range(num_of_cases) :
    num_of_next_lines, _, num_of_pates =  map(int, input().split())
    arrays =  [None] * num_of_next_lines
    indexs =  [0] *  num_of_next_lines
    total = 0  
    for line in range(num_of_next_lines) :
        arrays[line]=list(map(int, input().split()))
    
    for i in range(num_of_pates):
        index = get_pest(indexs , arrays)
        if index == -1 :
            break
        total += arrays[index][indexs[index]]
        indexs[index] += 1  
    print("Case #{}: {}".format(case+1, total), flush = True)





# num_of_cases = 1  
 
# def get_pest(indexs , arrays):
#     Max = arrays[0][indexs[0]]
#     index = 0 
#     for i in range(len(indexs)):
#         if arrays[i][indexs[i]] > Max :
#             index = i
#             Max = arrays[i][indexs[i]]
#     return index


# for case in range(num_of_cases) :
#     num_of_next_lines , _ , num_of_pates =  map(int, input().split())
#     arrays =  [None] * num_of_pates
#     indexs =  [0] *  num_of_pates
#     total = 0  
#     for line in range(num_of_pates) :
#         arrays[line]=list(map(int, input().split()))
