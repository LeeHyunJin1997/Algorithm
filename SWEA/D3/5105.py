# 미로의거리
T = int(input())
for tc in range(1, 1+T):
    # N 미로크기
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    # 출발지 도착지 찾기
    start = None
    end = None
    for r in range(N):
        for c in range(N):
            if arr[r][c] == 3:
                arr[r][c] = 0
                end = [r, c]
            elif arr[r][c] == 2:
                arr[r][c] = 1
                start = [r, c]

    queue = [start]
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    cnt = -1
    finish = 0

    while True:
        # 도착지를 찾았을 경우
        if finish == 1:
            print(f'#{tc} {cnt}')
            break

        # 다 돌았는데 못 찾았을 경우
        if not queue:
            print(f'#{tc} 0')
            break

        for j in range(len(queue)):
            loc = queue.pop(0)

            for k in range(4):
                temp_r = loc[0] + dr[k]
                temp_c = loc[1] + dc[k]
                # 인덱스 에러 방지
                if temp_r < 0 or temp_r > N-1 or temp_c < 0 or temp_c > N-1:
                    continue
                elif [temp_r, temp_c] == end:
                    finish = 1
                    break
                else:
                    # 가려하는 곳이 안가본 통로라면
                    if arr[temp_r][temp_c] == 0:
                        arr[temp_r][temp_c] = 1
                        queue.append([temp_r, temp_c])

        # queue를 한번 비울 때마다 카운트
        cnt += 1


