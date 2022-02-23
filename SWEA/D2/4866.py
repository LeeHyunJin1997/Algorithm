def check(S):
    # 바로 stack[-1]과 비교하면 오류나니 미리 채워넣기
    stack = [0]
    for i in S:
        # 여는 괄호 만나면 스택 쌓기
        if i == '(' or i == '{':
            stack.append(i)
        # 닫는 괄호 만났을 때 바로 전에 넣은것이 여는 괄호면
        # 쌍으로 삭제
        if i == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                return False
        if i == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                return False

    # 미리 채워넣었던 것 삭제
    stack.pop(0)

    if len(stack) == 0:
        return True
    else:
        return False


T = int(input())
for tc in range(1, T+1):
    S = input()
    print(f'#{tc} {int(check(S))}')