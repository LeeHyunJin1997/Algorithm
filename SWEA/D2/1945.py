# 간단한 소인수분해
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 소인수분해할 인수들
    lst = [2, 3, 5, 7, 11]
    cnts = [0] * 5

    for i in range(len(lst)):
        # 각 인수로 나누어떨어질 때
        while N % lst[i] == 0:
            # cnts 에 저장
            cnts[i] += 1
            # 나눈 몫을 N 에 재할당
            N //= lst[i]

    print(f'#{tc}', end=' ')
    print(' '.join(map(str, cnts)))