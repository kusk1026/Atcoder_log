N, K = map(int, input().split())
h = list(map(int, input().split()))

dp = [0] * N

dp[1] = abs(h[1]-h[0])

for i in range(2, N):
    l = []
    for j in range(1, min(K+1, i+1)):
        l.append(dp[i-j] + abs(h[i]-h[i-j]))
    dp[i] = min(l)
    
print(dp[-1])