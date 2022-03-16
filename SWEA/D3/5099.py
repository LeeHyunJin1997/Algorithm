# 피자굽기
def melt():
    fire.append(fire.pop(0))
    fire[0][1] = fire[0][1]//2

T = int(input())
for tc in range(1, T+1):
    # N 화덕크기, M 피자개수
    N, M = map(int, input().split())
    Cis = list(map(int, input().split()))
    pizza_lst = []

    # 피자리스트는 [피자번호, 치즈양] 형태
    for i in range(len(Cis)):
        pizza_lst.append([i+1, Cis[i]])

    # 최초 한바퀴
    fire = pizza_lst[0:N]
    pizza_lst = pizza_lst[N:]
    fire[0][1] = fire[0][1]//2


    while True:
        # 피자가 하나 남았을 때
        if len(fire) == 1:
            print(f'#{tc} {fire[0][0]}')
            break

        # 치즈가 다 녹았다면
        while fire[0][1] == 0:
            if len(fire) ==1:
                break
            # 새 피자가 없다면
            if not pizza_lst:
                # 다된 피자 빼고 뒷 피자도 녹았다!
                fire.pop(0)
                fire[0][1] = fire[0][1]//2
            # 새 피자 넣기
            else:
                fire[0] = pizza_lst.pop(0)

        melt()



