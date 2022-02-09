T = int(input())

for _ in range(T):
    a, b = map(int, input().split())

    if b < a:
        a, b = b, a

    gcd = 0
    for i in range(1, a+1):
        if a % i == 0 and b % i == 0:
            gcd = i

    lcm = a * b // gcd

    print(lcm, gcd)