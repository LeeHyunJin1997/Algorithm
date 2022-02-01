from re import S


L, P = map(int, input().split())
n1, n2, n3, n4, n5 = map(int, input().split())

# 사람수
num = L * P

print(n1-num, n2-num, n3-num, n4-num, n5-num)
