import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    # 양쪽 벽에 0 으로 이루어진 열 삽입
    ladder = [[0] + list(map(int, input().split())) + [0] for i in range(100)]

    min_cnt = 999999999
    rlt = 0

    for c in range(1, len(ladder[0])-1):
        if ladder[0][c] == 0:
            continue
        
        cnt = 0
        # 시작점
        start = c-1

        # 내려가다가
        for r in range(len(ladder)):
            cnt += 1
            
            # 왼쪽 막대를 만나면
            if ladder[r][c-1] == 1:
                # 왼쪽으로 쭉가
                while True:
                    c -= 1
                    cnt += 1
                    # 0을 만나면 관둬
                    if ladder[r][c-1] == 0:
                        break

            # 오른쪽 막대를 만나면
            elif ladder[r][c+1] == 1:
                # 오른쪽으로 쭉가
                while True:
                    c += 1
                    cnt += 1
                    # 0을 만나면 관둬
                    if ladder[r][c+1] == 0:
                        break

        if cnt < min_cnt:
            min_cnt = cnt
            rlt = start
    
    print(f'#{tc} {rlt}')