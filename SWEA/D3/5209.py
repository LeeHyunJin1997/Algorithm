# 최소 생산 비용
def DFS(r, now_sum):
    global min_val
    # 끝 행에 도달하면 최솟갑을 갱신하고 리턴
    if r == N:
        if min_val > now_sum:
            min_val = now_sum
        return

    # 가지치기, 현재 합이 이미 최솟갑을 넘어서면 볼 필요없음
    if min_val < now_sum:
        return

    for c in range(N):
        # 선택 안한 열에 한해
        if not visited[c]:
            # 선택하고 다음 행 진행
            visited[c] = 1
            DFS(r+1, now_sum + arr[r][c])
            # 다음 열을 위해 원래대로 복구
            visited[c] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 이미 사용한 줄을 체크
    visited = [0] * N

    min_val = 99999999

    DFS(0, 0)

    print(f'#{tc} {min_val}')