def cal_distance(first, second):
    global result
    global data
    a = 0
    b = 0

    for i in first:
        for j in first:
            if i != j:
                a += data[i][j]
    for i in second:
        for j in second:
            if i != j:
                b += data[i][j]
    temp_result = abs(a-b)
    if result > temp_result:
        result = temp_result

def select(start = 0, first = []):
    if len(first) == N//2:
        second = []
        for i in range(N):
            if not(i in first):
                second.append(i)
        cal_distance(first, second)
    else:
        for i in range(start, N):
                first.append(i)
                select(i+1,first)
                first.pop()


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    result = float('inf')
    data = []
    for i in range(N):
        data.append(list(map(int, input().split())))

    select()

    print(f'#{test_case} {result}')