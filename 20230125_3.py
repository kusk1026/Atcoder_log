N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

cnt = 0

for i in range(N):
    if B[i] - A[i] >= 0:
        
        if A[i+1] > B[i]-A[i]:
            cnt += B[i]
            A[i+1] -= B[i] - A[i]
        else:
            cnt += A[i] + A[i+1]
            A[i+1] = 0

    else:
        cnt += B[i]
        
print(cnt)