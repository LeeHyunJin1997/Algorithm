# 이진 탐색

# l 시작 인덱스, r 끝 인덱스, num 찾는 숫자, select 좌우선택여부
def bin(l, r, num, select):
    m = (l + r) // 2

    # 값을 못 찾았을 경우
    if l == r and A[m] != num:
        return False

    # 값을 찾았을 경우
    if A[m] == num:
        return True
    # 찾는 값보다 작으면 오른쪽 구간 선택
    elif A[m] < num:
        # 이 전에도 오른쪽을 선택했으면 False
        if select == 1:
            return False
        else:
            return bin(m+1, r, num, 1)
    # 찾는 값보다 크면 왼쪽 구간 선택
    else:
        # 이 전에도 왼쪽을 선택했으면 False
        if select == -1:
            return False
        else:
            return bin(l, m-1, num, -1)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0

    # B에 있는 수를 탐색
    for i in B:
        if bin(0, N-1, i, 0):
            cnt += 1

    print(f'#{tc} {cnt}')