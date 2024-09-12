"""
my solution for https://leetcode.com/problems/rotate-array/
"""


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp_nums = nums[::]
        l = len(nums)
        for i in range(l):
            temp_nums[(i + k) % l] = nums[i]

        nums[::] = temp_nums

"""
best solution
"""


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # In case k is greater than the length of the array

        # Step 1: Reverse the entire array
        self.reverse(nums, 0, n - 1)

        # Step 2: Reverse the first k elements
        self.reverse(nums, 0, k - 1)

        # Step 3: Reverse the remaining elements from k to the end
        self.reverse(nums, k, n - 1)

    def reverse(self, nums: list[int], start: int, end: int) -> None:
        """Helper function to reverse elements in the array between start and end indices."""
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
