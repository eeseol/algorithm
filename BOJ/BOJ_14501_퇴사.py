def dfs(index, end_date, price):
    global final_price
    if index >= len(data):
        final_price = max(final_price, price)
        return

    if end_date < data[index][0]:
        dfs(index+1, data[index][1], price + data[index][2])
    dfs(index+1, end_date, price)

N = int(input())

data = []

for i in range(N):
    final_price = 0
    a, b = map(int, input().split())
    if a + i > N:
        continue
    data.append([i, a + i - 1, b])

dfs(0, -1, 0)

print(final_price)

