# 계산기 3
T = 10
for tc in range(1, T+1):
    # 후위표기식 변환
    N = int(input())
    S = list(input())
    stack = []
    rlt = ''

    icp = {'*': 2, '+': 1, '(': 3}  # 넣을때
    isp = {'*': 2, '+': 1, '(': 0}  # 스택안

    for i in S:
        # 숫자라면 바로 넣고
        if i.isdigit():
            rlt += i
        # 스택이 빈 경우
        elif not stack:
            stack.append(i)

        # 닫는 괄호를 만나면
        elif i == ')':
            # 여는 괄호를 꺼낼 때까지 이어붙이기
            while stack[-1] != '(':
                rlt += stack.pop()
            stack.pop()

        # 우선순위가 큰게 들어올 때
        elif icp[i] > isp[stack[-1]]:
            stack.append(i)

        else:
            # 우선순위가 작은게 들어올 때
            while icp[i] <= isp[stack[-1]]:
                rlt += stack.pop()
            stack.append(i)

    # 남은 스택이 있다면 전부 붙이기
    while stack:
        temp = stack.pop()
        if temp != '(':
            rlt += temp

    # ------- 후미표기식 이용해 계산 --------
    nums = []

    for j in rlt:
        # 숫자라면 바로 넣기
        if j.isdigit():
            nums.append(int(j))
        # 연산자라면
        elif j == '+':
            p2 = nums.pop()
            p1 = nums.pop()
            nums.append(p1 + p2)
        elif j == '*':
            p2 = nums.pop()
            p1 = nums.pop()
            nums.append(p1 * p2)

    print(f'#{tc} {nums[0]}')
