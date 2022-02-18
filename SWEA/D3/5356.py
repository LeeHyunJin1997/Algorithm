T = int(input())
for tc in range(1, T+1):
    lst = [input() for _ in range(5)]

    # 문자열 최대 길이 계산
    max_len = 0
    for i in lst:
        if len(i) > max_len:
            max_len = len(i)
    
    # 리스트 안의 각 문자열이
    for i in range(len(lst)):
        # 최대길이보다 짧을 때
        if len(lst[i]) < max_len:
            # 짧은 만큼을 _ 로 채움
            lst[i] += '_' * (max_len - len(lst[i]))


    rlt = ''
    for j in range(max_len):
        for i in lst:
            if i[j] == '_':
                continue
            else:
                rlt += i[j]
    
    print(f'#{tc} {rlt}')