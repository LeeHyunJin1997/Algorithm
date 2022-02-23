def erase(S):
    # 첫 문자를 비교할 때 에러를 방지하기 위해 항목을 하나 채움
    stack = [0]
    # 순서대로 넣다가
    for i in S:
        # 방금 들어간 애랑 지금 넣을 애랑 같으면
        if i == stack[-1]:
            # 이전에 있던 애도 들어내
            stack.pop()
        else:
            stack.append(i)

    # 처음에 임시로 넣은 애(인덱스 0) 다시 빼고
    stack.pop(0)
    return len(stack)

T = int(input())
for tc in range(1, T+1):
    S = input()
    print(f'#{tc} {erase(S)}')