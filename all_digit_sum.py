def digitsum(x):
    s = str(x)
    l = list(map(int, s))
    result = sum(l)
    return result

print(digitsum(567))