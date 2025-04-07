from pprint import pprint

def check_wall(d, r, c, new_r, new_c):
    global walls

    for wall in walls:
        if wall[2] == 0:
            if d == 1:
                if wall[0] == new_r and wall[1] == new_c:
                    return False
            if d == 2:
                if wall[0] == new_r and wall[1] == new_c + 1:
                    return False
        else:
            if d == 3:
                if wall[0] == new_r and wall[1] == new_c:
                    return False
            if d == 4:
                if wall[0] == new_r - 1 and wall[1] == c:
                    return False

    return True

def wind():
    global real_map

    delta = [
        [],
        [[-1, 1], [0, 1], [1, 1]],      # 오른쪽 방향
        [[-1, -1], [0, -1], [1, -1]],   # 왼쪽 방향
        [[-1, -1], [-1, 0], [-1, 1]],   # 위쪽 방향
        [[1, -1], [1, 0], [1, 1]],      # 아래쪽 방향
    ]

    # 히터 개수만큼 반복하는 반복문
    for warmer in warmers:  # 방향, r, c
        ori_heat = set()    # 이전단계에서 히터영향 받은 곳
        ori_heat.add((warmer[1] + delta[warmer[0]][1][0], warmer[2] + delta[warmer[0]][1][1]))
        real_map[warmer[1] + delta[warmer[0]][1][0]][warmer[2] + delta[warmer[0]][1][1]] += 5

        # 5단계로 따뜻해지는 반복문
        for heat in range(4, 0, -1):
            new_heat = set()  # 새롭게 히터 영향 받을 곳
            while ori_heat:
                r, c = ori_heat.pop()

                for i in range(3):
                    new_r = r + delta[warmer[0]][i][0]
                    new_c = c + delta[warmer[0]][i][1]

                    # 범위 체크
                    if not (0 <= new_r < R and 0 <= new_c < C):
                        continue

                    if check_wall(warmer[0], r, c, new_r, new_c):
                        new_heat.add((new_r, new_c))

            for update in new_heat:
                real_map[update[0]][update[1]] += heat

            ori_heat.clear()
            ori_heat = new_heat

def control_temperature():
    global real_map

    dc = [0, 1, -1, 0, 0]
    dr = [0, 0, 0, -1, 1]

    temp_map = [[0] * C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            cnt =
            if real_map[r][c] != 0:
                update_data = real_map[r][c]
                for k in range(1, 5):
                    new_r = r + dr[k]
                    new_c = c + dc[k]

                    if not (0 <= new_r < R and 0 <= new_c < C):
                        continue





def cold_border():
    global real_map

    for i in range(C):
        if real_map[0][i] > 0:
            real_map[0][i] -= 1
        if real_map[R-1][i] > 0:
            real_map[R-1][i] -= 1

    for j in range(R):
        if real_map[j][0] > 0:
            real_map[j][0] -= 1
        if real_map[j][C-1] > 0:
            real_map[j][C-1] -= 1

def testing_checker():
    pass

R, C, K = map(int, input().split())

data = []
warmers = []
checker = []
walls = []
cnt = 0
real_map = [[0] * C for _ in range(R)]

for i in range(R):
    data.append(list(map(int, input().split())))
    for j in range(C):
        if data[i][j] == 5:
            checker.append([i, j])
        elif data[i][j] > 0:
            warmers.append([data[i][j], i, j])

W = int(input())
for _ in range(W):
    a, b, c = map(int, input().split())
    walls.append([a-1, b-1, c])

wind()

# while True:
#
#     # 1. 집에 있는 모든 온풍기에서 바람이 한 번 나옴
#     wind()
#     # 2. 온도가 조절됨
#     control_temperature()
#     # 3. 온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소
#     cold_border()
#     # 4. 초콜릿을 하나 먹는다.
#     cnt += 1
#     # 조사하는 모든 칸의 온도가 K 이상이 되었는지 검사. 모든 칸의 온도가 K이상이면 테스트를 중단하고, 아니면 1부터 다시 시작한다.
#     # if testing_checker():
#     #     break
#
#     if cnt > 100:
#         cnt = 101
#         break
#
# print(cnt)