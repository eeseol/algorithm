def dfs(index, result):
    global result_max
    global result_min

    if index == N:
        result_max = max(result_max, result)
        result_min = min(result_min, result)
        return

    for i in range(4):
        if symbol[i] > 0:
            symbol[i] -= 1
            if i == 0:
                dfs(index + 1, result + numbers[index])
            elif i == 1:
                dfs(index + 1, result - numbers[index])
            elif i == 2:
                dfs(index + 1, result * numbers[index])
            else:
                if result < 0 and numbers[index] > 0:
                    temp_result = abs(result)//numbers[index]
                    temp_result = -temp_result
                else:
                    temp_result = result//numbers[index]
                dfs(index + 1, temp_result)
            symbol[i] += 1



N = int(input())
numbers = list(map(int, input().split()))
symbol = list(map(int, input().split()))
result_max = -1000000000
result_min = float('inf')

dfs(1, numbers[0])

print(result_max)
print(result_min)