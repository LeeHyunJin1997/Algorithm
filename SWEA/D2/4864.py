T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    is_in = 0

    # str2를 str1 길이만큼 남기고 순회
    for i in range(len(str2)-len(str1)+1):
        # 첫글자가 나오면 비교 시작
        if str1[0] == str2[i]:
            # 끝까지 비교
            if str1 == str2[i:i+len(str1)]:
                is_in = 1
    
    print(f'#{tc} {is_in}')
