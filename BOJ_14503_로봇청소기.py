from pprint import pprint

def check_turn_back(d):
    global r
    global c
    new_dc = [0, -1, 0, 1]
    new_dr = [1, 0, -1, 0]

    new_r = r + new_dr[d]
    new_c = c + new_dc[d]

    if maps[new_r][new_c] == 1:
        return True
    else:
        r = new_r
        c = new_c
        return False

N, M = map(int, input().split())
r, c, d = map(int, input().split())

maps = []

dc = [0, 1, 0, -1]
dr = [-1, 0, 1, 0]

for _ in range(N):
    maps.append(list(map(int, input().split())))


cnt = 0
while True:

    if maps[r][c] == 0:
        cnt += 1
        maps[r][c] = 2
    else:
        flag = 0
        for i in range(4):
            new_r = r + dr[i]
            new_c = c + dc[i]
            if 0 <= new_r < N and 0 <= new_c < M:
                if maps[new_r][new_c] == 0:
                    flag = 1
                    break
        # 빈 칸이 없는 경우
        if flag == 0:
            #뒤가 벽인 경우
            if check_turn_back(d):
                break
            #뒤가 벽이 아닌 경우
            else:
                pass
        # 빈 칸이 있는 경우
        else:
            # 방향 반 시계로 90도 회전
            if d == 0:
                d = 3
            else:
                d -= 1
            new_r = r + dr[d]
            new_c = c + dc[d]
            if 0 <= new_r < N and 0 <= new_c < M:
                if maps[new_r][new_c] == 0:
                    r = new_r
                    c = new_c

print(cnt)