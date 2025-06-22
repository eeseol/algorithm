from collections import deque
from pprint import pprint
import heapq

def lets_debug(menu):
    #전체 맵 출력합니다.
    if menu == 1:
        pprint(maps)
    elif menu == 2:
        pprint(edge_price)

def bfs_for_island_labeling(enter_y, enter_x, island_count):
    global maps
    global island_xy
    de = deque()
    de.append([enter_y, enter_x])
    maps[enter_y][enter_x] = island_count + 1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while de:
        y, x = de.popleft()
        island_xy[island_count + 1].append([y, x])

        for i in range(4):
            new_y = y + dy[i]
            new_x = x + dx[i]
            # 범위 확인
            if not (0 <= new_x < M and 0 <= new_y < N):
                continue
            # 데이터 값이 1일때만
            if maps[new_y][new_x] == 1:
                # 맵에 몇번째 섬인지 체크~
                maps[new_y][new_x] = island_count + 1
                de.append([new_y, new_x])
def island_labeling():
    global maps
    global island_xy
    global island_count

    for i in range(N):
        for j in range(M):
            if maps[i][j] == 1:
                island_count += 1
                bfs_for_island_labeling(i, j, island_count)

def island_dis():
    global edge_price

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    de = deque()

    # 노드마다 반복
    for island in range(2, island_count + 2):
        # 방향마다 반복
        for dire in range(4):
            de.extend(island_xy[island])
            de.append([-1, -1])
            cnt = 0
            while de:
                y, x = de.popleft()
                if y == -1:
                    cnt += 1
                    if len(de) == 0:
                        break
                    else:
                        de.append([-1, -1])
                        continue
                new_y = y + dy[dire]
                new_x = x + dx[dire]

                if not(0 <= new_x < M and 0 <= new_y < N):
                    continue
                #같은 섬일 경우
                if maps[new_y][new_x] == island:
                    continue
                # 다른 섬 발견
                if maps[new_y][new_x] != 0:
                    if cnt >= 2:
                        orign_number = edge_price[maps[new_y][new_x]][island]
                        edge_price[maps[new_y][new_x]][island] = min(cnt, orign_number)
                        edge_price[island][maps[new_y][new_x]] = min(cnt, orign_number)
                else:
                    de.append([new_y, new_x])
            de.clear()

def cruscal():
    global result

    global count
    visited = [False] * 8
    heap = []

    heapq.heappush(heap, [0, 2])


    while heap:
        # 전체 노드 탐색 완료
        if count == island_count:
            break
        # new_data = heapq.heappop()
        new_price, target_node = heapq.heappop(heap)
        # 타겟 노드 이미 방문했을 경우
        if visited[target_node] == True:
            continue
        visited[target_node] = True
        result += new_price
        count += 1
        # 초기 데이터 넣어주기
        for i in range(2, island_count + 2):
            if visited[i] == False:
                price = edge_price[target_node][i]
                if price != 99999:
                    heapq.heappush(heap, [price, i])



####메인 입니다################################
N, M = map(int, input().split())
maps = []
island_xy = [[] for _ in range(8)]
island_count = 0
edge_price = [[99999]*8 for _ in range(8)]
result = 0
count = 0

for i in range(N):
    maps.append(list(map(int, input().split())))

# 섬 라벨링하기. 2번부터 값 매깁니다.
island_labeling()
island_dis()
cruscal()

if count == island_count:
    print(result)
else:
    print(-1)