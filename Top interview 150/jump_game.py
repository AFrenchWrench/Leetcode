"""
my solution for https://leetcode.com/problems/jump-game/
"""


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        
        # there is no possible way that it can't reach the end if there are no zeros
        if 0 not in nums:
            return True
        
        
        # if there is only one element the start is the end
        if len(nums) == 1:
            return True

        can = False

        for i in range(len(nums)):
            n = nums[i]
            # we go through the list and check if we can reach the end
            # if we reach 0 we will check if we can jump over it with any number before it
            # if we can't find one it is impossible to reach the end
            if n == 0:
                for j in range((i - 1), -1, -1):
                    m = nums[j]
                    if (m + j) > i:
                        can = True
                        break
                    elif (m + j) == i and (len(nums) - 1) == i:
                        can = True
                        break
                    else:
                        can = False
                if can == False:
                    break
        return can
