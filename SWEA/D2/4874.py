T = int(input())
for tc in range(1, T+1):
    stack = []
    code = input().split()

    print(f'#{tc}', end=' ')

    try:
        for i in code:                          # 주어진 코드를 순회하면서
            if i == '.':                        # 마침표 만나면 종료
                if len(stack) > 1:              # 스택에 2개이상의 숫자 남았다면
                    print('error')              # 잘못된 코드
                    break
                else:
                    print(stack.pop())          # 아니라면 top 출력 후 종료
                    break
            elif i.isdigit():                   # 숫자일 경우 push
                stack.append(int(i))
            else:                               # 연산자일 경우
                p2 = stack.pop()                # 먼저 pop 되는 숫자가 연산 뒤에 적용
                p1 = stack.pop()
                if i == '+':                    # 연산결과를 push
                    stack.append(p1 + p2)
                elif i == '*':
                    stack.append(p1 * p2)
                elif i == '-':
                    stack.append(p1 - p2)
                elif i == '/':
                    stack.append(int(p1 / p2))  # float 결과 방지 (나누어떨어짐)

    # 연산이 불가능할 경우 error 출력
    except:
        print('error')
