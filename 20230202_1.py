from collections import defaultdict
S = str(input())

X = []
Y =defaultdict(int)

now = set()

for s in S:
    if s == '(':
        X.append(now)
        now = set()
        continue
    
    if s == ')':
        for t in now:
            Y[t] = 0
            
        now = X.pop(-1)
        continue
    
    if Y[s] != 0:
        print('No')
        exit()
    
    Y[s] = 1
    now.add(s)
    
print('Yes')