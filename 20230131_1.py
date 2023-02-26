N, W = map(int, input().split())
l = [list(map(int, input().split())) for i in range(N)]

dp = [[float('inf')]*100001 for i in range(N+1)]
dp[0][0] = 0

for i in range(1, N+1):
    for j in range(1, 100001):
        if j < l[i-1][1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-l[i-1][1]]+l[i-1][0])
            
for j in range(100000):
    if W >= dp[N][100000-j]:
        print(100000-j)
        break