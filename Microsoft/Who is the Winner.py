class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque()
        for x in range(1,n+1):
            queue.append(x)
        
        for _ in range(n-1):
            c = k-1
            for __ in range(c):
                a = queue.popleft()
                queue.append(a)
            queue.popleft()
        return queue[0]

