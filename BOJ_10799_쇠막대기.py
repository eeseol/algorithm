stick = 0
data = list(map(str, input()))
total = 0

for index in range(len(data)):
    if data[index] == '(':
        stick += 1
    else:
        # 레이저임
        if data[index - 1] == '(':
            stick -= 1
            total += stick
        else:
            stick -= 1
            total += 1

print(total)