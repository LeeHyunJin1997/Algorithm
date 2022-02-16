# 테스트 케이스 10개
for _ in range(10):
    tc = int(input())
    target = input()
    sentence = input()
    cnt = 0

    # 문장을 순회하며
    for i in range(len(sentence)):
        # 첫 글자가 같은 때만 비교
        if sentence[i] == target[0]:
            # 해당 지점부터 목표 문장열과 같다면
            if sentence[i:i+len(target)] == target:
                cnt += 1

    print(f'#{tc} {cnt}')
