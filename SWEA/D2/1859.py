# 백만장자 프로젝트
import sys
sys.stdin = open('input.txt')

# Max 값의 인덱스 반환
def myMax(lst):
    max_idx = None
    max_val = 0
    for i in range(len(lst)):
        if max_val < lst[i]:
            max_val = lst[i]
            max_idx = i
    return max_idx

T = int(input())
for tc in range(1, T+1):
    # N 일동안 매매
    N = int(input())
    # 매매가 리스트
    lst = list(map(int, input().split()))
    
    total = 0

    # lst 에 아무것도 없을 때까지 반복
    while len(lst) > 0:
        # lst 에서 Max 값의 idx 저장
        high_idx = myMax(lst)
        # 최고점까지 구간 분리
        temp = lst[0:high_idx+1]
        # 해당 구간에서 취할 수 있는 이익 계산
        total += (len(temp)-1)*temp[-1] - sum(temp[:-1])
        # lst 에는 분리해낸 구간 이후를 재할당
        lst = lst[high_idx+1:]

    print(f'#{tc} {total}')
