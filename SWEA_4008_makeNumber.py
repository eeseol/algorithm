
def cal(susic):
    global big
    global small
    index = 1
    temp_result = numbers[0]
    for i in susic:
        if i == 0:
            temp_result += numbers[index]
        elif i == 1:
            temp_result -= numbers[index]
        elif i == 2:
            temp_result *= numbers[index]
        else:
            temp_result = int(temp_result / numbers[index])
        index += 1
    # print(susic, temp_result)
    big = max(big, temp_result)
    small = min(small, temp_result)

def dfs(temp=[]):
    global symbol
    if len(temp) == N - 1:
        cal(temp)
        return
    for i in range(4):
        if symbol[i] > 0:
            temp.append(i)
            symbol[i] -= 1
            dfs(temp)
            temp.pop()
            symbol[i] += 1


T = int(input())

for test_case in range(1, T+1):
    big = -100000000
    small = float('inf')
    N = int(input())
    symbol = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    dfs()

    print(f'#{test_case} {big-small}')

