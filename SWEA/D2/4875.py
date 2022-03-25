# 2에서 출발해 3에 도착할 수 있는가
# 출발지 도착지 위치 찾는 함수
def point(arr):
    start = None
    end = None

    for r in range(len(arr)):
        for c in range(len(arr[r])):
            if arr[r][c] == 2:          # 2 출발지
                arr[r][c] = 0           # 확인했으면 통로로 바꿔 지나갈 수 있게
                start = [r, c]
            if arr[r][c] == 3:
                arr[r][c] = 0
                end = [r, c]

    return start, end


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    start_idx, end_idx = point(arr)
    print(f'#{tc}', end=' ')

    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # stack(현재 경로)과 visit(방문 좌표)은 시작 위치를 담고 있음
    stack = [start_idx]
    visit = [start_idx]

    while True:
        # 더이상 갈데가 없으면 break
        if not stack:
            print(0)
            break

        # 도착지에 도착하면 break
        elif stack[-1] == end_idx:
            print(1)
            break


        else:
            # 현위치에서 사방 확인
            for k in range(4):
                temp_r = stack[-1][0]+dr[k]
                temp_c = stack[-1][1]+dc[k]
                # 움직일 칸이 인덱스를 벗어나면 넘어가
                if temp_r < 0 or temp_r > N-1 or temp_c < 0 or temp_c > N-1:
                    continue
                # 통로가 있다면, 그리고 안 가본데라면
                elif arr[temp_r][temp_c] == 0 and [temp_r, temp_c] not in visit:
                    # 가자
                    stack.append([temp_r, temp_c])
                    visit.append([temp_r, temp_c])
                    break
            # 벽이나 주변에 가본 통로밖에 없다면
            else:
                # 되돌아가기
                stack.pop()

