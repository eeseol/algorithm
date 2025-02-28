from collections import deque

def dfs(index):
    
    for i in data[index]:
        if visited[i] == True:
            continue
        dfs(i)
    de.append(index)
    visited[index] = True


for test_case in range(1, 11):
    V, E = list(map(int, input().split()))

    data = [[] for _ in range(V+1)]
    de = deque()
    visited = [[False] for _ in range(V+1)]

    temp = list(map(int, input().split()))

    for i in range(0, len(temp), 2):
        data[temp[i]].append(temp[i+1])

    for i in range(1, V+1):
        dfs(i)

    print(*de)