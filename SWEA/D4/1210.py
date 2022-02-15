# 전체 리스트와 뒤에서부터 x번 째 단계, 위치 인덱스 y를 인자로 받는 함수
def check(ladders, x, y):
    # 위치가 양쪽 끝 사다리라면, 확인 가능한 쪽만 진행
    if y == 99:
        # 옆으로 건너갈 다리를 만나면
        if ladders[x][y-1] == 1:
            while True:
                # 0 이면 멈춰
                if y == 0:
                    break
                # 쭉 가
                elif ladders[x][y-1] == 1:
                    y = y - 1
                else:
                    break
    elif y == 0:
        if ladders[x][y+1] == 1:
            while True:
                if y == 99:
                    break
                elif ladders[x][y+1] == 1:
                    y = y + 1
                else:
                    break
    else:
        if ladders[x][y+1] == 1:
            while True:
                if y == 99:
                    break
                elif ladders[x][y+1] == 1:
                    y = y + 1
                else:
                    break
        elif ladders[x][y-1] == 1:
            while True:
                if y == 0:
                    break
                elif ladders[x][y-1] == 1:
                    y = y - 1
                else:
                    break

    return y

for i in range(10):
    # 테스트 케이스 번호 N
    N = int(input())
    ladders = []

    for i in range(100):
        ladders.append(list(map(int, input().split())))

    # 도착점 번호 특정
    finish = ladders[-1].index(2)

    # check 후 이동 100번 반복
    y = finish
    for i in range(100):
        y = check(ladders, -(i+1), y)

    print(f'#{N} {y}')