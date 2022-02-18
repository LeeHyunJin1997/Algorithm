# 쇠막대 자르기
T = int(input())
for tc in range(1, T+1):
    N = input()
    # 현재 레이저에 걸리는 쇠막대 수
    cnt = 0
    sol = 0

    for i in range(len(N)):
        # ( 만나면 쇠막대 생성
        if N[i] == '(':
            cnt += 1
        # ) 만났는데
        else:
            # 레이저였다면
            if N[i-1] == '(':
                # 쇠막대 아니었으니 하나 빼주고
                cnt -= 1
                # 중첩되어 있는 만큼 조각 생김
                sol += cnt
            # 레이저가 아니면
            else:
                # 쇠막대 소멸
                cnt -= 1
                # 쇠막대 끄트머리 세주기
                sol += 1
                
    print(f'#{tc} {sol}')