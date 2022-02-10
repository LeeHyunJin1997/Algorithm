import sys

sys.stdin = open('input.txt')

def dump(boxes):
    highest = 0
    lowest = 100
    highest_idx = None
    lowest_idx = None

    # boxes 를 순회하며 최대, 최소값과 그 위치를 저장
    for i in range(len(boxes)):
        if highest < boxes[i]:
            highest = boxes[i]
            highest_idx = i
        if lowest > boxes[i]:
            lowest = boxes[i]
            lowest_idx = i

    # 가장 높은 박스더미에서 가장 낮은 박스더미로 하나 이동
    boxes[highest_idx] -= 1
    boxes[lowest_idx] += 1

    # 덤프 이후에 최대, 최소가 바뀌었는지 다시 점검
    new_highest = 0
    new_lowest = 100
    new_highest_idx = None
    new_lowest_idx = None

    for i in range(len(boxes)):
        if new_highest < boxes[i]:
            new_highest = boxes[i]
            new_highest_idx = i
        if new_lowest > boxes[i]:
            new_lowest = boxes[i]
            new_lowest_idx = i

    # 바뀐 후의 높이차를 구함
    dif = boxes[new_highest_idx] - boxes[new_lowest_idx]

    # 덤프된 리스트와 높이차를 반환
    return (boxes, dif)

# 테스트케이스 개수는 10
T = 10
for tc in range(1, T + 1):
    # 덤프 횟수
    repeat = int(input())
    boxes = list(map(int, input().split()))

    dif = 100
    # 주어진 덤프횟수만큼 반복
    for _ in range(repeat):
        # 평탄화가 완료되었을 경우, break
        if dif <= 1:
            print(f'#{tc} {dif}')
            break
        else:
            boxes, dif = dump(boxes)

    print(f'#{tc} {dif}')

