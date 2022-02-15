# 절반 부분을 구하는 함수
def half(start, end):
    return int((start+end)/2)


# 정답을 찾는 횟수를 구하는 함수
def find(start, end, target_page, cnt=0):
    # 절반부분이 목표 페이지일 때
    if half(start, end) == target_page:
        # 한번 더 세고 반환
        cnt += 1
        return cnt
    # 절반 부분이 찾는 부분보다 크다면
    elif half(start, end) > target_page:
        cnt += 1
        # 절반 부분을 end 에 두고 다시 찾아
        return find(start, half(start,end), target_page, cnt)
    else:
        cnt += 1
        return find(half(start, end), end, target_page, cnt)


T = int(input())
for tc in range(1, T+1):
    # P = 전체쪽수, Pa = A가 찾을 쪽, Pb = B가 찾을 쪽
    P, Pa, Pb = map(int, input().split())

    # A와 B가 목표 페이지를 찾는 데 걸린 횟수
    A = find(1, P, Pa)
    B = find(1, P, Pb)

    # 더 짧은 사람이 이김
    print(f'#{tc} ', end='')
    if A < B:
        print('A')
    elif A == B:
        print(0)
    else:
        print('B')
