#User function Template for python3
class Solution:
    def printMinNumberForPattern(ob,S):
        
        # code here 
        result = []
        stack = []
    
        num = 1      

        for char in S:
            stack.append(str(num))
            num += 1

            if char == "I":
                result += stack[::-1]
                stack = []
        stack.append(str(num))
        result += stack[::-1]
        return int(''.join(result))
        
    

