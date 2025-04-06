from pprint import pprint

def check_turn_back(d):
    global r
    global c
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]

    new_r = r + dr[d]
    new_c = c + dc[d]

    if maps[new_c][new_r] == 1:
        return True
    else:
        r = new_r
        c = new_c
        return False

N, M = map(int, input().split())
r, c, d = map(int, input().split())

maps = []

dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]

for _ in range(N):
    maps.append(list(map(int, input().split())))


cnt = 0
while True:

    if maps[c][r] == 0:
        cnt += 1
        maps[c][r] = 2
    else:
        flag = 0
        for i in range(4):
            new_r = r + dr[i]
            new_c = c + dc[i]
            if 0 <= new_r < M and 0 <= new_c < N:
                if maps[new_c][new_r] == 0:
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
            if 0 <= new_r < M and 0 <= new_c < N:
                if maps[new_c][new_r] == 0:
                    r = new_r
                    c = new_c

print(cnt)
