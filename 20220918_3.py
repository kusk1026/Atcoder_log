N = int(input())
A = list(map(int, input().split()))

cnt = 0
TF = True
while TF == True:
    for a in A:
        if a % 2 == 1:
            TF = False
    if TF == True:
        A = [a/2 for a in A]
        cnt += 1

print(cnt)
        
    