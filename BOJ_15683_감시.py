from copy import deepcopy


def check_area(map_data):
    global result
    something_is_here = 0

    for i in range(N):
        for j in range(M):
            if map_data[i][j] != 0:
                something_is_here += 1

    result = min(result, (M*N) - something_is_here)

def on_camera(camera_y, camera_x, camera_view, new_maps):

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    y, x = camera_y, camera_x
    for direc in camera_view:
        camera_y, camera_x = y, x
        while True:
            new_y = camera_y + dy[direc]
            new_x = camera_x + dx[direc]
            # 범위 넘어갔어요
            if not(0 <= new_y < N and 0 <= new_x < M):
                break
            # 벽 입니다
            if new_maps[new_y][new_x] == 6:
                break
            # 갈 수 있는 곳이에요
            if new_maps[new_y][new_x] == 0:
                new_maps[new_y][new_x] = 8
            camera_x = new_x
            camera_y = new_y


def recursion(start, before_maps):
    # 다 뽑았어요~~
    if start >= len(cameras):
        check_area(before_maps)
        return

    current_camera_y, current_camera_x = cameras[start]
    camera_type = maps[current_camera_y][current_camera_x]

    for camera_view in camera_direc[camera_type]:
        # new_map = deepcopy(before_maps)
        new_map = [row[:] for row in before_maps]
        on_camera(current_camera_y, current_camera_x, camera_view, new_map)
        recursion(start + 1, new_map)


##################   여기가 메인입니다   #############################################

N, M = map(int, input().split())
maps = []
cameras = []
result = float(99999)
for i in range(N):
    maps.append(list(map(int, input().split())))
    for j in range(M):
        if 1 <= maps[i][j] <= 5:
            cameras.append([i, j])

######################

camera_direc = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [0, 1, 3]],
    [[0, 1, 2, 3]],
]

recursion(0, maps)

print(result)