from math import sqrt
from collections import Counter

K = int(input())
root = int(sqrt(K))
prime = []

for i in range(2, root+1):
    while K % i == 0:
        K //= i
        prime.append(i)

if K != 1:
    prime.append(K)
    
d = Counter(prime)
l = []

for k, v in d.items():
    cnt = 0 #指数の数
    cc = 0 #係数
    while cnt < v:
        cc += 1
        div = k * cc
        while div % k == 0:
            div //= k
            cnt += 1
    l.append(k*cc)
    
print(max(l))