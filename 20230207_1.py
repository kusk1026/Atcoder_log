S = str(input())
T = str(input())

front = len(T)
rear = len(T)

for i in range(len(T)):
    s = S[i]
    t = T[i]
    
    if s == '?' or t == '?':
        continue
    if s == t:
        continue
    else:
        front = i
        break
    
for i in range(1, len(T)+1):
    s = S[-i]
    t = T[-i]

    if s == '?' or t == '?':
        continue
    if s == t:
        continue
    else:
        rear = i - 1
        break
    
for i in range(len(T)+1):
    if i <= front and len(T)-i <= rear:
        print('Yes')
    else:
        print('No')