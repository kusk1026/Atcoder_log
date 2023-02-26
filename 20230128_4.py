N, W = map(int, input().split())
l = [list(map(int, input().split())) for i in range(N)]

dp = [[0]*(W+1) for i in range(N+1)]

for i in range(1, N+1):
    for j in range(1, W+1):
        if j < l[i-1][0]:
            dp[i][j] = dp[i-1][j]
            
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-l[i-1][0]]+l[i-1][1])
            
            
print(dp[-1][-1])