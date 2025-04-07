from pprint import pprint
def check_wall_for_control(d, r, c, new_r, new_c):
    for wall in walls:
        x, y, t = wall
        if d == 1 and t == 1 and x == r and y == c:  # 오른쪽
            return False
        if d == 2 and t == 1 and x == r and y == new_c:  # 왼쪽
            return False
        if d == 3 and t == 0 and x == r and y == c:  # 위
            return False
        if d == 4 and t == 0 and x == new_r and y == c:  # 아래
            return False
    return True

def check_wall(d, r, c, new_r, new_c):
    global walls

    # 위/아래 벽 여부 확인 함수
    def is_wall_between(a, b, t):
        for wall in walls:
            if wall == [a, b, t]:
                return True
        return False

    # 바람 방향별 조건 설정
    if d == 1:  # 오른쪽
        if new_r == r - 1 and new_c == c + 1:
            return not is_wall_between(r, c, 0) and not is_wall_between(r - 1, c, 1)
        elif new_r == r and new_c == c + 1:
            return not is_wall_between(r, c, 1)
        elif new_r == r + 1 and new_c == c + 1:
            return not is_wall_between(r, c, 0) and not is_wall_between(r + 1, c, 1)

    elif d == 2:  # 왼쪽
        if new_r == r - 1 and new_c == c - 1:
            return not is_wall_between(r, c, 0) and not is_wall_between(r - 1, c - 1, 1)
        elif new_r == r and new_c == c - 1:
            return not is_wall_between(r, c - 1, 1)
        elif new_r == r + 1 and new_c == c - 1:
            return not is_wall_between(r, c, 0) and not is_wall_between(r + 1, c - 1, 1)

    elif d == 3:  # 위쪽
        if new_r == r - 1 and new_c == c - 1:
            return not is_wall_between(r, c, 1) and not is_wall_between(r, c - 1, 0)
        elif new_r == r - 1 and new_c == c:
            return not is_wall_between(r, c, 0)
        elif new_r == r - 1 and new_c == c + 1:
            return not is_wall_between(r, c, 1) and not is_wall_between(r, c + 1, 0)

    elif d == 4:  # 아래쪽
        if new_r == r + 1 and new_c == c - 1:
            return not is_wall_between(r + 1, c, 1) and not is_wall_between(r + 1, c - 1, 0)
        elif new_r == r + 1 and new_c == c:
            return not is_wall_between(r + 1, c, 0)
        elif new_r == r + 1 and new_c == c + 1:
            return not is_wall_between(r + 1, c, 1) and not is_wall_between(r + 1, c + 1, 0)

    return False


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
            # 온도있는 칸 발견! 온도 퍼트려보자
            if real_map[r][c] != 0:
                temp_result = 0
                # 델타 레츠기릿릿
                for k in range(1, 5):
                    new_r = r + dr[k]
                    new_c = c + dc[k]
                    # 범위 확인
                    if not (0 <= new_r < R and 0 <= new_c < C):
                        continue
                    # 확산 이니까 높은곳에서 낮은곳으로 가야겠죠
                    if real_map[r][c] > real_map[new_r][new_c]:
                        # true면 벽 없다는 뜻임.
                        if check_wall_for_control(k, r, c, new_r, new_c) == False:
                            continue
                        update_number = (real_map[r][c] - real_map[new_r][new_c])//4
                        temp_map[new_r][new_c] += update_number
                        temp_result += update_number
                temp_map[r][c] += real_map[r][c] - temp_result
    real_map = [row[:] for row in temp_map]

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

    for check in checker:
        if real_map[check[0]][check[1]] < K:
            return False
    return True

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

while True:

    # 1. 집에 있는 모든 온풍기에서 바람이 한 번 나옴
    wind()
    # 2. 온도가 조절됨
    control_temperature()
    # 3. 온도가 1 이상인 가장 바깥쪽 칸의 온도가 1씩 감소
    cold_border()
    # 4. 초콜릿을 하나 먹는다.
    cnt += 1
    # 조사하는 모든 칸의 온도가 K 이상이 되었는지 검사. 모든 칸의 온도가 K이상이면 테스트를 중단하고, 아니면 1부터 다시 시작한다.
    if testing_checker():
        break
    if cnt > 100:
        cnt = 101
        break

print(cnt)