N = int(input())
S = str(input())

X = []
l = list(S)
cnt = 0
cc = 0

for i in range(N):
    if l[i] == '"':
        cnt += 1
        
    elif cnt == 1:
        X.append(l[i])
        l[i] = ''
        
    if cnt == 2:
        cnt = 0
        
for i in range(N):
    if l[i] == ',':
        l[i] = '.'
        
    elif l[i] == '':
        l[i] = X[cc]
        cc += 1
        
ans = ''.join(l)
print(ans)