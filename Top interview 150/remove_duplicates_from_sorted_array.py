"""
my solution for https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums[::] = list(sorted(set(nums)))

        return len(nums)


"""
the best solution
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # Edge case: if the list is empty, return 0
        if not nums:
            return 0

        # Initialize the first pointer `i`
        i = 0

        # Loop through the array starting from the second element
        for j in range(1, len(nums)):
            # If the current element is different from the last unique element
            if nums[j] != nums[i]:
                # Increment the first pointer and update its value
                i += 1
                nums[i] = nums[j]

        # Return the length of the array without duplicates
        return i + 1
