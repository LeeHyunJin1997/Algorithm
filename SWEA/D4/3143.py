T = int(input())
for tc in range(1, T+1):
    A, B = input().split()

    i = 0
    # B 의 등장횟수
    cnt = 0
    # 인덱스 에러가 나지 않을 만큼 A 순회 
    while i < len(A)-len(B)+1:
        # B를 만나면
        if A[i:i+len(B)] == B:
            # 하나 세고 다음 문자로 점프!
            cnt += 1
            i += len(B)
        else:
            i += 1

    # 타이핑 최솟값은 전체 문자길이 - C 등장 횟수 * B 칠 때 단축되는 길이
    min_tab = len(A) - cnt * (len(B) - 1)
    print(f'#{tc} {min_tab}')

