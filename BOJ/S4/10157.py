# C 가로길이 R 세로길이
C, R = map(int, input().split())
# K 대기 순서
K = int(input())
# 배열 C * R
arr = [[0]*C for _ in range(R)]

# 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
k = 0

# 시작점
r = R-1
c = 0
arr[r][c] = 1
# 자리가 다 차서 배정하지 못한 경우
is_full = False

for i in range(K-1):
    # 좌표 이동
    r += dr[k]
    c += dc[k]
    # 인덱스를 벗어나거나, 자리에 이미 1이 있다면
    if r < 0 or r > R-1 or c < 0 or c > C-1 or arr[r][c] == 1:
        # 한칸 돌아가
        r -= dr[k]
        c -= dc[k]
        # 방향 꺾기
        k = (k + 1) % 4
        # 한칸 이동
        r += dr[k]
        c += dc[k]
        # 방향을 꺾었는데도 막혀있다면
        if arr[r][c] == 1:
            is_full = True
            break
    arr[r][c] = 1

if is_full:
    print(0)
else:
    # x, y 좌표로 변환
    print(c+1, R-r)
