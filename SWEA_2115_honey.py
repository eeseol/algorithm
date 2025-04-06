from pprint import pprint

def comb(numbers):
    big = 0
    # 부분집합 만들기
    for i in range(1 << M):
        pick = []
        for j in range(M):
            if i & 0x01:
                pick.append(numbers[j])
            i >>= 1
        # 부분집합 다 만들었음
        # 부분집합 원소 합이 C보다 같거나 작을경우
        if sum(pick) <= C:
            temp_result = 0
            for k in pick:
                temp_result += k*k
            if big < temp_result:
                big = temp_result
    return big

T = int(input())

for test_case in range(1, T + 1):
    N, M, C = map(int, input().split())

    data = []
    memo = []

    # 데이터 입력 받기
    for _ in range(N):
        data.append(list(map(int, input().split())))

    # 꿀 값 업데이트
    for i in range(N):
        for j in range(N-M+1):
            temp_loca = []
            temp_data = []
            for k in range(M):
                # 범위 만큼.
                # temp_loca에는 좌표 입력해 주기 => 겹치는지 확인하려고
                # temp_data에는 데이터 값 입력해 주기 => 꿀 최대값 구하려고
                temp_loca.append([i, j+k])
                temp_data.append(data[i][j+k])
            # 부분집합 구하기
            memo.append([comb(temp_data), temp_loca])

    result = 0
    for i in range(len(memo)-1):
        temp_result = 0

        # 겹치는지 확인하려고 1번 일꾼이 선택한 집합의 좌표 set에 넣어주기
        check = set()
        for k in range(len(memo[i][1])):
            check.add((memo[i][1][k][0], memo[i][1][k][1]))

        for j in range(i, len(memo)):
            for x, y in memo[j][1]:
                # set에 있으면 => 일꾼 1, 2가 겹치면
                if (x, y) in check:
                    break
            else:
                if result < memo[i][0] + memo[j][0]:
                    result = memo[i][0] + memo[j][0]

    print(f'#{test_case} {result}')