# subtree
def count(node):
    """
    하위 노드 개수를 세는 함수
    :param node: 현재 노드
    :return: None
    """
    global cnt
    if node:
        cnt += 1
        count(tree[node][0])
        count(tree[node][1])


T = int(input())
for tc in range(1, T+1):
    # E 간선 개수, N 노드 개수
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))

    tree = [[0, 0, 0] for _ in range(E+2)]

    for i in range(0, len(edges)-1, 2):
        parent_node = edges[i]  # 현재노드, 부모노드
        child_node = edges[i + 1]  # 자식노드

        if tree[parent_node][0] == 0:
            tree[parent_node][0] = child_node

        else:
            tree[parent_node][1] = child_node

        tree[child_node][2] = parent_node

    cnt = 0

    count(N)

    print(f'#{tc} {cnt}')
