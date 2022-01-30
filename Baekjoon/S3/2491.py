N = int(input())
input_list = list(map(int, input().split()))
cnt_increase_list = []
cnt_decrease_list = []
cnt_increase = 1 # 수열에서 연속된 숫자의 개수를 나(i)부터 세기 때문에 1로 초기화
cnt_decrease = 1

# 입력 받아온 수열에서
for i in range(len(input_list)):
		# i가 마지막 인덱스에 도달한 경우 cnt값을 append하고 끝
    if i == len(input_list) - 1:
        cnt_increase_list.append(cnt_increase)
        break
		# i의 값보다 i+1의 값이 크거나 같다면 
    elif input_list[i] <= input_list[i+1]:
				# cnt에 1 더해줌
        cnt_increase += 1
		# 더 작은 수를 만나면 cnt값을 append하고 초기화
    else:
        cnt_increase_list.append(cnt_increase)
        cnt_increase = 1
        continue
# 입력 받아온 수열에서
for i in range(len(input_list)):
		# i가 마지막 인덱스에 도달한 경우 cnt값을 append하고 끝
    if i == len(input_list)-1:
        cnt_decrease_list.append(cnt_decrease)
        break
		# i의 값보다 i+1의 값이 작거나 같다면 
    elif input_list[i] >= input_list[i+1]:
        cnt_decrease += 1
		# 더 큰 수를 만나면 cnt값을 append하고 초기화
    else:
        cnt_decrease_list.append(cnt_decrease)
        cnt_decrease = 1
        continue

# 커지는 수열 길이와 작아지는 수열 길이 중 큰것을 출력
if max(cnt_increase_list) >= max(cnt_decrease_list):
    print(max(cnt_increase_list))
else:
    print(max(cnt_decrease_list))