def josephus_recursive(N, K):
    """
    재귀를 사용한 요세푸스 문제 해결
    시간복잡도: O(N)
    공간복잡도: O(N) - 재귀 호출 스택
    """
    if N == 1:
        return 1
    
    # J(N, K) = (J(N-1, K) + K - 1) % N + 1
    return (josephus_recursive(N - 1, K) + K - 1) % N + 1

def josephus_sequence_recursive(N, K):
    """
    재귀를 사용하여 전체 요세푸스 순열 구하기
    시간복잡도: O(N^2)
    공간복잡도: O(N)
    """
    result = []
    for i in range(1, N + 1):
        # i번째 제거될 사람을 찾기 위해 i명으로 요세푸스 문제 해결
        survivor = josephus_recursive(i, K)
        result.append(survivor)
    
    return result

# 입력 받기
N, K = map(int, input().split())

# 결과 계산
result = josephus_sequence_recursive(N, K)

# 출력
print("<", end="")
print(', '.join(map(str, result)), end="")
print(">") 