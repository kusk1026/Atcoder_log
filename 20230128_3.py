N = int(input())
l = [list(map(int, input().split())) for i in range(N)]

dp = [[0]*3 for i in range(N)]

dp[0] = l[0]

for i in range(1,N):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + l[i][0]
    dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + l[i][1]
    dp[i][2] = max(dp[i-1][1], dp[i-1][0]) + l[i][2]
    
print(max(dp[-1]))

# for i in range(N):
#     if i == 0:
#         dp[0] = max(l[0])
        
#     elif dp[i-1] == l[i-1][0]:
#         dp[i] = max(l[i][1], l[i][2])
#     elif dp[i-1] == l[i-1][1]:
#         dp[i] = max(l[i][0], l[i][2])
#     elif dp[i-1] == l[i-1][2]:
#         dp[i] = max(l[i][0], l[i][1])
        
# print(sum(dp))