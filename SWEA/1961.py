T = int(input())
for test_case in range(T):

    N = int(input())
    nums = []


    for i in range(N):
        # 인풋을 받아 하나의 리스트로 연결
        nums.extend(input().split())

    # 테스트 케이스 번호 출력
    print(f'#{test_case+1}')

    # 숫자의 규칙별로 한줄씩 출력
    for j in range(0, N):
        # 뒤에서부터 N배씩 출력
        for i in range(1, N+1):
            print(nums[-i*N+j], end='')
        print(' ', end='')

        # 뒤에서부터 N개씩 출력
        for i in range(1, N+1):
            print(nums[-i-N*j], end='')
        print(' ', end='')

        # 앞에서부터 N배씩 출력
        for i in range(1, N+1):
            print(nums[i*N-1-j], end='')
        print('')