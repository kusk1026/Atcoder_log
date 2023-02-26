N, P, Q, R, S = map(int, input().split())
l = list(map(int, input().split()))

PQ = l[P-1:Q].copy()
RS = l[R-1:S].copy()

l[R-1:S] = PQ
l[P-1:Q] = RS

print(*l)