# bubble sort : 매우 오래 걸림
import sys
sys.stdin = open('GNS_test_input.txt')

nums = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

T = int(input())
for tc in range(1, T+1):
    info = input()
    str_lst = input().split()

    for j in range(len(str_lst)):
        for i in range(len(str_lst)-1):
            if nums.index(str_lst[i]) > nums.index(str_lst[i+1]):
                str_lst[i], str_lst[i+1] = str_lst[i+1], str_lst[i]

    print(f'#{tc}')
    print(' '.join(str_lst))