# 세제곱근을 찾아라
T = int(input())
for tc in range(1, 1+T):
    N = int(input())

    for i in range(1, N+1):
        if i ** 3 == N:
            print(f'#{tc} {i}')
            break
        elif i ** 3 > N:
            print(f'#{tc} {-1}')
            break

