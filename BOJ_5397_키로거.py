from collections import deque

T = int(input())

for test_case in range(1, T + 1):

    data = list(map(str, input()))
    left = deque()
    right = deque()

    for i in range(len(data)):
        if data[i] == '<':
            if left:
                right.appendleft(left.pop())
        elif data[i] == '>':
            if right:
                left.append(right.popleft())
        elif data[i] == '-':
            if left:
                left.pop()
        else:
            left.append(data[i])

    while left:
        print(left.popleft(), end="")
    while right:
        print(right.popleft(), end="")
    print("")