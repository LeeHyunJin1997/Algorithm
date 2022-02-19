# 킹(1), 퀸(1), 룩(2), 비숍(2), 나이트(2), 폰(8)
full = [1, 1, 2, 2, 2, 8]
N = list(map(int, input().split()))

for i in range(len(full)):
    print(full[i] - N[i], end=' ')
