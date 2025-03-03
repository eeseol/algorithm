# visited 업데이트 하는 위치!!!
# 값 이상하게 넣어줘서 ㅋㅋㅋㅋㅋㅋㅋㅋ
from collections import deque
def bfs():
    global de
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    time = 0
    while de and time != L:
        y, x = de.pop()

        if y == -1:
            time += 1
            if de:
                de.appendleft([-1, -1])
            continue
        visited[y][x] = True
        for i in range(4):
            new_y = y + dy[i]
            new_x = x + dx[i]

            if 0 <= new_y < N and 0 <= new_x < M:
                if visited[new_y][new_x] == False:
                    if data[new_y][new_x] in possible[data[y][x]][i]:
                        de.appendleft([new_y, new_x])

T = int(input())

for test_case in range(1, T + 1):
    possible = [[[],[],[],[]],
                [[1,2,5,6], [1,2,4,7], [1,3,4,5], [1,3,6,7]],
                [[1,2,5,6], [1,2,4,7], [], []],
                [[], [], [1,3,4,5], [1,3,6,7]],
                [[1,2,5,6], [], [], [1,3,6,7]],
                [[], [1,2,4,7], [], [1,3,6,7]],
                [[], [1,2,4,7], [1,3,4,5], []],
                [[1,2,5,6], [], [1,3,4,5], []],
                ]
    N, M, R, C, L = list(map(int, input().split()))

    de = deque()
    de.appendleft([R, C])
    de.appendleft([-1, -1])
    data = []
    visited = [[False]*M for _ in range(N)]
    visited[R][C] = True

    for i in range(N):
        data.append(list(map(int, input().split())))

    bfs()

    count = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == True:
                count += 1

    print(f'#{test_case} {count}')