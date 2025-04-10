S, P = map(int, input().split())

data = list(map(str, input()))
number = list(map(int, input().split()))

total = 0

check = [0, 0, 0, 0]

for i in range(S):


    if data[i] == 'A':
        check[0] += 1
    elif data[i] == 'C':
        check[1] += 1
    elif data[i] == 'G':
        check[2] += 1
    else:
        check[3] += 1

    if sum(check) == P:
        if check[0] >= number[0]:
            if check[1] >= number[1]:
                if check[2] >= number[2]:
                    if check[3] >= number[3]:
                        total += 1
        index = i - P + 1
        if data[index] == 'A':
            check[0] -= 1
        elif data[index] == 'C':
            check[1] -= 1
        elif data[index] == 'G':
            check[2] -= 1
        else:
            check[3] -= 1


print(total)