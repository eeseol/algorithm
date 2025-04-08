# 파이프의 현재 상태 반환하는 함수
def check_state():
    '''
    가로 = 1, 세로 = 2, 대각선 = 3
    '''
    first_pipe = pipe[0]
    second_pipe = pipe[1]
    # 가로인지 확인
    if first_pipe[0] == second_pipe[0]:
        return 1
    elif first_pipe[1] == second_pipe[1]:
        return 2
    else:
        return 3

def can_move(state, num):   # 매개변수(파이프 상태, 바꿀 인덱스번호)

    def check_left():
        second_pipe = pipe[1]
        new_y = second_pipe[0]
        new_x = second_pipe[1] + 1
        # 범위 확인
        if not(0 <= new_x < N and 0 <= new_y < N):
            return False
        if maps[new_y][new_x] == 1:
            return False
        return True

    def check_down():
        second_pipe = pipe[1]
        new_y = second_pipe[0] + 1
        new_x = second_pipe[1]
        # 범위 확인
        if not(0 <= new_x < N and 0 <= new_y < N):
            return False
        if maps[new_y][new_x] == 1:
            return False
        return True

    def check_middle():
        second_pipe = pipe[1]
        new_y = second_pipe[0] + 1
        new_x = second_pipe[1] + 1
        # 범위 확인
        if not(0 <= new_x < N and 0 <= new_y < N):
            return False
        if maps[new_y][new_x] == 1:
            return False
        return True

    check_color = ''
    if state == 1:
        if num == 0:
            check_color = 'yellow'
        else:
            check_color = 'blue'
    elif state == 2:
        if num == 0:
            check_color = 'green'
        else:
            check_color = 'blue'
    else:
        if num == 0:
            check_color = 'yellow'
        elif num == 1:
            check_color = 'green'
        else:
            check_color = 'blue'

    if check_color == 'yellow':
        return check_left()
    elif check_color == 'green':
        return check_down()
    else:
        if check_left() == False:
            return False
        if check_down() == False:
            return False
        if check_middle() == False:
            return False
        return True


def dfs():
    global result

    second_pipe = pipe[1]
    # 끝 지점에 도달했을 경우
    if second_pipe[0] == N-1 and second_pipe[1] == N-1:
        result += 1
        return
    # 현재 파이프 상태 저장하는 변수
    state = check_state()

    for method in range(len(positive[state])):
        # 갈 수 없는 경우
        if can_move(state, method) == False:
            continue
        # 갈 수 있을 때
        f_pipe = [pipe[0][0], pipe[0][1]]
        s_pipe = [pipe[1][0], pipe[1][1]]

        # 첫번재 파이프 y좌표, x좌표 업데이트
        pipe[0][0] += positive[state][method][0][0]
        pipe[0][1] += positive[state][method][0][1]
        # 두번재 파이프 y좌표, x좌표 업데이트
        pipe[1][0] += positive[state][method][1][0]
        pipe[1][1] += positive[state][method][1][1]

        dfs()

        pipe[0] = f_pipe
        pipe[1] = s_pipe


N = int(input())

maps = []
pipe = [[0, 0], [0, 1]]
result = 0
positive = {
    1: [[[0, 1], [0, 1]], [[0, 1], [1, 1]]],
    2: [[[1, 0], [1, 0]], [[1, 0], [1, 1]]],
    3: [[[1, 1], [0, 1]], [[1, 1], [1, 0]], [[1, 1], [1, 1]]]
}

for _ in range(N):
    maps.append(list(map(int, input().split())))

dfs()


print(result)