# 테스트 케이스 개수
T = int(input())
for test_case in range(T):

    # N*N 행렬
    N = int(input())
    # 주어진 행렬
    warehouse = []

    for _ in range(N):
        warehouse.append(list(map(int, input().split())))

    non_zero = []

    # 각 줄에서 0이 아닌 수가 연속된 개수 세기 ex) [3,0,0,5]
    for i in range(len(warehouse)):
        cnt_list = []
        cnt = 0
        for j in range(len(warehouse[i])):
            if warehouse[i][j] != 0:
                cnt += 1
                if j == len(warehouse[i])-1:
                    cnt_list.append(cnt)
            else:
                cnt_list.append(cnt)
                cnt = 0
        non_zero.extend(cnt_list)

    # 각 항목의 개수 세기, 0 제거, 중복 제거
    rects = set()

    for i in non_zero:
        if i == 0:
            pass
        else:
            rects.add((non_zero.count(i), i))

    rects = list(rects)

    # 크기 작은 순 정렬, 사이즈가 같은 경우 행이 작은 순
    rects.sort(key=lambda x : (x[0]*x[1], x[0]))

    # 출력부
    print(f'#{test_case+1}', end=' ')
    print(len(rects), end=' ')
    for i in rects:
        for j in i:
            print(j, end=' ')
    print('')
