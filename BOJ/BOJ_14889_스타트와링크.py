def cal(team):
    global result

    team_total = 0
    another_team_total = 0

    for i in range(N):
        if i in team:
            for j in team:
                team_total += data[i][j]
        else:
            for j in range(N):
                if not j in team:
                    another_team_total += data[i][j]

    temp_result = abs(another_team_total - team_total)

    result = min(result, temp_result)


def recursion(start, temp):

    if len(temp) == N // 2:
        cal(temp)
        return

    for i in range(start, N):
        temp.append(i)
        recursion(i + 1, temp)
        temp.pop()

N = int(input())
result = float('inf')
data = []
for _ in range(N):
    data.append(list(map(int, input().split())))

recursion(0, [])

print(result)