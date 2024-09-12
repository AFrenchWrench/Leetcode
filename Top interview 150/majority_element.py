"""
mt solution for https://leetcode.com/problems/majority-element/
"""


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        nums_set = set(nums)
        counts = {}
        for num in nums_set:
            counts[nums.count(num)] = num

        return counts[max(counts.keys())]


"""
best solution
"""


class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Initialize candidate and count
        candidate = None
        count = 0

        # Phase 1: Find the majority candidate
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1

        # Since the problem guarantees the majority element exists,
        # we can directly return the candidate found.
        return candidate
