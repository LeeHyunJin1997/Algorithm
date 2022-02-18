# 스도쿠 검증

# 행 검증
def isRow(arr):
    is_true = [0] * 9

    for i in range(9):
        # 숫자에 해당하는 칸(인덱스)에 카운트
        cnts = [0] * 10
        for j in range(9):
            cnts[arr[i][j]] += 1

        # 숫자별로 전부 1이 채워졌으면 그 행은 검증 완료
        if all(cnts[1:10]):
            is_true[i] += 1
    
    # 모든 행이 완료라면 True
    if all(is_true):
        return True
    else:
        return False

# i, j만 바꾼 열 검증
def isCol(arr):
    is_true = [0] * 9

    for j in range(9):
        # 숫자에 해당하는 칸(인덱스)에 카운트
        cnts = [0] * 10
        for i in range(9):
            cnts[arr[i][j]] += 1

        # 숫자별로 전부 1이 채워졌으면 그 행은 검증 완료
        if all(cnts[1:10]):
            is_true[j] += 1
    
    # 모든 행이 완료라면 True
    if all(is_true):
        return True
    else:
        return False

# 3x3 칸 검증
def isBlock(arr):
    dr = [0, 0, 0, 1, 1, 1, 2, 2, 2]
    dc = [0, 1, 2, 0, 1, 2, 0, 1, 2]
    is_true = 0
    # i,j 는 0, 3, 6
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            cnts = [0] * 10
            # 델타를 이용해 3x3 확인
            for k in range(9):
                cnts[arr[i+dr[k]][j+dc[k]]] += 1
            if all(cnts[1:10]):
                is_true += 1
    
    # 모두 True라 9가 되면
    if is_true == 9:
        return True
    else:
        return False


T = int(input())
for tc in range(1,1+T):
    # 9x9 퍼즐
    arr = [list(map(int, input().split())) for _ in range(9)]

    rlt = int(isRow(arr) and isCol(arr) and isBlock(arr))

    print(f'#{tc} {rlt}')