def getLargest(a, b, c):
    if a > b:
        if a > c:
            return a
        else: 
            return c
    else:
        if b > c:
            return b
        else:
            return c

a, b, c = map(int, input().split())

print(getLargest(a, b, c))
