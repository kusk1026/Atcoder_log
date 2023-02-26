N = int(input())
l = list(map(int, input().split()))

SUM1 = 0
SUM2 = 0

for i in range(N):
    MAX = max(l)
    num = l.index(MAX)
    Del = l.pop(num)
    if i % 2 == 0:
        SUM1 += Del
    else:
        SUM2 += Del
        
print(SUM1 - SUM2)
        

