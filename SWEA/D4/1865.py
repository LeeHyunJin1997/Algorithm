# 동철이의 일 분배
def DFS(r, now_p):
    global max_p

    # 마지막 행까지 돌았을 때 최댓값 갱신
    if r == N:
        if now_p > max_p:
            max_p = now_p
        return

    # 다 돌지도 않았는데 벌써 값이 작다면 가지치기
    if max_p >= now_p:
        return

    for c in range(N):
        if not visited[c]:
            visited[c] = 1
            DFS(r+1, now_p * (arr[r][c]/100))
            visited[c] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    max_p = 0

    DFS(0, 1)

    print(f'#{tc} {max_p*100:0.6f}')