import heapq
from collections import deque
def dijkstra():
    global distance_for_shark
    de = deque()
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    shark_y = shark_locate[0]
    shark_x = shark_locate[1]
    distance_for_shark[shark_y][shark_x] = 0
    de.append([shark_y, shark_x])

    while de:
        y, x = de.popleft()
        for k in range(4):
            new_y = y + dy[k]
            new_x = x + dx[k]
            if 0 <= new_x < N and 0 <= new_y < N:
                if maps[new_y][new_x] > shark_size:
                    continue
                if distance_for_shark[new_y][new_x] > distance_for_shark[y][x] + 1:
                    distance_for_shark[new_y][new_x] = distance_for_shark[y][x] + 1
                    de.append([new_y, new_x])

def choose_fish():
    global fish_distance

    for one in fish:
        fish_y = one[0]
        fish_x = one[1]
        if distance_for_shark[fish_y][fish_x] == float('inf'):
            continue

        if maps[fish_y][fish_x] < shark_size:
            distance = distance_for_shark[fish_y][fish_x]
            heapq.heappush(fish_distance, (distance, fish_y, fish_x))


########################메인입니다####################################

N = int(input())

maps = []
shark_locate = []   # 현재 상어 위치 y, x
shark_size = 2
shark_eaten = 0
fish =[]            # 물고기 좌표 저장

for i in range(N):
    maps.append(list(map(int, input().split())))
    for j in range(N):
        if maps[i][j] == 9:
            shark_locate.append(i)
            shark_locate.append(j)
        elif 1 <= maps[i][j] <= 8:
            fish.append([i, j])

maps[shark_locate[0]][shark_locate[1]] = 0
time = 0
while True:
    # 아기상어와 물고기 거리 계산하기
    distance_for_shark = [[float('inf')] * N for _ in range(N)]
    dijkstra()
    # 사냥할 물고기 뽑으러 갑시다.
    fish_distance = []
    choose_fish()

    # 사냥할 물고기가 없어요
    if len(fish_distance) == 0:
        break

    # 사냥할 물고기!
    target_distance, target_y, target_x = heapq.heappop(fish_distance)

    # 사냥 시작해요
    time += target_distance
    shark_eaten += 1
    shark_locate[0] = target_y
    shark_locate[1] = target_x

    # 물고기 정보 지워주기
    fish = [f for f in fish if not (f[0] == target_y and f[1] == target_x)]
    maps[target_y][target_x] = 0

    if shark_size == shark_eaten:
        shark_size += 1
        shark_eaten = 0

print(time)
