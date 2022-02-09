# 수열을 찾는 함수
def sequence(a, b):
    # 첫 2개의 수를 담은 리스트
    sequence_list = [a, b]
    # 음수가 나올 때까지 반복
    while sequence_list[-2] - sequence_list[-1] >= 0:
         sequence_list.append(sequence_list[-2] - sequence_list[-1])

    return sequence_list

N = int(input())
max_len = 0

# 최대길이가 나오게 하는 두 번째 숫자 찾기, 0부터 N까지 반복
for i in range(N+1):
    new_sequence = sequence(N, i)
    if max_len < len(new_sequence):
        max_len = len(new_sequence)
        max_len_sequence = new_sequence

print(max_len)
for i in max_len_sequence:
    print(i, end= ' ')