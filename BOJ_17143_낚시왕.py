from pprint import pprint

# 낚시왕 행에 상어가 있는지 확인 -> 인덱스 정보 넘겨주기
def shark_in_this_row(fisher_index):
    '''
    수면과 가까운 상어의 고유 인덱스 반환하는 함수
    상어 없으면 0 반환
    '''
    test_y = 0
    while test_y < R:
        # 상어 찾았어요
        if maps[test_y][fisher_index] > 0:
            return maps[test_y][fisher_index]
        test_y += 1
    return 0

def delete_shark(shark_index):
    global maps
    global sharks

    r, c, *data = sharks[shark_index]
    if maps[r][c] == shark_index:
        maps[r][c] = 0
    sharks[shark_index] = [0]

def move_shark():
    global sharks
    global maps
    total_shark = len(sharks)
    visited = [False]*total_shark
    dx = [0, 0, 0, 1, -1]  # 1번 인덱스 부터 위, 아래, 오른쪽, 왼쪽
    dy = [0, -1, 1, 0, 0]

    for shark_index in range(1, len(sharks)):
        # 이미 죽은 상어 일 경우 건너뛰기
        if len(sharks[shark_index]) == 1:
            continue
        # 가독성을 위해 변수 만들어 줬어요
        shark_y, shark_x, shark_speed, shark_direction, shark_size = sharks[shark_index]

        # 방향 안 바뀌는 상어 좌표 업데이트
        new_shark_y, new_shark_x, new_shark_direction = update_shark_xy(shark_y, shark_x, shark_speed, shark_direction)
        # print(f'상어 인덱스 : {shark_index}')
        # print(f'기존 y : {shark_y}, 기존 x {shark_x}, 기존 방향 {shark_direction}')
        # print(f'기존 y : {new_shark_y}, 기존 x {new_shark_x}, 기존 방향 {new_shark_direction}')
        # continue


        # 해당 장소에 아무 상어도 없을 경우
        if maps[new_shark_y][new_shark_x] == 0:
            maps[new_shark_y][new_shark_x] = shark_index
            if maps[shark_y][shark_x] == shark_index:
                maps[shark_y][shark_x] = 0
            sharks[shark_index] = [new_shark_y, new_shark_x, shark_speed, new_shark_direction, shark_size]
            visited[shark_index] = True
        # 해당 장소에 상어 있어요
        else:
            another_shark_index = maps[new_shark_y][new_shark_x]
            # 해당 장소에 상어가 아직 이동 전이었어요.
            if visited[another_shark_index] == False:
                if maps[shark_y][shark_x] == shark_index:
                    maps[shark_y][shark_x] = 0
                maps[new_shark_y][new_shark_x] = shark_index
                sharks[shark_index] = [new_shark_y, new_shark_x, shark_speed, new_shark_direction, shark_size]
                visited[shark_index] = True
            # 이미 이동한 상어였어요
            else:
                if maps[shark_y][shark_x] == shark_index:
                    maps[shark_y][shark_x] = 0
                # 작은 상어 선택해요.
                if shark_size < sharks[another_shark_index][4]:
                    delete_shark(shark_index)
                else:
                    delete_shark(another_shark_index)
                    maps[new_shark_y][new_shark_x] = shark_index
                    sharks[shark_index] = [new_shark_y, new_shark_x, shark_speed, new_shark_direction, shark_size]
                    visited[shark_index] = True
        # print(f'상어 인덱스 : {shark_index}')
        # print(f'기존 y : {shark_y}, 기존 x {shark_x}, 기존 방향 {shark_direction}')
        # print(f'기존 y : {new_shark_y}, 기존 x {new_shark_x}, 기존 방향 {new_shark_direction}')
        # pprint(maps)
        # print("================================================")



def change_diraction(now_direc):
    if now_direc == 1:
        return 2
    elif now_direc == 2:
        return 1
    elif now_direc == 3:
        return 4
    else:
        return 3

def update_shark_xy(y, x, speed, direction):
    if direction == 1 or direction == 2:  # 위(1), 아래(2)
        cycle = (R - 1) * 2
        move = speed % cycle
        for _ in range(move):
            if direction == 1 and y == 0:
                direction = 2
            elif direction == 2 and y == R - 1:
                direction = 1
            y += -1 if direction == 1 else 1
    else:  # 오른쪽(3), 왼쪽(4)
        cycle = (C - 1) * 2
        move = speed % cycle
        for _ in range(move):
            if direction == 4 and x == 0:
                direction = 3
            elif direction == 3 and x == C - 1:
                direction = 4
            x += -1 if direction == 4 else 1
    return y, x, direction

#####################################################################
# 각 상어는 고유 index를 가진다.
# maps에는 상어가 있는 위치마다 상어 고유의 index가 저장되어 있다.
# 상어 리스트의 인덱스가 각 상어의 고유 인덱스이다.
# 여러마리 도달하는건 visted 써서 처리.
###########################메인 입니다.#################################
R, C, M = map(int, input().split())

maps = [[0]*C for _ in range(R)]

sharks = [[0]]

# 상어 정보 넣어주기. index 1부터 시작하는 걸로 입력 들어옵니다.. -1해주기
for i in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks.append([r - 1, c - 1, s, d, z])
    maps[r - 1][c - 1] = i + 1

fisher_index = 0  # 낚시왕 현재 위치
catch_total = 0   # 낚시왕이 잡은 상어 마릿수

while fisher_index < C:

    # 낚시왕과 같은 행에 상어가 있는지 판단.
    target_index = shark_in_this_row(fisher_index)

    # 상어 삭제해 주기
    if target_index != 0:
        catch_total += sharks[target_index][4]
        delete_shark(target_index)

    # 상어 이동
    move_shark()
    # 낚시왕 한칸 이동
    fisher_index += 1

# pprint(maps)
# print(sharks)

print(catch_total)

