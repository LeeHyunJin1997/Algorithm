# 이진 힙
def make_tree():
    """
    BFS로 tree의 간선을 생성
    :return: None
    """
    cnt = 1
    queue = [1]

    while True:
        if cnt > N:
            break

        for _ in range(len(queue)):
            temp = queue.pop(0)

            if cnt > N:
                break

            # 좌우 자식에게 반복
            for i in range(2):
                cnt += 1
                if cnt > N:
                    break

                tree[temp][i] = cnt
                queue.append(cnt)
                tree[cnt][2] = temp


def compare(node):
    """
    부모노드와 값을 비교하는 함수
    :param node: 현재노드
    :return: None
    """
    parent = tree[node][2]
    # 부모노드가 존재할 때만 진행
    if parent:
        # 부모노드의 값이 더 크다면
        if tree[node][3] < tree[parent][3]:
            # 값을 바꿔
            tree[node][3], tree[parent][3] = tree[parent][3], tree[node][3]
    else:
        return

    # 부모노드도 반복
    compare(parent)


def an_sum(node):
    """
    해당 노드의 조상 노드의 합을 구하는 함수
    :param node: 현재 노드
    :return: 함수 재호출
    """
    global rlt
    if node == 1:
        return 0

    parent = tree[node][2]
    # 결과값에 조상 노드 값들을 쌓아감
    rlt += tree[parent][3]
    return an_sum(parent)


T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    values = list(map(int, input().split()))
    # 왼쪽 자식 노드, 오른쪽 자식노드, 부모노드, 값
    tree = [[0 for _ in range(4)] for _ in range(N + 1)]

    make_tree()

    # values의 각 값을 tree에 배정
    for i in range(N):
        tree[i+1][3] = values[i]

    # 비교를 반복해 정렬
    for i in range(1, N+1):
        compare(i)

    rlt = 0

    # 마지막 노드 = N번째 노드
    last_node = N
    an_sum(last_node)

    print(f'#{tc} {rlt}')
