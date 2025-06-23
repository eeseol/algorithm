class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)
        # 초기화: 모든 위치에 1을 설정
        for i in range(1, n + 1):
            self.update(i, 1)
    
    def update(self, idx, val):
        while idx <= self.n:
            self.tree[idx] += val
            idx += idx & -idx
    
    def query(self, idx):
        result = 0
        while idx > 0:
            result += self.tree[idx]
            idx -= idx & -idx
        return result
    
    def find_kth(self, k):
        """k번째 1을 찾기"""
        left, right = 1, self.n
        while left < right:
            mid = (left + right) // 2
            if self.query(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left

def josephus_fenwick_tree(N, K):
    """
    이진 인덱스 트리를 사용한 요세푸스 문제 해결
    시간복잡도: O(N * log N)
    공간복잡도: O(N)
    """
    fenwick = FenwickTree(N)
    result = []
    remaining = N
    current = 0
    
    while remaining > 0:
        # 현재 위치에서 K번째 사람 찾기
        current = (current + K - 1) % remaining + 1
        
        # k번째 사람의 실제 위치 찾기
        pos = fenwick.find_kth(current)
        result.append(pos)
        
        # 해당 위치 제거
        fenwick.update(pos, -1)
        remaining -= 1
    
    return result

# 입력 받기
N, K = map(int, input().split())

# 결과 계산
result = josephus_fenwick_tree(N, K)

# 출력
print("<", end="")
print(', '.join(map(str, result)), end="")
print(">") 