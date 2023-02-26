N, M = map(int, input().split())

A = []
cnt = 0

for i in range(M):
    C = int(input())    
    a = list(map(int, input().split()))
    A.append(a)
        
        
for i in range(2**M):
    l = []
    for j in range(M):
        if (i >> j) & 1:
            l += A[j]
    if len(set(l)) == N:
        cnt += 1
        
print(cnt)