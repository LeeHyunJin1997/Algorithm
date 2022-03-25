# 홈방법 서비스
T = int(input())
for tc in range(1, T+1):
    # N 도시 크기, M 각 집이 내는 비용
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 각 집들의 좌표를 저장
    houses = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                houses.append((i,j))

    max_val = 0
    # 각 좌표에서 집들과의 거리를 구해
    for ci in range(N):
        for cj in range(N):
            houses_dis = []
            for i in range(len(houses)):
                houses_dis.append(abs(houses[i][0]-ci) + abs(houses[i][1]-cj))

            # k 범위는 1 ~ N+1
            for k in range(1, N+2):
                cost = k*k + (k-1)*(k-1)
                cnt = 0
                # 거리가 k 미만인 집들의 수를 세
                for j in range(len(houses_dis)):
                    if houses_dis[j] < k:
                        cnt += 1
                
                # 해당 k에서 손해를 보지 않으면서 이전보다 더 많은 집에 서비스 제공한다면
                if cnt*M >= cost and max_val < cnt:
                    max_val = cnt


    print(f'#{tc} {max_val}')

