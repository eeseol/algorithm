import heapq

N, K = map(int, input().split())
jewels = []
bags = []

for _ in range(N):
    m, v = map(int, input().split())
    jewels.append((m, v))

for _ in range(K):
    bags.append(int(input()))


jewels.sort()
bags.sort()

result = 0
hq = []
jewel_idx = 0

for bag_weight in bags:
    # 이 가방에 담을 수 있는 모든 보석 후보를 heap에 넣음
    while jewel_idx < N and jewels[jewel_idx][0] <= bag_weight:
        # 가치 기준으로 최대힙 만들기
        heapq.heappush(hq, -jewels[jewel_idx][1])
        jewel_idx += 1

    # 가장 비싼 보석 하나 꺼내서 result에 더함
    if hq:
        result += -heapq.heappop(hq)

print(result)
