N = int(input())
B = list(map(int, input().split()))

cnt = B[0]

for i in range(1, N-1):
    cnt += min(B[i-1], B[i])

cnt += B[N-2]
print(cnt)