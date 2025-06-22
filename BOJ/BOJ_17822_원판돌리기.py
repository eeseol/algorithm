from pprint import pprint
from collections import deque

def rotate_board(target_board, direction, degree):
    global maps
    for t_board in range(target_board-1, N, target_board):
        for i in range(degree % M):
            if direction == 0:
                temp = maps[t_board].pop()
                maps[t_board].insert(0, temp)
            else:
                temp = maps[t_board].pop(0)
                maps[t_board].append(temp)

def delete_number(delete_locate):
    global maps

    for y, x in delete_locate:
        maps[y][x] = 0

def ava_board():
    global maps

    cnt = 0
    total = 0
    for i in range(N):
        for j in range(M):
            if maps[i][j] != 0:
                cnt += 1
                total += maps[i][j]
    if cnt == 0:
        return
    gijun = total/cnt

    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                continue

            if maps[i][j] > gijun:
                maps[i][j] -= 1
            elif maps[i][j] < gijun:
                maps[i][j] += 1



def check_near_number():
    global maps

    # 원판 인접한 수 있었는지 확인해요
    delete_locate = set()
    flag = 0

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for y in range(N):
        for x in range(M):

            if maps[y][x] == 0:
                continue

            for k in range(4):
                new_y = y + dy[k]
                new_x = x + dx[k]
                if not(0 <= new_y < N):
                    continue
                if new_x == M:
                    new_x = 0
                elif new_x == -1:
                    new_x = M-1

                if maps[y][x] == maps[new_y][new_x]:
                    delete_locate.add((y, x))
                    delete_locate.add((new_y, new_x))
                    flag = 1
    # 같은 수가 인접해 있으면 지워요
    delete_number(delete_locate)
    # 인접한 수 없는 판은 평균~~
    if flag == 0:
        ava_board()


###################   메인  입니다   ############################################
N, M, T = map(int, input().split())

maps = []

for _ in range(N):
    maps.append(list(map(int, input().split())))

for _ in range(T):
    # 회전 데이터 입력 받아요
    target_board, direction, degree = map(int, input().split())

    # 회전하는 함수 호출
    rotate_board(target_board, direction, degree)

    # 인접한 수 확인, 지워요~
    check_near_number()
total = 0

for i in range(N):
    total += sum(maps[i])

print(total)
