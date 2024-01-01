class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(k, n, m):
            if n < k or n > k * 9 or n > 45:
                return []
            if k == 1 and n >= m:
                return [[n]]
            res = []
            for i in range(m, 10):
                for ans in dfs(k - 1, n - i, i + 1):
                    res.append([i] + ans)
            return res
        return dfs(k, n, 1)
