L = int(input())

if L % 5 == 0:
    t = L // 5
else:
    t = int(L/5 + 1)

print(t)