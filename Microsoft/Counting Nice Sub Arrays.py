class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_sum = [0] * (len(nums) + 1)
        odd_count = 0
        res = 0
        for num in nums:
            prefix_sum[odd_count] += 1
            if num % 2 == 1:
                odd_count += 1
            if odd_count >= k:
                res += prefix_sum[odd_count - k]
        return res
