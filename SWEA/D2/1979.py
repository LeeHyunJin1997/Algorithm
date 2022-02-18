T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    # NxN 배열 입력, 우측과 하단 끝에 0 배치
    arr = [list(map(int, input().split())) + [0] for _ in range(N)]
    arr.append([0]*(N+1))

    print(arr)
    # 결과
    sol = 0

    # 행 검사
    for i in range(N+1):
        cnt = 0
        for j in range(N+1):
            # 1 을 만나면 길이(cnt) +1
            if arr[i][j] == 1:
                cnt += 1
            # 0 을 만나면 길이가 K 와 같은지 확인, cnt 초기화
            else:
                if cnt == K:
                    sol += 1
                cnt = 0
    
    # 열 검사
    for j in range(N+1):
        cnt = 0
        for i in range(N+1):
            # 1 을 만나면 길이(cnt) +1
            if arr[i][j] == 1:
                cnt += 1
            # 0 을 만나면 길이가 K 와 같은지 확인, cnt 초기화
            else:
                if cnt == K:
                    sol += 1
                cnt = 0
    
    print(f'#{tc} {sol}')