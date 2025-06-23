def josephus_array(N, K):
    """
    배열을 사용한 요세푸스 문제 해결
    시간복잡도: O(N*K)
    공간복잡도: O(N)
    """
    people = list(range(1, N + 1))
    result = []
    current = 0
    
    while people:
        # K번째 사람 찾기 (현재 위치에서 K-1번 이동)
        current = (current + K - 1) % len(people)
        result.append(people.pop(current))
    
    return result

# 입력 받기
N, K = map(int, input().split())

# 결과 계산
result = josephus_array(N, K)

# 출력
print("<", end="")
print(', '.join(map(str, result)), end="")
print(">") 