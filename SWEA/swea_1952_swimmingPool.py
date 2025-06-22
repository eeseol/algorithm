T = int(input())

def min_cost(month, cost):
    global min_total_cost
    if month >= 12:  # 12개월을 모두 탐색하면 최소 비용 업데이트
        min_total_cost = min(min_total_cost, cost)
        return

    # 1일 이용권 vs 1달 이용권 중 최적 선택
    min_cost(month + 1, cost + min(plan[month] * day_fee, month_fee))

    # 3달 이용권 선택
    if month <= 9:  # 3달 이용권은 10월까지만 선택 가능
        min_cost(month + 3, cost + three_fee)

    # 1년 이용권 선택 (한 번만 선택 가능)
    if month == 0:  # 1월에서만 선택 가능
        min_cost(12, cost + year_fee)

for test_case in range(1, T + 1):
    day_fee, month_fee, three_fee, year_fee = map(int, input().split())
    plan = list(map(int, input().split()))

    min_total_cost = year_fee  # 최소 비용을 1년 이용권으로 초기화
    min_cost(0, 0)  # DP 백트래킹 실행

    print(f'#{test_case} {min_total_cost}')
