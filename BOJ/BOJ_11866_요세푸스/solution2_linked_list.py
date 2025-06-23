class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def josephus_linked_list(N, K):
    """
    연결 리스트를 사용한 요세푸스 문제 해결
    시간복잡도: O(N*K)
    공간복잡도: O(N)
    """
    if N == 1:
        return [1]
    
    # 원형 연결 리스트 생성
    head = Node(1)
    current = head
    for i in range(2, N + 1):
        current.next = Node(i)
        current = current.next
    current.next = head  # 원형으로 만들기
    
    result = []
    current = head
    
    while N > 0:
        # K-1번 이동
        for _ in range(K - 2):
            current = current.next
        
        # K번째 노드 제거
        if current.next == current:  # 마지막 하나 남은 경우
            result.append(current.data)
            break
        else:
            result.append(current.next.data)
            current.next = current.next.next
            current = current.next
            N -= 1
    
    return result

# 입력 받기
N, K = map(int, input().split())

# 결과 계산
result = josephus_linked_list(N, K)

# 출력
print("<", end="")
print(', '.join(map(str, result)), end="")
print(">") 