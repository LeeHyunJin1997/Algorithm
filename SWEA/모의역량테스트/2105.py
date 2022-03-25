# 디저트 카페

# n 회전 횟수, ci, cj 현위치, visited 지나친 좌표, cnt 먹은 디저트 종류
def DFS(n, ci, cj, visited, cnt):
    global si, sj, max_val
    # 방향회전 2번했는데 최대치 반도 못 먹었으면 의미없어!
    if n==2 and max_val>=cnt*2:
        return
    # 방향회전을 4회했을 때 종료(의미 없음)
    if n > 3:
        return
    # 시작점으로 돌아왔고, 현재 정답보다 많이 먹었을 때
    if n == 3 and ci==si and cj==sj and max_val<cnt:
        max_val = cnt
        return

    # 직진(k=n) 혹은 방향 전환(k=n+1)
    for k in range(n, n+2):
        ni, nj = ci+di[k], cj+dj[k]
        # 배열의 범위 내인지, 중복 인지 체크
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] not in visited:
            visited.append(arr[ni][nj])
            DFS(k, ni, nj, visited, cnt+1)
            visited.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 정답 저장, 정답이 없을땐 -1
    max_val = -1
    # 대각선으로 움직이는 방향
    # k + 1 이 되어 인덱스 에러가 나는 것을 방지하기 위해 의미없는 5번째 값 삽입
    di, dj = (1,1,-1,-1,0),(-1,1,1,-1,0)

    # i, j에서 시작
    for si in range(0, N-2):
        for sj in range(1, N-1):
            DFS(0, si, sj, [], 0)

    print(f'#{tc} {max_val}')