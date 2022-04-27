def merge_sort(lst):
    global cnt
    # 원소가 하나 남으면 반환
    if len(lst) < 2:
        return lst

    mid = len(lst) // 2
    low_lst = merge_sort(lst[:mid])
    high_lst = merge_sort(lst[mid:])

    # low_arr 와 high_arr 를 앞에서부터 비교, 더 작은 것을 merged_lst 로 복사
    merged_lst = []
    l = h = 0
    while l < len(low_lst) and h < len(high_lst):
        if low_lst[l] <= high_lst[h]:
            merged_lst.append(low_lst[l])
            l += 1
        else:
            merged_lst.append(high_lst[h])
            h += 1

    # 오른쪽이 먼저 복사된 경우 카운트
    if low_lst[l:]:
        cnt += 1

    # low_arr 와 high_arr 중 하나만 전부 이동시켰을 때
    # 남은 원소 이어붙이기
    merged_lst += low_lst[l:]
    merged_lst += high_lst[h:]
    return merged_lst


T = int(input())
for tc in range(1, T+1):
    # 정수의 개수
    N = int(input())
    lst = list(map(int, input().split()))

    cnt = 0
    lst = merge_sort(lst)
    print(f'#{tc} {lst[N//2]} {cnt}')
