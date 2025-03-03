# 답은 쉽게 구하는데 시간관리가 좀 빡센 문제,,
def check(new_data):
    global K
    for i in range(W):
        cnt = 1
        for j in range(0, D-1):
            if new_data[j][i] == new_data[j+1][i]:
                cnt += 1
            else:
                cnt = 1
            if cnt >= K:
                break
        else:
            return False
    return True

def update(temp, change_number, change_row):
    temp[change_row] = [change_number]*W

def logic(new_data, start = 0, already = []):
    global time
    if check(new_data):
        if time > start:
            time = start
            return
    if  start >= time or len(already) == D:
        return

    for i in range(D):
        if i in already:
            pass
        else:
            origin = new_data[i][:]

            update(new_data, 0, i)
            logic(new_data, start + 1, already + [i])

            update(new_data, 1, i)
            logic(new_data, start + 1, already + [i])

            new_data[i] = origin

T = int(input())

for test_case in range(1, T + 1):
    time = float('inf')
    D, W, K = list(map(int, input().split()))

    data = []
    for i in range(D):
        data.append(list(map(int, input().split())))

    logic(data)

    print(f'#{test_case} {time}')