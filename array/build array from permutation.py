"""
My solution for https://leetcode.com/problems/build-array-from-permutation/
"""

from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        arr_len = len(nums)
        ans = [""] * arr_len
        for i in range(arr_len):
            ans[i] = nums[nums[i]]
        return ans
