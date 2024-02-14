from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [None for _ in range(n)]

        plus = 0
        minus = 1

        for x in nums:
            if x < 0:
                ans[minus] = x
                minus += 2
            else:
                ans[plus] = x
                plus += 2

        return ans
