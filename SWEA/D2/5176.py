# 이진탐색
def make_tree():
    """
    BFS로 tree 의 간선을 생성
    :return: None
    """
    cnt = 1
    Q = [1]

    while True:
        if cnt > N-1:
            break

        for _ in range(len(Q)):
            temp = Q.pop(0)

            cnt += 1
            tree[temp][0] = cnt
            Q.append(cnt)
            if cnt > N-1:
                break

            cnt += 1
            tree[temp][1] = cnt
            Q.append(cnt)
            if cnt > N-1:
                break


def inorder(node):
    """
    중위순회하며 값을 저장하는 함수
    :param node: 노드 번호
    :return: None
    """
    global num
    if node:
        inorder(tree[node][0])
        tree[node][2] = num
        num += 1
        inorder(tree[node][1])


T = int(input())
for tc in range(1, T+1):
    # N 노드 개수
    N = int(input())

    # 왼쪽 자식 노드, 오른쪽 자식 노드, 값 저장
    tree = [[0 for _ in range(3)] for _ in range(N+1)]

    make_tree()

    num = 1
    inorder(1)

    # 루트(1번 노드)에 저장된 값과 N//2 번 노드에 저장된 값 출력
    print(f'#{tc} {tree[1][2]} {tree[N//2][2]}')