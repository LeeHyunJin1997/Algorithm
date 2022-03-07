for tc in range(1, 11):
    T = int(input())
    # 후위 표기식으로 변경
    S = input()
    cal_stack = []
    tail = ''
    for i in range(len(S)):
        # * 만나면 스택 쌓기
        if S[i] == '*':
            cal_stack.append(S[i])
        # + 만나면 저장되어 있던 스택 붙이기
        # + 를 스택에 쌓기
        elif S[i] == '+':
            while cal_stack:
                tail += cal_stack.pop()
            cal_stack.append(S[i])
        # 연산자가 아니면 이어붙이기
        else:
            tail += S[i]

    # 남아있는 스택 이어붙이기
    for _ in range(len(cal_stack)):
        tail += cal_stack.pop()

    rlt = []
    for i in tail:
        if i == '*':
            temp1 = rlt.pop()
            temp2 = rlt.pop()
            rlt.append(temp2*temp1)
        elif i == '+':
            temp1 = rlt.pop()
            temp2 = rlt.pop()
            rlt.append(temp2+temp1)
        else:
            rlt.append(int(i))

    print(f'#{tc} {rlt[0]}')