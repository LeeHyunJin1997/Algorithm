# 전기버스2

T = int(input())
for tc in range(1, T+1):
    lst = list(map(int, input().split()))
    # 정류장 수
    N = lst[0]

    queue = [1]
    cnt = 0
    fin = False

    while queue:
        for _ in range(len(queue)):
            now = queue.pop(0)

            # 현재 정류장에서 갈 수 있는 모든 정류장 추가
            for i in range(1, lst[now]+1):
                # 종점에 갈 수 있다면
                if now+i >= N:
                    fin = True
                    break
                queue.append(now+i)

            if fin:
                break

        if fin:
            break

        cnt += 1

    print(f'#{tc} {cnt}')
