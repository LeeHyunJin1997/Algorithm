def mySum(lst):
    total = 0
    for i in lst:
        total += i
    return total

# A는 1~12
A = [i for i in range(1, 13)]

T = int(input())
for tc in range(1, T+1):

    # N = 원소의 수, K = 부분집합의 합
    N, K = map(int, input().split())

    n = len(A)
    cnt = 0

    for i in range(1 << n):
        sets = []

        # 부분집합 생성
        for j in range(n):
            if i & (1 << j):
                sets.append(A[j])

        # 길이가 N이고 값의 합이 K일때
        if len(sets) == N and mySum(sets) == K:
            cnt += 1

    print(f'#{tc} {cnt}')


