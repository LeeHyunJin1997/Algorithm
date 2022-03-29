# 최소합

def move(n, m, s):
    """
    :param n: 우로 이동한 횟수
    :param m: 하로 이동한 횟수
    :param s: 현재까지의 부분 합
    :return:
    """
    global rlt
    # 진행중인 경로합이 이미 최솟값을 넘어갔다면
    if s > rlt:
        return

    # 오른쪽 아래로 정상적으로 이동했을 때
    if n == N-1 and m == N-1:
        rlt = s
        return

    # 배열을 넘어갔을 때
    if n > N-1:
        return

    if m > N-1:
        return

    # 우로 더이상 못갈때 하로만 진행
    if n == N-1:
        move(n, m+1, s+arr[n][m+1])

    # 하로 더이상 못갈때 우로만 진행
    elif m == N-1:
        move(n+1, m, s+arr[n+1][m])

    # 둘다 진행
    else:
        move(n+1, m, s+arr[n+1][m])
        move(n, m+1, s+arr[n][m+1])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    rlt = 999999999

    move(0, 0, arr[0][0])

    print(f'#{tc} {rlt}')
