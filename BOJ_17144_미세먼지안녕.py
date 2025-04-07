from collections import deque

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

    # 1T
    size = len(dust)

    #먼지 확산 레츠고
    for i in range(size):

        y, x = dust.popleft()
        direc = 0
        add_dust = data[y][x]//5
        # 네 방향 추가해주기.
        for k in range(4):
            new_y = y + dy[k]
            new_x = x + dx[k]
            if 0 <= new_y < R and 0 <= new_x < C:
                if data[new_y][new_x] != -1:
                    direc += 1
                    temp_data[new_y][new_x] += add_dust
        temp_data[y][x] += data[y][x] - (add_dust * direc)
    time += 1
    data = [row[:] for row in temp_data]

    # 첫 번째 공기청정기 가동.
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
    dust.clear()
    for i in range(R):
        for j in range(C):
            if data[i][j] > 0:
                dust.append([i, j])

result = 0
for i in range(R):
    for j in range(C):
        if data[i][j] == -1:
            continue
        result += data[i][j]

print(result)
