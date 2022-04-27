# 연산
from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    visited = set()
    queue = deque()
    queue.append(N)
    cnt = 0
    fin = 0

    while queue:
        for _ in range(len(queue)):
            temp = queue.popleft()

            # 백만이하의 자연수가 아니라면 넘어가
            if temp < 1 or 1000000 < temp:
                continue

            # 정답이라면
            if temp == M:
                fin = 1
                break

            # 연산을 계속 해야 한다면
            if temp not in visited:
                visited.add(temp)
                queue.append(temp-1)
                queue.append(temp-10)
                queue.append(temp+1)
                queue.append(temp*2)

        if fin:
            break

        cnt += 1

    print(f'#{tc} {cnt}')
