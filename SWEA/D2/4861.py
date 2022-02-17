import sys
sys.stdin = open('sample_input.txt')

# 회문임을 판단하는 함수
def isPalindrome(str_lst):
    if str_lst == str_lst[::-1]:
        return True
    else:
        return False

def findPalindrome(matrix, M):
    # 가로 문자열 판단
    for r in range(len(matrix)):
        for c in range(len(matrix)-M+1):
            # 각 위치에서 가로길이 M짜리 문자열
            str_hor = matrix[r][c:c+M]
            if isPalindrome(str_hor):
                return ''.join(str_hor)

    # 세로 문자열 판단
    for r in range(len(matrix)-M+1):
        for c in range(len(matrix)):
            # 각 위치에서 세로길이 M짜리 문자열
            str_ver = ''
            for k in range(M):
                str_ver += matrix[r+k][c]
            if isPalindrome(str_ver):
                return ''.join(str_ver)

    return '회문없음'

T = int(input())
for tc in range(1, T+1):
    # NxN, 회문 길이 M
    N, M = map(int, input().split())
    matrix = [list(input()) for _ in range(N)]

    print(f'#{tc} {findPalindrome(matrix, M)}')