# 미생물 격리
T = int(input())
di, dj = (0,-1,1,0,0),(0, 0, 0, -1, 1)
opp = [0,2,1,4,3]
for tc in range(1, 1+T):
    # N 배열 크기, M 시간, K 군집개수
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(K)]

    # M 시간 경과
    for _ in range(M):
        # 각각의 미생물 이동, 경계 처리
        for i in range(len(arr)):
            arr[i][0] = arr[i][0] + di[arr[i][3]]
            arr[i][1] = arr[i][1] + dj[arr[i][3]]
            # 경계값일 경우
            if arr[i][0] == 0 or arr[i][0] == N-1 or arr[i][1] == 0 or arr[i][1] == N-1:
                # 미생물 수 반으로 줄이고
                arr[i][2] //= 2
                # 방향은 반대로 바꿔줘
                arr[i][3] = opp[arr[i][3]]

        # 내림차순 정렬
        arr.sort(key=lambda x: (x[0],x[1],x[2]), reverse=True)

        # 좌표가 같은 경루 큰 미생물로 합치기
        i = 1
        while i < len(arr):
            if arr[i-1][0] == arr[i][0] and arr[i-1][1] == arr[i][1]:
                arr[i-1][2] += arr[i][2]
                arr.pop(i)
            else:
                i += 1
    
    ans = 0
    for i in range(len(arr)):
        ans += arr[i][2]

    print(f'#{tc} {ans}')
