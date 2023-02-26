N  =int(input())
l = list(map(int, input().split()))

cnt = 0
TF = True

while TF == True:
    l = [a/2 for a in l]

    for a in l:
        if a.is_integer() == False:
            print(cnt)
            TF = False
            break
    if TF == True:
        cnt += 1
    