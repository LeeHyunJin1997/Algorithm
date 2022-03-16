# 노드의 거리
T = int(input())
for tc in range(1, T+1):
    # V 노드 개수, E 간선 개수
    V, E = map(int, input().split())
    links = [list(map(int, input().split())) for _ in range(E)]
    # S 출발 노드, G 도착노드
    S, G = map(int, input().split())
    # 노드 개수만큼의 빈 리스트
    lines = [list() for _ in range(V+1)]
    Q = [S]

    # lines 각 인덱스에 연결된 노드를 저장
    for i in links:
        lines[i[0]].append(i[1])
        lines[i[1]].append(i[0])

    cnt = -1
    end = False

    while True:
        if end:
            print(f'#{tc} {cnt}')
            break

        if not Q:
            print(f'#{tc} {0}')
            break

        for j in range(len(Q)):
            temp = Q.pop(0)

            if temp == G:
                end = True
                break

            for i in range(len(lines[temp])):
                Q.append(lines[temp][i])

            lines[temp] = []

        cnt += 1
