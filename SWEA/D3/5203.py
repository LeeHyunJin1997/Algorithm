# 베이비진 게임

def check(player):
    count = [0] * 12
    for k in player:
        count[k] += 1

    # 9, 0, 1을 비교하기 위해 count 연장
    count[10], count[11] = count[0], count[1]

    for j in range(len(count) - 2):
        # 연이은 숫자가 1개 이상일 때
        if count[j] >= 1 and count[j + 1] >= 1 and count[j + 2] >= 1:
            return True
        # 한 숫자가 3개 이상일 때
        if count[j] >= 3:
            return True

    # 해당 하지 않으면
    else:
        return False


T = int(input())
for tc in range(1, T+1):
    cards = list(map(int, input().split()))
    # A 플레이어1 B 플레이어2
    A = []
    B = []

    rlt = 0
    for i in range(len(cards)):
        # 한장씩 나눠줘
        if i % 2:
            B.append(cards[i])
        else:
            A.append(cards[i])

        # 3장도 안 되면 카드 계속 받아
        if len(A) < 3 and len(B) < 3:
            continue

        # A만 먼저 3장을 받았을 때는 A만 체크
        if len(A) == 3 and len(B) == 2:
            if check(A):
                rlt = 1
                print(f'#{tc} {1}')
                break

        else:
            if check(A):
                rlt = 1
                print(f'#{tc} {1}')
                break

            if check(B):
                rlt = 1
                print(f'#{tc} {2}')
                break

    if rlt == 0:
        print(f'#{tc} {rlt}')
