from pprint import pprint

def remove_line(map, y, x, direction):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    new_y = y
    new_x = x
    while True:
        new_y += dy[direction]
        new_x += dx[direction]
        if 0 <= new_y < N and 0 <= new_x < N:
            map[new_y][new_x] = 0
        else:
            return

def create_line(map, y, x, direction):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    cnt = 0
    new_y = y
    new_x = x
    while True:
        new_y += dy[direction]
        new_x += dx[direction]
        if 0 <= new_y < N and 0 <= new_x < N:
            map[new_y][new_x] = -1
            cnt += 1
        else:
            return cnt

def dfs(new_map, total_node = 0, start = 0, total_line = 0):
    global line
    global node

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    if start >= len(processor):
        if node < total_node:
            node = total_node
            line = total_line
        elif node == total_node:
            line = min(line, total_line)
        return

    x, y = processor[start]
    # 선택 하기로 했을때
    for i in range(4):
        new_x = x
        new_y = y
        while True:
            new_x += dx[i]
            new_y += dy[i]

            # 경로에 뭔가 있었을 경우
            if new_map[new_y][new_x] == 1 or new_map[new_y][new_x] == 2 or new_map[new_y][new_x] == -1:
                break

            # 가장자리에 도달했을때
            if new_x == 0 or new_x == N-1 or new_y == 0 or new_y == N-1:
                temp_line = create_line(new_map, y, x, i)
                total_node += 1
                dfs(new_map, total_node, start+1, total_line + temp_line)
                total_node -= 1
                remove_line(new_map, y, x, i)
                break
    dfs(new_map, total_node, start + 1, total_line)

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    data = []
    processor = []
    line = float('inf')
    node = 0

    for i in range(N):
        data.append(list(map(int, input().split())))
        for j in range(N):
            if data[i][j] == 1:
                if i == 0 or i == N-1 or j == 0 or j == N - 1:
                    data[i][j] = 2
                    node += 1
                else:
                    processor.append([j, i]) #x좌표 y좌표
    dfs(data, node)
    print(f'#{test_case} {line}')