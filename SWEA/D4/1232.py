# 사칙연산
import sys
sys.stdin = open('input.txt')


def cal(node):
    """
    하위 노드들의 계산을 수행하는 함수
    :param node: 현재 노드
    :return: 각 단계에서 계산 결과
    """
    left_child = tree[node][0]
    right_child = tree[node][1]

    # 현재 노드가 리프노드 일때
    if tree[node][2].isdigit():
        return int(tree[node][2])

    elif tree[node][2] == '*':
        return cal(left_child) * cal(right_child)
    elif tree[node][2] == '/':
        return cal(left_child) / cal(right_child)
    elif tree[node][2] == '+':
        return cal(left_child) + cal(right_child)
    elif tree[node][2] == '-':
        return cal(left_child) - cal(right_child)


T = 10
for tc in range(1, T+1):
    # N 노드 수
    N = int(input())
    edges = [list(input().split()) for _ in range(N)]

    # [왼쪽 자식노드, 오른쪽 자식노드, 값]
    tree = [[0 for _ in range(3)] for _ in range(N + 1)]

    # edges로 받아온 입력을 tree에 맞는 형태로 옮김
    for i in range(len(edges)):
        if len(edges[i]) == 4:
            tree[int(edges[i][0])][0] = int(edges[i][2])
            tree[int(edges[i][0])][1] = int(edges[i][3])
            tree[int(edges[i][0])][2] = edges[i][1]
        elif len(edges[i]) == 2:
            tree[int(edges[i][0])][2] = edges[i][1]

    print(f'#{tc} {int(cal(1))}')

