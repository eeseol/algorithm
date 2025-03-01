from collections import deque

def dfs(index):
    global de
    global visited

    if len(data[index]) == 0:
        de.appendleft(index)
        visited[index] = True

    else:
        for new_index in data[index]:
            if visited[new_index] == False:
                dfs(new_index)
        de.appendleft(index)
        visited[index] = True


for test_case in range(1, 11):
    V, E = list(map(int, input().split()))

    data = [[] for _ in range(V+1)]
    de = deque()
    visited = [False for _ in range(V+1)]

    temp = list(map(int, input().split()))

    # 간선 정보 data 변수에 장 부모, 자식식
    for i in range(0, len(temp), 2):
        data[temp[i]].append(temp[i+1])

    for i in range(1, V+1):
        if visited[i] == False:
            dfs(i)

    print(f'#{test_case}', end=" ")
    print(*de)

