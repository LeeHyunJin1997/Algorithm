import sys

sys.stdin = open('input.txt')

for tc in range(1, 11):
    # 테스트 케이스의 길이
    N = int(input())
    # 건물 형태
    buildings = list(map(int, input().split()))
    # 세대 수를 세기 위한 변수
    cnt = 0

    # 개별 건물 인덱스, 양쪽 맨 끝 2칸에는 건물이 없음
    for i in range(2, len(buildings)-2):
        # 주변 건물 중 가장 높은 건물 높이 blind
        blind = 0
        for j in [buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2]]:
            if j > blind:
                blind = j

        # 건물이 주변 건물 최대 높이보다 크다면, 그 차이만큼 세대수에 더함
        if buildings[i] > blind:
            cnt += buildings[i] - blind

    print(f'#{tc} {cnt}')