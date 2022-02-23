def cases():
    global memo
    # 2단계 전 * 2 + 1단계 전
    memo.append(memo[-2]*2 + memo[-1])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # N은 10일 때 1, 20일 때 3
    memo = [1, 3]
    # 10, 20일 때가 주어져 있으니 30부터 적용
    # 추가분만큼 반복하여 memo를 늘려나감
    for _ in range(N//10-2):
        cases()

    print(f'#{tc} {memo[N//10 - 1]}')