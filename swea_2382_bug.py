T = int(input())

for test_case in range(1, T + 1):
    N, M, K = list(map(int, input().split()))

    bugs =[]
    dy = [0, -1, 1, 0, 0]
    dx = [0, 0, 0, -1, 1]
    data = [[[] for _ in range(N)] for _ in range(N)]

    for i in range(K):
        bugs.append(list(map(int, input().split())))
        data[bugs[i][0]][bugs[i][1]].append(i)

    for _ in range(M):
        meet = []

        for bug_index in range(len(bugs)):
            bug = bugs[bug_index]
            if bug[0] == -1:
                continue

            y = bug[0] + dy[bug[3]]
            x = bug[1] + dx[bug[3]]

            # 이동
            data[y][x].append(bug_index)
            data[bug[0]][bug[1]].pop(0)
            bugs[bug_index][0] = y
            bugs[bug_index][1] = x
            #약품 안쪽에 있을때
            if 0 < y < (N-1) and 0 < x < (N-1):
                if len(data[y][x]) > 1:
                    meet.append([y, x])
            else:
                bugs[bug_index][2] //= 2
                # 벌레가 0일경우
                if bugs[bug_index][2] == 0:
                    bugs[bug_index][0] = -1
                    bugs[bug_index][1] = -1
                    continue
                # 방향 바꿔주기기
                if bugs[bug_index][3] == 2:
                    bugs[bug_index][3] = 1
                elif bugs[bug_index][3] == 4:
                    bugs[bug_index][3] = 3
                else:
                    bugs[bug_index][3] += 1
        
        if meet:
            meets = list(map(list, set(map(tuple, meet))))  # 리스트 내부의 리스트를 튜플로 변환 후 중복 제거
            # 만난 좌표만큼
            for y, x in meets:
                max_index = data[y][x][0]
                total_bug = 0
                # 특정 좌표에서 만난 군집 만큼
                temp = len(data[y][x])
                for _ in range(temp):
                    meet_index = data[y][x][0]
                    data[y][x].pop(0)
                    total_bug += bugs[meet_index][2]
                    # max보다 클경우
                    if bugs[max_index][2] < bugs[meet_index][2]:
                        bugs[max_index][0] = -1
                        bugs[max_index][1] = -1
                        bugs[max_index][2] = 0
                        max_index = meet_index
                    elif bugs[max_index][2] > bugs[meet_index][2]:
                        bugs[meet_index][0] = -1
                        bugs[meet_index][1] = -1
                        bugs[meet_index][2] = 0
                data[y][x].append(max_index)
                bugs[max_index][2] = total_bug
    result = 0
    for bug in bugs:
        result += bug[2]

    print(f'#{test_case} {result}')
