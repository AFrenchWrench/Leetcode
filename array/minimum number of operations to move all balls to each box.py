"""
My solution for https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
"""

from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        idxes = []
        n = len(boxes)
        for idx, box in enumerate(boxes):
            if box == "1":
                idxes.append(idx)

        ans = [sum(idxes)]
        ones_count = len(idxes)
        r = ones_count
        l = 0
        if boxes[0] == "1":
            r -= 1
            l += 1

        for i in range(1, n):
            ans.append(ans[-1] - r + l)
            if boxes[i] == "1":
                r -= 1
                l += 1

        return ans
