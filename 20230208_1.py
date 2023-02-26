S = input()
T = input()

for i in range(len(T)):
    if i == len(T)-1:
        print(len(T))
        break
    s = S[i]
    t = T[i]
    
    if s == t:
        continue
    elif s != t:
        print(i+1)
        break