"""
my solution for https://leetcode.com/problems/merge-sorted-array/
"""


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[::]

        """ 
        
        this is because we need to modify nums1 in-place
        if we do something like nums1 = sorted(nums1) it will not work
        because it will create a new list and not modify nums1
        
        """
        nums1[::] = sorted(nums1)


"""
the best solution
"""


class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # Initialize two pointers for nums1 and nums2
        p1, p2 = m - 1, n - 1
        # Pointer for the last position in nums1
        p = m + n - 1

        # Traverse from the end and compare elements from both arrays
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If there are still elements in nums2, add them to nums1
        # (This happens when nums1's elements are smaller than nums2's)
        nums1[: p2 + 1] = nums2[: p2 + 1]
