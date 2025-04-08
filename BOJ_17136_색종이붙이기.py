
def attach(row, col, sized, state):
    global maps
    global remain_one

    if state == 'at':
        for i in range(sized):
            for j in range(sized):
                new_row = row + i
                new_col = col + j
                maps[new_row][new_col] = 0
                remain_one -= 1
    else:
        for i in range(sized):
            for j in range(sized):
                new_row = row + i
                new_col = col + j
                maps[new_row][new_col] = 1
                remain_one += 1

def can_attach(row, col, sized):
    for i in range(sized):
        for j in range(sized):
            new_row = row + i
            new_col = col + j
            # 일단 범위 확인
            if not(0 <= new_row < 10 and 0 <= new_col < 10):
                return False
            if maps[new_row][new_col] == 0:
                return False
    return True

def dfs(pos, used_paper):
    global minimum_paper

    # 가지치기. 지금쓴 종이가 최소 종이보다 크면 그냥 종료.
    if used_paper > minimum_paper:
        return

        # 모든 곳에 색종이 다 붙였을 경우
    if remain_one == 0:
        minimum_paper = min(minimum_paper, used_paper)
        return

    for i in range(pos, 100):
        c = i % 10
        r = i // 10

        # 색종이 붙일 수 없는 좌표면 넘어가기
        if maps[r][c] == 0:
            continue

        # 색종이 붙일 수 있는 좌표
        # 색종이 크기 큰것부터 붙여보기
        for size in range(5, 0, -1):
            # 해당 사이즈의 색종이가 하나도 없을 경우 넘어가기
            if paper[size] <= 0:
                continue
            # 붙일 수 있는 곳이면
            if can_attach(r, c, size):
                # 색종이 붙이기 (mpas에 업데이트)
                attach(r, c, size, 'at')
                # 색종이 개수 하나 줄이기
                paper[size] -= 1
                # 다음 좌표들 확인하러 가기
                dfs(i, used_paper + 1)
                # 색종이 떼기
                attach(r, c, size, 'de')
                # 색종이 개수 하나 늘이기
                paper[size] += 1
        return


# 지도 정보 업데이트 받기
maps = []
check_location = []
remain_one = 0
for i in range(10):
    maps.append(list(map(int, input().split())))
    for j in range(10):
        if maps[i][j] == 1:
            check_location.append([i, j])
            remain_one += 1

# 남은 색종이 개수 저장한 변수
paper = [0, 5, 5, 5, 5, 5]
minimum_paper = float('inf')

dfs(0, 0)

if minimum_paper == float('inf'):
    minimum_paper = -1

print(minimum_paper)