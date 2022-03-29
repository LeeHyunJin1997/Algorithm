# 컨테이너 운반

T = int(input())
for tc in range(1, T+1):
    # N 컨테이너 개수, M 트럭 개수
    N, M = map(int, input().split())
    # 컨테이너 무게 리스트
    w = list(map(int, input().split()))
    # 트럭 용량 리스트
    t = list(map(int, input().split()))

    # 가장 큰 트럭에도 못 들어가는 컨테이너는 날려버려
    w.sort()
    t.sort()

    rlt = 0
    while True:
        # 화물이나 트럭이 더이상 안 남았으면 그만
        if not w:
            break

        if not t:
            break

        # 가장 큰 트럭이 가장 큰 화물을 못 담는 다면 다음 화물
        if w[-1] > t[-1]:
            w.pop()
        # 담을 수 있다면 담아서 출발~
        else:
            rlt += w[-1]
            w.pop()
            t.pop()

    print(f'#{tc} {rlt}')

