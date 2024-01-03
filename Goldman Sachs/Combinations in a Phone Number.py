class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def dfs(i, subset):
            if i == len(digits):
                res.append(subset)
                return
            
            for c in digitToChar[digits[i]]:
                dfs(i+1, subset+c)
            
        if digits:
            dfs(0, '')
        return res
            