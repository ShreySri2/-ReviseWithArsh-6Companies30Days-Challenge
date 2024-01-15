class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        l, r = 0, 0
        res = set()

        while l < len(nums):
            count = 0
            for r in range(l,len(nums)):
                if nums[r] % p == 0:
                    count += 1

                if count > k:
                    break
                else:
                    res.add(tuple(nums[l:r + 1]))
                    

            l += 1

        return len(res)

