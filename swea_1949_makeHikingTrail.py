def dfs(y, x, depth = 0, flag = 0):
    visited[y][x] = True
    global real_depth
    if real_depth < depth:
        real_depth = depth
    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]
    for i in range(4):
        new_y = y + dy[i]
        new_x = x + dx[i]
        if 0<= new_x < N and 0 <= new_y < N and visited[new_y][new_x] == False:
            if data[y][x] > data[new_y][new_x]:
                dfs(new_y, new_x, depth+1, flag)
            elif K > 0 and flag == 0:
                for k in range(1, K+1):
                    data[new_y][new_x] -= k
                    if data[y][x] > data[new_y][new_x]:
                        dfs(new_y, new_x, depth+1, 1)
                        data[new_y][new_x] += k
                        break
                    data[new_y][new_x] += k
                        
    visited[y][x] = False



T = int(input())
for test_case in range(1, T + 1):
    N, K = list(map(int, input().split()))
    real_depth = 0
    data = []
    high = 0
    index_high = []
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        data.append(list(map(int, input().split())))
        for j in range(N):
            if data[i][j] > high:
                high = data[i][j]
                index_high.clear()
                index_high.append([i, j])
            elif data[i][j] == high:
                index_high.append([i, j])

    for y, x in index_high:
        dfs(y, x, 1)

    print(f'#{test_case} {real_depth}')