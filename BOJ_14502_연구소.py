from collections import deque
from pprint import pprint

def spread_virus():
    global safe_area
    global big_safe_area
    locate = set()
    de = deque()

    # 초기 바이러스 정보 덱이랑 셋에 넣어주기
    # 셋은 지도 유지하기 위한 변수임.
    for viru in virus:
        locate.add((viru[0], viru[1]))
        de.append([viru[0], viru[1]])

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while de:
        y, x = de.popleft()

        for i in range(4):
            new_y = y + dy[i]
            new_x = x + dx[i]
            # 범위 확인
            if not (0 <= new_y < N and 0 <= new_x < M):
                continue
            # 방문 한 적 있는지 확인
            if (new_y, new_x) in locate:
                continue
            # 갈 수 있는 곳인지 확인
            if maps[new_y][new_x] == 0:
                locate.add((new_y, new_x))
                de.append([new_y, new_x])

        if big_safe_area > safe_area - len(locate):
            return
        
    big_safe_area = max(big_safe_area, safe_area - len(locate))


def dfs(r, c, cnt):
    global maps

    if cnt >= 3:
        # 탐색 하러 가야됨
        spread_virus()
        return
    
    for i in range(0, N):
        for j in range(0, M):
            if maps[i][j] == 0:
                maps[i][j] = 1
                dfs(i, j, cnt + 1)
                maps[i][j] = 0



N, M = map(int, input().split())

maps = []
virus = []
big_safe_area = 0
safe_area = N * M

for i in range(N):
    maps.append(list(map(int, input().split())))
    for j in range(M):
        if maps[i][j] == 2:
            virus.append([i, j])
        elif maps[i][j] == 1:
            safe_area -= 1
#
safe_area -= 3

dfs(0, 0, 0)

print(big_safe_area)

