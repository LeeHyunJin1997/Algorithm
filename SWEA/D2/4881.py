def arrMin(r):
    global each_sum
    global rlt
    # 이번 합계가 결과보다 커지면 더 돌 필요없어
    if rlt < each_sum:
        return

    # 끝까지 갔으면 종료
    if r == N:
        # 이번 합이 결과보다 작을 때는 덮어씌우기
        if each_sum < rlt:
            rlt = each_sum
        return

    # 열 순회
    for c in range(N):
        # 해당 열 선택 안했으면
        if not select[c]:
            # 선택했다치고
            select[c] = 1
            each_sum += arr[r][c]
            # 다음 행 진행해봐
            arrMin(r+1)
            # 다시 안한걸로 해
            select[c] = 0
            each_sum -= arr[r][c]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr =[list(map(int, input().split())) for _ in range(N)]

    # 선택한 column 은 1로 표시
    select = [0] * N

    rlt = 1000
    each_sum = 0

    # 행 인덱스 0부터 시작
    arrMin(0)

    print(f'#{tc} {rlt}')

