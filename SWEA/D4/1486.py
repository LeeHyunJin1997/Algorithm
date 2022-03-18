# 장훈이의 높은 선반

def subset(idx):
    if idx == len(bit):
        height_sum.append(sum(bit))
        return
    else:
        bit[idx] = 0
        subset(idx+1)
        bit[idx] = H[idx]
        subset(idx+1)


# B 이상인 탑 중에서 높이가 가잔 낮은 탑
T = int(input())
for tc in range(1, T+1):
    # N 점원 수, B 선반 높이
    N, B = map(int, input().split())
    # H 점원들의 키
    H = list(map(int, input().split()))

    bit = [0] * N
    # 각 조합의 합을 담을 리스트
    height_sum = []

    subset(0)

    min_val = 999999
    for i in height_sum:
        # temp 선반 높이와 탑 높이의 차
        temp = i - B
        if min_val > temp >= 0:
            min_val = temp

    print(f'#{tc} {min_val}')
