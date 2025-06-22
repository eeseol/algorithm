import heapq

# pick은 home 리스트에서 선택된 대피소의 인덱스 번호.
def find_big_distance(pick):
    global result

    now_distance = []
    for index_home in range(N):
        each_distance = []
        for place in pick:
            di = memo[index_home][place]
            heapq.heappush(each_distance, di)
        each_short_distance = heapq.heappop(each_distance)
        heapq.heappush(now_distance, -each_short_distance)

    far_distance = heapq.heappop(now_distance)

    result = min(result, -far_distance)


def recursion(start, pick):

    if len(pick) == K:
        find_big_distance(pick)
        return

    for i in range(start, N):
        pick.append(i)
        recursion(i + 1, pick)
        pick.pop()

###############메인입니다####################

N, K = map(int, input().split())
result = float('inf')
home = []
memo = [[0] * N for _ in range(N)]
for _ in range(N):
    y, x = map(int, input().split())
    home.append([y, x])

# 각 노드당 거리 업데이트
for i in range(N):
    for j in range(i, N):
        distance = abs(home[i][0] - home[j][0]) + abs(home[i][1] - home[j][1])
        memo[i][j] = distance
        memo[j][i] = distance

recursion(0, [])
print(result)