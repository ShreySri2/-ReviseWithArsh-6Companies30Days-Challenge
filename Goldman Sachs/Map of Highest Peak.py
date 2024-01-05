class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        arr = deque()
        m, n = len(isWater), len(isWater[0])

        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    isWater[i][j] = 0
                    arr.append((0, i, j))
                else:
                    isWater[i][j] = -1

        while arr:
            val, x, y = arr.popleft()

            for i, j in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                if 0 <= x + i < m and 0 <= y + j < n and isWater[x+i][y+j] == -1:
                    isWater[x+i][y+j] = val + 1
                    arr.append((val + 1, x + i, y + j))

        return isWater
