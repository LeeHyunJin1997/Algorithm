# 재미있는 오셀로 게임

# 돌 하나 놓을 때 뒤집기 함수
def flip(c, r, bw):
    # 팔방 탐색
    # 상 우상 우 우하 하 좌하 좌 좌상
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]

    # 돌 놓은 자리
    arr[r][c] = bw
    # 각 방향에 대해서
    for k in range(8):
        i = 1
        footprint = []
        while True:
            # 이번에 뒤집어야할 좌표
            r_temp = r + dr[k] * i
            c_temp = c + dc[k] * i
            # 벽이나 0을 만나면 그간 바꿨던 자리 돌려놔
            if r_temp < 0 or r_temp > N-1 or c_temp < 0 or c_temp > N-1 or arr[r_temp][c_temp] == 0:
                for j in footprint:
                    # 바꾼 색이 1이면 2, 2면 1
                    arr[j[0]][j[1]] = 3 - bw
                break
            # 같은 색 돌을 만나면 그만
            elif arr[r_temp][c_temp] == bw:
                break
            # 사이에 있는 돌 뒤집고 temp 에 바꾼 좌표를 임시 저장
            arr[r_temp][c_temp] = bw
            footprint.append([r_temp, c_temp])
            i += 1


T = int(input())
for tc in range(1, T+1):
    # N 보드 크기, M 돌 놓는 횟수
    N, M = map(int, input().split())
    # [[c, r, bw], ...]
    input_list = [list(map(int, input().split())) for _ in range(M)]
    # NxN 보드
    arr = [[0]*N for _ in range(N)]
    # 처음 주어지는 기본 배치
    arr[N//2][N//2] = 2
    arr[N//2 - 1][N//2 - 1] = 2
    arr[N//2 - 1][N//2] = 1
    arr[N//2][N//2 - 1] = 1


    for i in input_list:
        flip(i[0]-1, i[1]-1, i[2])

    # 흑돌(1) 개수, 백돌(2) 개수 차례로 출력
    cnt_black = 0
    cnt_white = 0

    for i in arr:
        for j in i:
            if j == 1:
                cnt_black += 1
            elif j == 2:
                cnt_white += 1

    print(f'#{tc} {cnt_black} {cnt_white}')