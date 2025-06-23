def josephus_iterative(N, K):
    """
    반복문을 사용한 요세푸스 문제 해결
    시간복잡도: O(N)
    공간복잡도: O(1)
    """
    result = 0
    for i in range(2, N + 1):
        result = (result + K) % i
    return result + 1

def josephus_sequence_iterative(N, K):
    """
    반복문을 사용하여 전체 요세푸스 순열 구하기
    시간복잡도: O(N^2)
    공간복잡도: O(N)
    """
    result = []
    for i in range(1, N + 1):
        survivor = josephus_iterative(i, K)
        result.append(survivor)
    
    return result

# 입력 받기
N, K = map(int, input().split())

# 결과 계산
result = josephus_sequence_iterative(N, K)

# 출력
print("<", end="")
print(', '.join(map(str, result)), end="")
print(">") 