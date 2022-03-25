# 정식이의 은행업무
def solve(lst3):
    for i in range(len(lst2)):
        # 각 자리에서 1->0, 0->1 
        lst2[i] = (lst2[i]+1) % 2

        # 10진수로 변환
        dec = 0
        for idx in range(len(lst2)):
            dec = dec*2 + lst2[idx]

        # 3진수로 변환
        s = []
        ret = dec 
        while dec > 0:
            s.append(dec%3)
            dec //= 3
        lst = lst3[::-1]

        cnt = 0
        for idx in range(min(len(s), len(lst))):
            if s[idx] != lst[idx]:
                cnt += 1
        # 길이가 다른만큼도 체크
        cnt += abs(len(s)-len(lst))

        if cnt == 1:
            return ret

        # 원래대로 복구
        lst2[i] = (lst2[i]+1) % 2 


T = int(input())
for tc in range(1, 1+T):
    lst2 = list(map(int, input()))
    lst3 = list(map(int, input()))

    ans = solve(lst3)
    print(f'#{tc} {ans}')