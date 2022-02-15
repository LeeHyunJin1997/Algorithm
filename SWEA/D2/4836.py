T = int(input())

for tc in range(1, 1+T):
    N = int(input())

    nums = []
    red = set()
    blue = set()

    # 칠할 영역
    for _ in range(N):
        nums.append(list(map(int, input().split())))

    for i in nums:
        # 색상이 빨강이라면
        if i[-1] == 1:
            # 두 점 사이에 있는 좌표를 set 에 저장
            for j in range(i[0], i[2]+1):
                for k in range(i[1], i[3]+1):
                    red.add((j, k))

        # 파랑일 때
        else:
            for j in range(i[0], i[2]+1):
                for k in range(i[1], i[3]+1):
                    blue.add((j, k))

    # 빨강과 파랑의 교집합의 수를 출력
    print(f'#{tc} ', end='')
    print(len(red & blue))