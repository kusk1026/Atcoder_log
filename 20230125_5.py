N, A, B = map(int, input().split())
S = str(input())

l = [i for i in S]
digit = N // 2
M = 0

for i in range(N):
    cnt = 0
    b = 0
    for j in range(digit): #一致数
        if l[j] == l[-j-1]:
            cnt += 1
    b = digit - cnt
    money = A*i + B*b
    if M > money or i == 0:
        M = money
    p = l.pop(0)
    l.append(p)
    
print(M)