"""
my solution for https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        for num in nums:
            reps = nums.count(num)
            if reps > 2:
                for _ in range(reps - 2):
                    nums.remove(num)

        return len(nums)


"""
best solution
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # If there are 2 or fewer elements, no need to process further
        if len(nums) <= 2:
            return len(nums)

        # Pointer `i` starts from the 2nd element (index 1)
        i = 2

        # Loop through the array starting from the 3rd element (index 2)
        for j in range(2, len(nums)):
            # If the current element is different from the element at `i-2`, it can stay
            if nums[j] != nums[i - 2]:
                nums[i] = nums[j]
                i += 1

        # Return the new length of the modified array
        return i
