import copy
 
#남은 벽돌 세는 함수
def check(final_data):
    temp_result = 0
    for i in range(W):
        for j in range(H-1, -1, -1):
            # 위에 데이터가 없을 경우 탐색 중단, 다음 칸 탐색
            if final_data[j][i] == 0:
                pass
            else:
                temp_result += 1
                # 여기 기존 결과보다 커지면 걍 탐색 중단해 버리는 코드 추가하면 시간 좀 줄어들것 같음.
 
    return temp_result
 
# 중력 적용하는 함수
def gravity(g_data):
 
    for i in range(W):
 
        update_index = -1
        index = H-1
 
        while index >= 0:
            if update_index != -1:
                if g_data[index][i] != 0:
                    g_data[update_index][i] = g_data[index][i]
                    g_data[index][i] = 0
                    index = update_index-1
                    update_index = -1
                    continue
            elif update_index == -1:
                if g_data[index][i] == 0:
                    update_index = index
            index -= 1
    return(g_data)
 
 
# 연쇄 폭발하는 함수
def bomb(target_x, b_data):
    # x좌표에서 제일 위에 있는 블럭 찾기
    target_y = -1
    for i in range(H):
        if b_data[i][target_x] != 0:
            target_y = i
            break
    # 블럭이 없을 경우 함수 종료
    if target_y == -1:
        return b_data
     
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
 
    stack = []
    stack.append([target_y, target_x])
    while stack:
        y, x = stack.pop()
        power = b_data[y][x]
        b_data[y][x] = 0
 
        if power > 1:
            for i in range(1, power):
                for j in range(4):
                    new_y = y + (dy[j]*i)
                    new_x = x + (dx[j]*i)
                    if 0<= new_y <H and 0<= new_x < W and b_data[new_y][new_x] != 0:
                        stack.append([new_y, new_x])
     
    return b_data
 
def update(start, N, u_data):
 
    global result
 
    if start == N:
        for i in range(W):
            c_data = copy.deepcopy(u_data)
            new_data = bomb(i, c_data)
            temp = copy.deepcopy(gravity(new_data))
            temp_result = check(temp)      
            if result > temp_result:
                result = temp_result
 
    else:
        for i in range(W):
            c_data = copy.deepcopy(u_data)
            new_data = bomb(i, c_data)
            temp = copy.deepcopy(gravity(new_data))
            update(start+1, N, temp)
 
T = int(input())
 
for test_case in range(1, T + 1):
     
    N,  W, H = list(map(int, input().split()))
    result = float('inf')
    # data 받기
    data = []
    for i in range(H):
        data.append(list(map(int, input().split())))
 
    update(1, N, data)
    print(f'#{test_case} {result}')