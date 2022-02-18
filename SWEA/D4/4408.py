# 자기방으로 돌아가기
def myMax(lst):
    max_val = 0
    for i in lst:
        if i > max_val:
            max_val = i
    return max_val

# 홀수방만 만들어
rooms_odd = [i for i in range(1, 400, 2)]

T = int(input())
for tc in range(1, T+1):
    # 돌아갈 학생수
    N = int(input())

    lst = [list(map(int, input().split())) for _ in range(N)]
    cnts = [0] * 200
    
    # 짝수 번째 방 번호에서 -1 해주면 홀수 번째와 idx(방 위치) 동일
    for i in lst:
        for j in range(2):
            if i[j] % 2 == 0:
                i[j] -= 1

        # 도착하는 방번호가 크도록 설정
        if i[0] > i[1]:
            i[0], i[1] = i[1], i[0]

        # 방 번호의 idx(위치)를 추출, 해당 위치에 대해 카운트
        start_idx = rooms_odd.index(i[0])
        end_idx = rooms_odd.index(i[1])
        for k in range(start_idx, end_idx+1):
            cnts[k] += 1

    print(f'#{tc} {myMax(cnts)}')