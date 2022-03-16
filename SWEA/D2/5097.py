# 회전
T = int(input())
for tc in range(1, T+1):
    # N 리스트 길이, M 이동 횟수
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    rlt = lst[M % len(lst)]
    print(f'#{tc} {rlt}')