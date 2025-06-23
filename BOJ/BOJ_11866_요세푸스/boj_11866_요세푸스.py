from collections import deque

N, K = list(map(int, input().split()))

a = deque()
result = []
for i in range(N):
    a.append(i+1)


for i in range(N):
    for j in range(K - 1):
        temp = a.popleft()
        a.append(temp)
    result.append(a.popleft())
        

print("<", end="")
print(', '.join(map(str, result)), end="")
print(">")