# 터렛
T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    # 반지름이 더 큰 원을 r2로 고정
    if r1 > r2 :
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        r1, r2 = r2, r1

    # 두 점 사이의 거리 d
    d = pow(((x2-x1)**2 + (y2-y1)**2), 0.5)

    # 두 점의 좌표, 거리가 모두 같아 만나는 점이 무수히 많을 때
    if x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    # 원1의 중심이 원2 위에 있을 때
    elif d == r2:
        print(2)
    # 두 원이 떨어져 있을 때
    elif d > r2:
        # 두 점에서 만날 경우
        if r1 + r2 > d:
            print(2)
        # 외접할 경우
        elif r1 + r2 == d:
            print(1)
        # 만나지 않을 경우
        elif r1 + r2 < d:
            print(0)
    # 원2 안에 원1이 들어있을 때
    elif d < r2:
        # 두 점에서 만날 경우
        if r1 + d > r2:
            print(2)
        # 내접할 경우
        elif r1 + d == r2:
            print(1)
        # 만나지 않을 경우
        elif r1 + d < r2:
            print(0)
    # 생각하지 못한 경우
    else:
        print('원 위치 설정이 잘못되었습니다.')