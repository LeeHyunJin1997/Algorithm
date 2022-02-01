def Rev(X):
    str(X)
    return int(X[::-1])

X, Y = input().split()

Z = str(Rev(X)+Rev(Y))[::-1]

print(Z.lstrip('0'))

