# D = 대각선 길이, H = 높이 비율, W = 너비 비율
D, H, W = map(int, input().split())
x = pow(D**2 / (H**2 + W**2), 0.5)
print(int(H*x), int(W*x))