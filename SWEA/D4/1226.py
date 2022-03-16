# 미로 1
T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(16)]

    visited = []
    stack = []

    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                start = [i, j]

    visited = []
    stack = [[start[0], start[1]]]
    goal = False

    while True:
        # 도착못할 경우
        if not stack:
            print(f'#{tc} {0}')
            break

        if goal:
            print(f'#{tc} {1}')
            break

        r = stack[-1][0]
        c = stack[-1][1]

        for k in range(4):
            temp_r = r + dr[k]
            temp_c = c + dc[k]
            # 도착지에 도착했을 경우
            if arr[temp_r][temp_c] == 3:
                goal = True
                break

            # 통로를 만날 경우 이동
            elif arr[temp_r][temp_c] == 0 and [temp_r, temp_c] not in visited:
                visited.append([temp_r, temp_c])
                stack.append([temp_r, temp_c])
                break

        # 사방이 막혀있을 경우
        else:
            stack.pop()


