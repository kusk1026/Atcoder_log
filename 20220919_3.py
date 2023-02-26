N, Y = map(int, input().split())

for l in range(N+1):
    for m in range(N-l+1):
        money = 10000*l + 5000*m + 1000*(N-l-m)
        if money == Y:
            a = l
            b = m
            c = N - l - m
            break
        elif l == N:
            a = -1
            b = -1
            c = -1
    if money == Y:
        break

print(a, b, c)