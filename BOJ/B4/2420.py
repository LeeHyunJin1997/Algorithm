N, M = map(int, input().split())
s = N - M

if s < 0:
    s = -s

print(s)