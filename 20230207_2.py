from math import sqrt
T = int(input())

for t in range(T):
    N = int(input())
    for i in range(2,N):

        if N % i**2 == 0:
            p = i
            q = N // (i**2)
            print(p, q)
            break
            
        elif N % i == 0:
            q = i
            p = int(sqrt(N//i))
            print(p, q)
            break