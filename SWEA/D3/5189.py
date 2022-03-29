# 전자카트

def f(i, N):
    """
    1로 끝나는 순열을 생성하는 함수
    :param i: 현위치
    :param N: 순열길이
    :return:
    """
    if i == N:
        routes.append(p + [1])
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            f(i+1, N)
            # 원래대로 복구
            p[i], p[j] = p[j], p[i]


T = int(input())
for tc in range(1, T+1):
    # N 배열크기
    N = int(input())
    # e 배터리 소비량 표
    e = [list(map(int, input().split())) for _ in range(N)]

    p = [x for x in range(1, N+1)]

    routes = []

    # 양 끝이 1로 고정된 경로(순열)를 탐색
    f(1, N)

    # 각 경로 별로 배터리 소비량을 찾기
    min_battery = 999999999
    for i in range(len(routes)):
        battery = 0
        for j in range(1, N+1):
            battery += e[routes[i][j-1] - 1][routes[i][j] - 1]

        if battery < min_battery:
            min_battery = battery

    print(f'#{tc} {min_battery}')
