def rsp(a, b):
    # 비겼을 때는 번호가 작은 쪽 반환
    if students[a - 1] == students[b - 1]:
        return a
    # 가위바위보 이긴 쪽의 인덱스 반환
    elif students[a-1] == 1 and students[b-1] == 3:
        return a
    elif students[a-1] == 3 and students[b-1] == 1:
        return b
    elif students[a-1] > students[b-1]:
        return a
    elif students[a-1] < students[b-1]:
        return b

def tor(start, end):
    # 혼자 남을 때
    if end == start:
        # 그 학생 번호 저장
        return start
    else:
        left = tor(start, (start+end)//2)
        right = tor((start+end)//2+1, end)
        return rsp(left, right)


T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    students = list(map(int, input().split()))

    winner = tor(1, N)
    print(f'#{tc} {winner}')