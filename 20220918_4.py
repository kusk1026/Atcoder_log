A = int(input()) #500円
B = int(input()) #100円
C = int(input()) #50円
X = int(input()) #金額

cnt = 0

for a in range(A+1):
    for b in range(B+1):
        for c in range(C+1):
            money = 500 * a + 100 * b + 50 * c
            if money == X:
                cnt += 1

print(cnt)