from copy import deepcopy

def select_enemy(shooter_x):
    cal_distance_enemy = []
    shooter_y = N

    # 적과의 거리를 변수에 다 저장
    for each_enemy in real_enemy:
        reach = abs(shooter_y - each_enemy[0]) + abs(shooter_x - each_enemy[1])
        # 거리, x좌표, y좌표 => 정렬을 위해
        cal_distance_enemy.append([reach, each_enemy[1], each_enemy[0]])

    sorted(cal_distance_enemy)
    # return 줄 때는 y좌표, x좌표로 전달
    return cal_distance_enemy[0][2], cal_distance_enemy[0][1]


def kill_enemy():
    pass

def move_enemy():
    pass

def locate_shooter(start, pick):
    if len(pick) == 3:
        # 여기 조합 끝났어요
        where_shooters.append(pick)
        return

    for i in range(start, M):
        pick.append(i)
        locate_shooter(i + 1, pick)
        pick.pop()

N, M, D = map(int, input().split())

maps = []           # 전체 지도
where_shooters = [] # 궁수가 위치할 수 있는 모든 경우의 수.
enemy = []          # 적 좌표가 저장된 변수
big_kill = 0        # 처리한 최대 적의 수

# 지도 입력 받는 반복문
for i in range(N):
    maps.append(list(map(int, input().split())))
    for j in range(M):
        enemy.append([i, j])

# 궁수 위치 경우의 수
locate_shooter(0, [])

# 궁수 위치 경우의 수마다 도는 반복문
for here_shooters in where_shooters:
    real_enemy = deepcopy(enemy)
    kill_number = 0

    # 적이 지도에 다 없어질 때까지 도는 반복문
    while len(real_enemy) != 0:

        for shooter in here_shooters:
            select_enemy(shooter)

        kill_enemy()

        move_enemy()

    big_kill = max(big_kill, kill_number)

print(big_kill)

