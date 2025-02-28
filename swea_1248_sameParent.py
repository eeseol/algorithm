from pprint import pprint

def up(a_index, b_index):
    global result
    global cnt
    if a_index != 0 and data[a_index]:
        if data[a_index][0] != None:
            a_index = data[a_index][0]
            if visited[a_index]:
                result = a_index
                return
            visited[a_index] = True
        else:
            a_index = 0
    
    if b_index != 0 and data[b_index]:
        if data[b_index][0] != None:
            b_index = data[b_index][0]
            if visited[b_index]:
                result = b_index
                return
            visited[b_index] = True
        else:
            b_index = 0
    up(a_index, b_index)
    
def dfs(index):
    global cnt

    if data_low[index]:
        for da in data_low[index]:
            cnt += 1
            dfs(da)


T = int(input())

for test_case in range(1, T + 1):
    result = 0
    cnt = 1
    V, E, A, B = list(map(int, input().split()))

    temp = list(map(int, input().split()))

    data = [[] for _ in range(V+1)]
    data_low = [[] for _ in range(V+1)]
    visited = [False]*(V+1)

    for i in range(0, len(temp), 2):
        p = temp[i]
        c = temp[i+1]
        data[c].append(p)
        data_low[p].append(c)
    visited[A] = True
    visited[B] = True
    up(A, B)

    dfs(result)
    print(f'#{test_case} {result} {cnt}')
