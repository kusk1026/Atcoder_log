N, X = map(int, input().split())

dp = [[False]*(X+1) for i in range(2501)]
dp[0][0] = True
cnt = 1

for i in range(1,N+1):
    A, B = map(int, input().split())
    for k in range(B):
        for j in range(X+1):
            if j < A:
                dp[cnt][j] = dp[cnt-1][j]
            elif (dp[cnt-1][j] == True) or (dp[cnt-1][j-A] == True):
                dp[cnt][j] = True
        cnt += 1               
        
for i in range(2501):
    if dp[i][-1] == True:
        print('Yes')
        break
    elif i == 2500:
        print('No')
    