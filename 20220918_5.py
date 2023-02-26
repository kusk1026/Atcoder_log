N, A, B = map(int, input().split())

all = 0

for i in range(1, N+1):
    quotient = i
    sum = 0
    while True:
        sum += quotient % 10
        quotient = quotient // 10
        if quotient == 0:
            if A <= sum <= B:
                all += i
            break
        
print(all)