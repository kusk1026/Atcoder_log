S = str(input())

n = int(len(S))
cnt = 1
for i in range(n-1):
    if S[i] == 0 and S[i+1] == 0:
        cnt += 1
    else:
        