# 10x10 종이 상태 입력 받기
maps = [list(map(int, input().split())) for _ in range(10)]

# 색종이 종류별 개수: 인덱스 1~5를 쓰기 위해 0은 dummy로 둔다
# 각 크기의 색종이는 5장씩 있음
papers = [0, 5, 5, 5, 5, 5]

# 사용할 색종이의 최소 개수를 저장하는 변수
# 색종이는 최대 5개씩 * 5종류 = 25장 이므로, 26으로 초기화 (절대 나올 수 없는 수)
min_used = 26


# (y, x) 위치에 size x size 크기의 색종이를 붙일 수 있는지 확인하는 함수
def can_attach(y, x, size):
    # 종이의 경계를 넘는 경우는 불가능
    if y + size > 10 or x + size > 10:
        return False
    # 범위 내 모든 칸이 1(붙여야 할 부분)인지 확인
    for i in range(y, y + size):
        for j in range(x, x + size):
            if maps[i][j] != 1:
                return False
    return True


# (y, x) 위치에 size x size 크기의 색종이를 value(0 or 1)로 붙이거나 떼는 함수
# value=0이면 색종이 붙이기 (1 → 0), value=1이면 되돌리기 (0 → 1)
def attach(y, x, size, value):
    for i in range(y, y + size):
        for j in range(x, x + size):
            maps[i][j] = value


# DFS 탐색 함수
# pos: 현재 탐색 위치(0~99), used_count: 지금까지 사용한 색종이 수
def dfs(pos, used_count):
    global min_used

    # 이미 현재까지 쓴 색종이 수가 최소보다 많으면 더 볼 필요 없음 (가지치기)
    if used_count >= min_used:
        return

    # pos부터 끝(100칸)까지 순차적으로 탐색
    for i in range(pos, 100):
        y, x = divmod(i, 10)  # 0~99를 2차원 좌표로 변환
        if maps[y][x] == 1:
            # 현재 위치가 1이라면 (색종이 붙여야 한다면), 큰 색종이부터 시도
            for size in range(5, 0, -1):
                if papers[size] > 0 and can_attach(y, x, size):
                    # 색종이 붙이기
                    attach(y, x, size, 0)
                    papers[size] -= 1

                    # 다음 위치로 재귀 호출
                    dfs(i, used_count + 1)

                    # 백트래킹 (되돌리기)
                    attach(y, x, size, 1)
                    papers[size] += 1
            # 이 칸은 반드시 처리돼야 하므로, 한 번이라도 색종이 붙였으면 더 볼 필요 없음
            return

    # 여기까지 왔다는 건 모든 1이 0으로 덮였다는 뜻 → 최소 사용 수 갱신
    min_used = min(min_used, used_count)


# 탐색 시작: 맨 처음 위치 pos = 0, 색종이 사용 개수 = 0
dfs(0, 0)

# 결과 출력: 색종이로 다 덮었으면 최소값 출력, 아니면 -1
print(min_used if min_used != 26 else -1)
