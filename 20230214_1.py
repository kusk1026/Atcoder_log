N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
X = int(input())

dp = [-1] * (10**6)
dp[0] = True

for i in range(M):
    dp[B[i]] = False

for i in range(X):
    if dp[i] == True:
        for j in range(N):
            if dp[A[j]+i] == False:
                continue
            else:
                dp[A[j]+i] = True

if dp[X] == True:
    print('Yes')
else:
    print('No')