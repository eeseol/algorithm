





########################메인 함수는 아니고 메인입니다####################################

N = int(input())

maps = []
shark_locate = []
shark_size = 1
shark_eaten = 0

for _ in range(N):
    maps.append(list(map(int, input().split())))

# while True:
#
#
