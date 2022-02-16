# 같은 문자끼리의 순서는 고려하지 않는 count sort
import sys
sys.stdin = open('GNS_test_input.txt')

nums = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

T = int(input())
for tc in range(1, T+1):
    info = input()
    str_lst = input().split()
    cnt = [0] * 10
    sorted_str_lst = []

    # 문자열을 순회하며 해당 숫자(문자로 된)에 해당하는 칸에 +1
    for i in range(len(str_lst)):
        cnt[nums.index(str_lst[i])] += 1

    for i in range(len(cnt)):
        for j in range(cnt[i]):
            sorted_str_lst.append(nums[i])

    print(f'#{tc}')
    print(' '.join(sorted_str_lst))