T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))

    # 버블 정렬
    for j in range(len(nums)):
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]

    print(f'#{tc}', end=' ')
    # 뒤에서(최댓값) 하나씩, 앞에서(최솟값) 하나씩
    for i in range(5):
        print(nums[-i - 1], end=' ')
        print(nums[i], end=' ')

    print('')