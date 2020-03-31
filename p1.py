num_of_cases = int(input())

for case in range(num_of_cases) :
    _ , total_monay =  map(int, input().split())
    arr_cost = list(map(int, input().strip().split()))
    
    arr_cost.sort()
    Sum = 0 
    for i in range(len(arr_cost)) :
        Sum  += arr_cost[i]
        if Sum  > total_monay :
            break 

    print("Case #{}: {}".format(case+1, i), flush = True)

