S = str(input())
cnt = 0

# while S != 0:
#     if S % 100 == 0:
#         cnt += 1
#         S //= 100
#     else:
#         cnt += 1
#         S //= 10
#時間がかかったためNG→文字列で処理

while len(S) != 1:
    if S[-1] == '0' and S[-2] == '0':
        cnt += 1
        S = S[:-2]
    else:
        cnt += 1
        S = S[:-1]
        
        
print(cnt+1)
