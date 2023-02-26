N = int(input())
A_list = list(map(int, input().split()))
Q = int(input())
query_list = [list(map(int, input().split())) for i in range(Q)]
# 1 k x または 2 k

for query in query_list:
        if query[0] == 1:
            A_list[query[1]-1] = query[2]
        if query[0] == 2:
            print(A_list[query[1]-1])