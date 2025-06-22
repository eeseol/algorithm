import copy

T = int(input())

def save_distance():
    global distance
    for i in range(len(people)):
        people_y, people_x = people[i]
        for j in range(len(stair)):
            stair_y, stair_x = stair[j]
            distance[i].append(abs(people_y - stair_y) + abs(people_x - stair_x))

def match_people_stair(people_index = 0): 
    global distance
    if people_index == len(people):
        temp_data = copy.deepcopy(go_stair)
        logic(temp_data)
        return
    
    for i in range(len(stair)):
        go_stair[i].append([people_index, distance[people_index][i]])
        match_people_stair(people_index+1)
        go_stair[i].pop()

def logic(co_go_stair):
    global cnt
    temp_cnt = 0
    flag = 0
    flag2 =0
    waiting = [[] for _ in range(len(stair))]
    moving = [[] for _ in range(len(stair))]

    while flag2 != len(people):
        temp_cnt += 1
        if flag != len(people):
            for i in range(len(co_go_stair)):
                for j in range(len(co_go_stair[i])):
                    # 0이 아닐때 줄여주기기
                    if co_go_stair[i][j][1] != 0:
                        co_go_stair[i][j][1] -= 1
                        # 계단에 도착!
                        if co_go_stair[i][j][1] == 0:
                            flag += 1
                            # waiting 변수에 넣어주기
                            waiting[i].append(co_go_stair[i][j][0])
        
        # 여기에 moving
        for i in range(len(stair)):
            index = 0
            while index != len(moving[i]):
                moving[i][index][1] += 1
                if moving[i][index][1] == data[stair[i][0]][stair[i][1]]:
                    del moving[i][index]
                    flag2 += 1
                else:
                    index += 1

        for i in range(len(stair)):
            for j in range(len(waiting[i])):
                if len(moving[i]) == 3:
                    break
                else:
                    moving[i].append([waiting[i][-1], 0])  
                    waiting[i].pop()
        

    if temp_cnt < cnt:
        cnt = temp_cnt
        
for test_case in range(1, T + 1):
    N = int(input())
    data = []
    people = []
    stair = []
    cnt = float('inf')
    for i in range(N):
        data.append(list(map(int, input().split())))
        for j in range(N):
            if data[i][j] == 1:
                people.append([i, j])
            elif data[i][j] > 1:
                stair.append([i, j])

    go_stair = [[] for _ in range(len(stair))]
    distance = [[] for _ in range(len(people))]
    save_distance()
    match_people_stair()

    print(f'#{test_case} {cnt + 1}')