# 격자판의 숫자 이어붙이기

# n 선택한 숫자 개수, ci, cj 현시점 좌표, num 만들어낸 숫자
def DFS(n, ci, cj, num):
    # 숫자 7개 채우면 종료
    if n == 7:
        sset.add(num)
        return
    # 상하좌우 네 방향 만들기
    for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni, nj = ci+di, cj+dj
        # 이동할 방향이 격자 범위 내라면
        if 0<=ni<4 and 0<=nj<4:
            DFS(n+1, ni, nj, num*10+arr[ni][nj])


T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    # 경우의 수 중복제거를 위한 sset
    sset =set()
    for i in range(4):
        for j in range(4):
            DFS(0, i, j, 0)

    print(f'#{tc} {len(sset)}')