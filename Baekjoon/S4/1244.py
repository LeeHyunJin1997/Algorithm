# 스위치 켜고끄는 함수
def on_off(x):
    if on_and_off_status[x] == 0:
        on_and_off_status[x] = 1
    elif on_and_off_status[x] == 1:
        on_and_off_status[x] = 0
    else:
        print('다른 숫자가 들어옴')
    
def boy(number, switches):
    # 스위치 번호 1 ~ 스위치개수
    for switch_num in range(1, switches+1):
        # 스위치 번호가 주어진 번호의 배수라면
        if switch_num % number == 0:
            on_off(switch_num-1)

def girl(number, switches):
    for i in range(switches):
        # try는 마이너스 인덱스일때 break하지 못하기 때문에, if 별도 구축
        if number-1-i < 0:
            break   
        try:
            # i = 0 인 경우, 상태가 2 번 바뀌어 원점으로 가기 때문에 별도 처리
            if i == 0:
                on_off(number-1)
            elif on_and_off_status[number-1-i] == on_and_off_status[number-1+i]:
                on_off(number-1-i)
                on_off(number-1+i)
            # 대칭이지 않은 수를 만날 경우 break
            else:
                break
        # 인덱스 에러가 날 경우 break
        except IndexError:
            break

# 스위치개수
switches = int(input())
# 현재 전구 상태
on_and_off_status = list(map(int, input().split()))
# 학생 성별 리스트
sex = [] 
# 각 학생이 받은 숫자 리스트
numbers = []

# N은 주어진 학생 수
N = int(input())

# 입력 받은 수를 각각 성별, 숫자로 구분해 리스트에 담음
for i in range(N):
    x, y = map(int, input().split())
    sex.append(x)
    numbers.append(y)

# 성별이 1이면, 함수 boy를, 2이면 함수 girl을 호출
for i in range(len(sex)):
    if sex[i] == 1:
        boy(numbers[i], switches)
    elif sex[i] == 2:
        girl(numbers[i], switches)

# 결과 상태인 on_and_off_status를 20개씩 끊어서 출력
for i in range(len(on_and_off_status)):
    if (i+1) % 20 == 0:
        print(on_and_off_status[i])
    else:
        print(on_and_off_status[i], end=' ')