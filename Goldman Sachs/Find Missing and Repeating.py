#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        summ = n*(n+1)//2
        seen = set()
        res = []
        for num in arr:
            if num in seen:
                res.append(num)
            else:
                summ-=num
                seen.add(num)
        res.append(summ)
        return res
            
