from collections import deque

def move_people(group, group_total):
    global maps

    new_population = group_total//len(group)

    for y, x in group:
        maps[y][x] = new_population


def bfs(visited, de, group, group_total):
    global flag
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    while de:
        y, x = de.pop()

        for k in range(4):
            new_y = y + dy[k]
            new_x = x + dx[k]
            if not (0 <= new_x < N and 0 <= new_y < N):
                continue
            if visited[new_y][new_x] == True:
                continue
            if L <= abs(maps[y][x] - maps[new_y][new_x]) <= R:
                flag = 1
                group.append([new_y, new_x])
                de.append([new_y, new_x])
                group_total += maps[new_y][new_x]
                visited[new_y][new_x] = True

    return group_total

def group():
    global visited
    global flag

    for i in range(N):
        for j in range(N):
            if visited[i][j] == True:
                continue
            # 방문한 적없는 좌표 도착
            # 탐색 위한 변수들 선언
            visited[i][j] = True
            de = deque()        # 방문하는 노드 저장하는 덱. 추가 탐색을 위해
            group = []          # 방문한 노드 저장하는 리스트. 인구수 업데이트를 위해
            group.append([i, j])
            group_total = maps[i][j]     # 방문한 지역의 인구를 모두 더한 변수
            de.append([i, j])
            # 탐색시작
            group_total = bfs(visited, de, group, group_total)
            # 인구 이동
            if flag == 0:
                continue
            move_people(group, group_total)


#####메인입니다#####################################################################
N, L, R = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

day = 0
flag = 0

while True:
    visited = [[False] * N for _ in range(N)]

    group()

    if flag == 0:
        break
    flag = 0
    day += 1

print(day)
