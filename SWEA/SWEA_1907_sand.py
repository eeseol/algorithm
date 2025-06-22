from collections import deque

# 특정 좌표 (x, y)의 모래성이 무너졌을 때,
# 그 주변 8칸에 있는 모래성의 현재 바다 인접 개수(state)를 +1 증가시킴
def wave_update(x, y):
    global state

    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    dy = [1, 1, 1, 0, 0, -1, -1, -1]

    for i in range(8):
        new_x = x + dx[i]
        new_y = y + dy[i]
        # 범위 내이고, 모래성이 있는 곳이라면
        if 0 <= new_x < W and 0 <= new_y < H:
            if data[new_y][new_x] != '.':
                state[new_y][new_x] += 1

# 파도가 치는 과정 전체를 처리하는 함수
def wave():
    global de       # 현재 남아있는 모래성 좌표들을 담은 큐
    global state    # 각 칸이 현재 인접한 바다 개수를 담고 있는 배열
    global cnt      # 파도가 몇 번 쳤는지 세는 카운트 변수
    change = []     # 이번 턴에 무너질 모래성 좌표들

    while True:
        x, y = de.popleft()

        # [-1, -1]는 한 턴의 경계를 의미함
        if x == -1:

            # 이번 턴에 무너질 게 없으면, 종료
            if len(change) == 0:
                break
            # 무너질 좌표들 처리
            while change:
                ch_x, ch_y = change.pop()
                wave_update(ch_x, ch_y)     # 이 칸이 무너지므로 주변 영향 업데이트
                state[ch_y][ch_x] = 0       # 현재 칸은 초기화
                data[ch_y][ch_x] = '.'      # 실제 데이터도 바다로 변경
            de.append([-1, -1])     # 다음 턴을 위한 경계 넣어주기
            cnt += 1                # 파도 한 번 쳤음
        else:
            # 무너질 때
            if int(data[y][x]) <= state[y][x]:
                change.append([x, y])   # 이번 턴에 무너질 대상으로 추가
            else:
                de.append([x, y])       # 아직 안 무너짐 → 다음 턴에 다시 평가

# 초기 상태에서 각 모래성 칸이 인접한 바다 개수를 미리 계산하는 함수
def state_update(x, y):
    global state

    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    dy = [1, 1, 1, 0, 0, -1, -1, -1]

    no_sand = 0      # 인접한 바다 칸 수

    for i in range(8):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_x < W and 0 <= new_y < H:
            if data[new_y][new_x] == '.':
                no_sand += 1

    state[y][x] = no_sand   # 현재 칸 기준 인접한 바다 개수 기록

T = int(input())

for test_case in range(1, T+1):
    H, W = map(int, input().split())
    cnt = 0

    data = []           # 실제 모래성 맵
    state = [[0]*W for _ in range(H)]   # 각 칸의 인접한 바다 수를 저장할 맵
    de = deque()        # 탐색 대상이 되는 모래성 칸들을 담은 큐

    for i in range(H):
        data.append(list(input()))
        for j in range(W):
            if data[i][j] != '.':
                de.append([j, i])  #x좌표 y좌표 모래성이 있는 칸만 큐에 추가 (x, y 순서)

    # 턴 경계 삽입
    de.append([-1, -1])

    # 초기 상태 업데이트
    while de:
        x, y = de.popleft()
        if x == -1:
            de.append([-1, -1])
            break
        state_update(x, y)
        de.append([x, y])

    wave()

    print(f'#{test_case} {cnt}')
