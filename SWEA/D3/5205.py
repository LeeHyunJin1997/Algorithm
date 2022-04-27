# 퀵정렬
def quick_sort(low, high):
    # 더이상 바꿀게 없다면 return
    if high <= low:
        return

    mid = partition(low, high)
    # partition 을 기준으로 분할 정렬
    quick_sort(low, mid-1)
    quick_sort(mid+1, high)


def partition(low, high):
    pivot = (low + high) // 2
    L = low
    R = high
    while L < R:
        # 피봇보다 작은 값을 찾으며 L 이동
        while L < R and A[L] < A[pivot]:
            L += 1
        # 피봇보다 크거나 같은 값을 찾으며 R 이동
        while L < R and A[pivot] <= A[R]:
            R -= 1

        # L, R이 서로 만나지 않고 정지했을 때
        if L < R:
            # R, L 값 교환
            A[R], A[L] = A[L], A[R]
            # pivot 좌측에 더이상 큰 값이 없으면
            if L == pivot:
                # 피봇을 옮겨
                pivot = R

    # L == R일 때는 피봇과 R(L) 값 바꿔
    A[pivot], A[R] = A[R], A[pivot]
    return R


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    quick_sort(0, len(A)-1)
    print(f'#{tc} {A[N//2]}')

