N, M = map(int, input().split())
input_list= []

for i in range(N):
    input_list.append(input())

for i in input_list:
    print(i[::-1])