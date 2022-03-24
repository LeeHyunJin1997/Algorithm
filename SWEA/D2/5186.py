# 이진수2
T = int(input())
for tc in range(1, T+1):
    N = float(input())

    i = -1
    bin_num = '0.'
    while True:
        # 나누어떨어지면 break
        if N == 0:
            print(f'#{tc} {bin_num[2:]}')
            break

        # bin_num 가 소수점 아래 12자리를 넘어가면 overflow
        elif len(bin_num) > 14:
            print(f'#{tc} overflow')
            break

        elif N // (2**i) > 0:
            bin_num += '1'
            N -= 2**i
            i -= 1

        else:
            bin_num += '0'
            i -= 1


