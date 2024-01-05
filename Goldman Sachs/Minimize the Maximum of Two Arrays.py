class Solution:
    def minimizeSet(self, divisor1: int, divisor2: int, uniqueCnt1: int, uniqueCnt2: int) -> int:
        def relu(x):
            if x>0:
                return x
            else:
                return 0 
        n = uniqueCnt1+uniqueCnt2
        n_0 = 0
        divisor = lcm(divisor1,divisor2)
        while n>n_0:
            n_0 = n
            g1_len, g2_len = n//divisor2-n//divisor, n//divisor1-n//divisor
            n+= relu(uniqueCnt1-g1_len) + relu(uniqueCnt2-g2_len) - n + n//divisor + g1_len+g2_len
        return n