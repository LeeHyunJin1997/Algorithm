T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    max_cnt = 0

    # str1 에 있는 각 문자들을
    for i in str1:
        cnt = 0

        # str2 에서 찾아
        for j in str2:
            # 같으면 +1
            if i == j:
                cnt += 1

        if max_cnt < cnt:
            max_cnt = cnt

    print(f'#{tc} {max_cnt}')