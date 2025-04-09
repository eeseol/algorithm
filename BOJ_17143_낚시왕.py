from pprint import  pprint

# 낚시왕 행에 상어가 있는지 확인 -> 인덱스 정보 넘겨주기
def shark_in_this_row(fisher_index):
    test_y = 0
    while test_y < R:
        # 상어 찾았어요
        if maps[test_y][fisher_index] > 0:
            return maps[test_y][fisher_index]
        test_y += 1
    return 0

def delete_shark(shark_index):
    global maps
    global sharks

    r, c, *data = sharks[shark_index]
    maps[r][c] = 0
    sharks[shark_index] = [0]

###########################메인 입니다.#################################
R, C, M = map(int, input().split())

maps = [[0]*C for _ in range(R)]

sharks = [[0]]

for i in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks.append([r, c, s, d, z])
    maps[r - 1][c - 1] = i + 1

# fisher_index = 0
# catch_total = 0
#
# while fisher_index < C:
#
#     # 낚시왕과 같은 행에 상어가 있는지 판단.
#     target_index = shark_in_this_row(fisher_index)
#     # 상어 삭제해 주기
#     delete_shark(target_index)
#     catch_total += 1

    break
pprint(maps)
print(sharks)

