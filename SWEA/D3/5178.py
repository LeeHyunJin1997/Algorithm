# 노드의 합
def make_tree():
    """
    BFS로 온전한 tree 구조(간선)을 생성
    :return: None
    """
    cnt = 1
    queue = [1]

    while True:
        if cnt > N - 1:
            break

        for _ in range(len(queue)):
            temp = queue.pop(0)

            cnt += 1
            tree[temp][0] = cnt
            queue.append(cnt)
            if cnt > N - 1:
                break

            cnt += 1
            tree[temp][1] = cnt
            queue.append(cnt)
            if cnt > N - 1:
                break


def cal(node):
    """
    해당 노드의 값을 계산하는 함수
    :param node: 현재 노드
    :return: 현재 노드의 값이 있을 때는 그대로 반환, 없을 때는 하위 노드의 합을 계산
    """
    if tree[node][2]:
        return tree[node][2]
    # 오른쪽 자식이 없는 경우
    elif not tree[node][1]:
        return cal(tree[node][0])
    else:
        return cal(tree[node][0]) + cal(tree[node][1])


T = int(input())
for tc in range(1, 1+T):
    # N 노드 개수, M 리프노드 개수, L 출력할 노드 번호
    N, M, L = map(int, input().split())
    leaves = [list(map(int, input().split())) for _ in range(M)]

    # 왼쪽 자식 노드, 오른쪽 자식 노드, 값 저장
    tree = [[0 for _ in range(3)] for _ in range(N + 1)]
    make_tree()

    # 리프노드에 값 저장
    for i in leaves:
        tree[i[0]][2] = i[1]

    print(f'#{tc} {cal(L)}')
