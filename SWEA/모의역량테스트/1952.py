# 수영장

# n 월수(종료조건), ssum 비용합
def DFS(n, ssum):
    global min_val
    # 종료조건 (12개월)
    if n > 12:
        # 종료되었을 때 최솟값 갱신
        if min_val > ssum:
            min_val = ssum
        return

    DFS(n+1, ssum+lst[n]*day)   # 일일권: 한달 증가, +일수*일일권 가격
    DFS(n+1, ssum+mon)          # 월간: 한달 증가, + 1달권 가격
    DFS(n+3, ssum+mon3)         # 3달: 3달 증가, + 3달권 가격
    DFS(n+12, ssum+year)        # 년간: 12달 증가, +1년권 가격

T = int(input())
for tc in range(1, 1+T):
    day, mon, mon3, year = map(int, input().split())
    # 월별 이용계획, 인덱스와 월 맞춰줌
    lst = [0] + list(map(int, input().split()))
    min_val = 12345678

    DFS(1, 0)
    print(f'#{tc} {min_val}')
