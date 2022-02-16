# 직사각형에서 탈출
x, y, w, h = map(int, input().split())

A = [w-x, x, h-y, y]
print(min(A))