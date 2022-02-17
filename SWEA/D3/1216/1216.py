import sys
sys.stdin = open('input.txt')

# 회문임을 판단하는 함수
def isPalindrome(lst):
    if lst == lst[::-1]:
        return True
    else:
        return False

# 홀수일 때
def countPalindromeOdd(matrix, r, c):
    max_cnt = 0

    # 확장할 수 있는 길이 설정
    if 50 <= r:
        safe_r = 99 - r
    else:
        safe_r = r

    if 50 <= c:
        safe_c = 99 - c
    else:
        safe_c = c

    # 가로 먼저 검사
    for k in range(safe_c+1):
        if isPalindrome(matrix[r][c-k:c+k+1]):
            if max_cnt < len(matrix[r][c-k:c+k+1]):
                max_cnt = len(matrix[r][c-k:c+k+1])
        else:
            break

    # 세로 검사
    str_lst = [matrix[r][c]]
    for k in range(1, safe_r+1):
        str_lst = [matrix[r-k][c]] + str_lst + [matrix[r+k][c]]
        if isPalindrome(str_lst):
            if max_cnt < len(str_lst):
                max_cnt = len(str_lst)
        else:
            break

    return max_cnt

# 짝수일 때
def countPalindromeEven(matrix, r, c):
    max_cnt = 0

    # 확장할 수 있는 길이 설정
    if 49 <= r:
        safe_r = 98 - r
    else:
        safe_r = r

    if 49 <= c:
        safe_c = 98 - c
    else:
        safe_c = c

    # 가로 먼저 검사
    for k in range(safe_c+1):
        if isPalindrome(matrix[r][c-k:c+k+2]):
            if max_cnt < len(matrix[r][c-k:c+k+2]):
                max_cnt = len(matrix[r][c-k:c+k+2])
        else:
            break
    
    # 세로 검사
    str_lst = [matrix[r][c], matrix[r+1][c]]
    for k in range(1, safe_r+1):
        str_lst = [matrix[r-k][c]] + str_lst + [matrix[r+1+k][c]]
        if isPalindrome(str_lst):
            if max_cnt < len(str_lst):
                max_cnt = len(str_lst)
        else:
            break
    return max_cnt




# 테스트케이스 10개 
for _ in range(10):
    tc = int(input())
    # 100줄의 입력 받기
    matrix = [list(input()) for _ in range(100)]
    max_palindrome = 0

    for r in range(100):
        for c in range(100):
            cnt_palindrome = countPalindromeOdd(matrix, r, c)
            if max_palindrome < cnt_palindrome :
                max_palindrome = cnt_palindrome
    
    for r in range(99):
        for c in range(99):
            cnt_palindrome = countPalindromeEven(matrix, r, c)
            if max_palindrome < cnt_palindrome :
                max_palindrome = cnt_palindrome


    print(f'#{tc} {max_palindrome}')


