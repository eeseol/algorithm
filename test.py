from pprint import pprint
from collections import deque
import copy

R, C, T = map(int, input().split())

data = []
cleaner = []
dust = deque()

for i in range(R):
    data.append(list(map(int, input().split())))
    for j in range(C):
        if data[i][j] == -1:
            cleaner.append([i, j])
        elif data[i][j] > 0:
            dust.append([i, j])

time = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while T != time:

    temp_data = [[0]*C for _ in range(R)]
    temp_data[cleaner[0][0]][cleaner[0][1]] = -1
    temp_data[cleaner[1][0]][cleaner[1][1]] = -1

    # 🔥 수정된 부분: 확산할 먼지 따로 저장
    size = len(dust)

    for _ in range(size):
        y, x = dust.popleft()
        direc = 0
        add_dust = data[y][x] // 5
        for k in range(4):
            new_y = y + dy[k]
            new_x = x + dx[k]
            if 0 <= new_y < R and 0 <= new_x < C:
                if data[new_y][new_x] != -1:
                    direc += 1
                    temp_data[new_y][new_x] += add_dust
        temp_data[y][x] += data[y][x] - (add_dust * direc)

    time += 1
    data = copy.deepcopy(temp_data)

    # 공기청정기 작동 (윗부분: 반시계)
    current_y, current_x = cleaner[0][0] - 1, cleaner[0][1]
    if current_y != -1:
        data[current_y][current_x] = 0
        while current_y != 0:
            data[current_y][current_x] = data[current_y-1][current_x]
            current_y -= 1
        while current_x != C-1:
            data[current_y][current_x] = data[current_y][current_x + 1]
            current_x += 1
        while current_y != cleaner[0][0]:
            data[current_y][current_x] = data[current_y+1][current_x]
            current_y += 1
        while True:
            if data[current_y][current_x-1] == -1:
                data[current_y][current_x] = 0
                break
            else:
                data[current_y][current_x] = data[current_y][current_x-1]
                current_x -= 1

    # 공기청정기 작동 (아랫부분: 시계)
    current_y, current_x = cleaner[1][0] + 1, cleaner[1][1]
    if current_y != R:
        data[current_y][current_x] = 0
        while current_y != R - 1:
            data[current_y][current_x] = data[current_y+1][current_x]
            current_y += 1
        while current_x != C-1:
            data[current_y][current_x] = data[current_y][current_x + 1]
            current_x += 1
        while current_y != cleaner[1][0]:
            data[current_y][current_x] = data[current_y-1][current_x]
            current_y -= 1
        while True:
            if data[current_y][current_x-1] == -1:
                data[current_y][current_x] = 0
                break
            else:
                data[current_y][current_x] = data[current_y][current_x-1]
                current_x -= 1

    # 🔥 수정된 부분: 다음 턴을 위한 먼지 큐 다시 채우기
    dust.clear()
    for i in range(R):
        for j in range(C):
            if data[i][j] > 0:
                dust.append([i, j])

# 정답 계산
result = 0
for i in range(R):
    for j in range(C):
        if data[i][j] == -1:
            continue
        result += data[i][j]

print(result)
