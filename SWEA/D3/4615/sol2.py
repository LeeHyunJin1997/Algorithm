# 재미있는 오셀로 게임

T = int(input())
for tc in range(1, 1+T):
    N, M = map(int, input().split())
    arr = [[0]*(N+1) for _ in range(N+1)]
    # 초기 톨 세팅
    arr[N//2][N//2] = arr[N//2+1][N//2+1] = 2
    arr[N//2+1][N//2] = arr[N//2][N//2+1] = 1

    for _ in range(M):
        sj, si, d = map(int, input().split())
        arr[si][sj] = d
        # 8방향으로
        for di, dj in ((-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1),(0,-1),(0,1)):
            s = []
            # 쭉 나아가면 확인
            for k in range(1, N):
                ni, nj = si+di*k, sj+dj*k
                # 범위 체크
                if 1<=ni<=N and 1<=nj<=N:
                    # 0 나오면 안봐도돼
                    if arr[ni][nj] == 0:
                        break
                    # 같은 돌인 때는
                    elif arr[ni][nj] == d:
                        # 뒤집어!
                        for ci,cj in s:
                            arr[ci][cj] = d
                        break
                    # 다른 돌이면 적어놔
                    else:
                        s.append((ni,nj))
                    
                else:
                    break
    
    # 개수 세기
    bcnt = wcnt = 0
    for lst in arr:
        bcnt += lst.count(1)
        wcnt += lst.count(2)

    print(f'#{tc} {bcnt} {wcnt}')




