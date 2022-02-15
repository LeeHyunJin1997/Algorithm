T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    paris = []

    for _ in range(N):
        paris.append(list(map(int, input().split())))

    max_val = 0

    for r in range(N+1-M):
        for c in range(N+1-M):
            total = 0
            
            for r_M in range(M):
                for c_M in range(M):
                    total += paris[r+r_M][c+c_M]

            if total > max_val:
                max_val = total

    print(f'#{tc} {max_val}')