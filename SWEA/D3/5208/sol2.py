# 전기버스2

# 정류장 n에 도착할 수 있는 가장 먼 정류장을 찾는 함수
def find(n):
    for i in range(n-1, 0, -1):
        if i + lst[i] >= n:
            first = i
    return first


T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    # 정류장 수
    N = lst[0]

    cnt = -1
    now = N
    while now > 1:
        now = find(now)
        cnt += 1

    print(f'#{tc} {cnt}')

