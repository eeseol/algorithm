from collections import deque

def josephus_queue(N, K):
    """
    큐를 사용한 요세푸스 문제 해결
    시간복잡도: O(N*K)
    공간복잡도: O(N)
    """
    queue = deque(range(1, N + 1))
    result = []
    
    while queue:
        # K-1번 앞에서 빼서 뒤로 보내기
        for _ in range(K - 1):
            queue.append(queue.popleft())
        # K번째 사람 제거
        result.append(queue.popleft())
    
    return result

# 입력 받기
N, K = map(int, input().split())

# 결과 계산
result = josephus_queue(N, K)

# 출력
print("<", end="")
print(', '.join(map(str, result)), end="")
print(">") 