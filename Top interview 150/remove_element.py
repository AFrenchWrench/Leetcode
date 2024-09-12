"""
my solution for https://leetcode.com/problems/remove-element/
"""


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        l1 = len(nums)
        l2 = nums.count(val)

        for i in range(l2):
            nums.remove(val)

        return l1 - l2


"""
the best solution
"""


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        # Initialize a pointer for the next position of non-val element
        insert_pos = 0

        # Iterate through the list
        for num in nums:
            # If the current element is not equal to val, we keep it
            if num != val:
                nums[insert_pos] = num
                insert_pos += 1

        # Return the length of the modified array
        return insert_pos
