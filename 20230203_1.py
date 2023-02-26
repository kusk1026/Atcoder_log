N, K, D = map(int, input().split())
A = list(map(int, input().split()))

dp = [[[-1]*D for i in range(N+1)] for j in range(K+1)] #dp[j][i][d]

for i in range(N+1):
    dp[0][i][0] = 0    

for j in range(K):
    for i in range(N):
        a = A[i]
        for d in range(D):
            if dp[j][i][d] != -1:
                dp[j+1][i+1][(d+a)%D] = max(dp[j][i][d]+a, dp[j+1][i][(d+a)%D])
            
        for d in range(D):
            dp[j+1][i+1][d] = max(dp[j+1][i+1][d], dp[j+1][i][d])
            
print(dp[-1][-1][0])