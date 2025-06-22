from collections import deque

def check_bfs(group):

    if len(group) == 0 or len(group) == N:
        return
    
    de = deque()
    de.append(group[0])
    check_node = set()

    while de:
        node = de.popleft()
        check_node.add(node)
        for new_node_index in range(len(graph[node])):
            new_node = graph[node][new_node_index]
            if (new_node in check_node) or (new_node not in group):
                continue
            check_node.add(new_node)
            de.append(graph[node][new_node_index])

    if len(check_node) == len(group):
        return True
    else:
        return False


N = int(input())

result = -1
people = [0] + list(map(int, input().split()))
graph = [[0] for _ in range(N + 1)]

for i in range(1, N + 1):
    a, *temp = list(map(int, input().split()))
    graph[i] = temp

for i in range((1<<N)//2):
    A_group = []
    B_group = []
    A_population = 0
    B_population = 0
    for k in range(1, 1 + N):
        if i & 0x01:
            A_population += people[k]
            A_group.append(k)
        else:
            B_population += people[k]
            B_group.append(k)
        i >>= 1
    
    if check_bfs(A_group) and check_bfs(B_group):
        if result == -1:
            result = abs(A_population - B_population)
        else:
            result = min(result, abs(A_population - B_population))

print(result)