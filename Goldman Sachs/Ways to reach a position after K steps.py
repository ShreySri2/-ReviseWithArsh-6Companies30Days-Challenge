class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        startPos, endPos = 0, abs(endPos-startPos)
        MOD = 10**9+7
        cache = {}
        def dfs(start,step):
            if start == endPos and step==0:
                return 1
            if step==0:
                return 0 
            if (start,step) in cache:
                return cache[(start,step)]
            
            res = dfs(start+1,step-1)+dfs(start-1,step-1)
            cache[(start,step)] = res
            return res
        
        
        return dfs(0,k)%MOD
     
            
        