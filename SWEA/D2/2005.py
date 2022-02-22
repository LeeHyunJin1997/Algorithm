# pascal 함수는 선언된 리스트에 다음 줄을 이어붙임
def pascal():
    global lst
    # 마지막 줄보다 길이를 1 늘린 리스트 (양쪽 끝에 1)
    temp = [1] + [0] * (len(lst[-1])-1) + [1]
    # 새로 생긴 줄의 각 항목은 전 줄의 i-1과 i의 합
    for i in range(1, len(temp)-1):
        temp[i] = lst[-1][i-1] + lst[-1][i]
    lst.append(temp)

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    # 첫 줄은 항상 1
    lst = [[1]]

    # pascal 함수를 N-1번 반복
    for _ in range(N-1):
        pascal()

    print(f'#{tc}')
    for i in lst:
        for j in i:
            print(j, end=' ')
        print('')



