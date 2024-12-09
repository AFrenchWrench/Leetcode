# my solution for https://leetcode.com/problems/h-index/

class Solution:
    def hIndex(self, citations: list[int]) -> int:
        for i in range(len(citations), -1, -1):
            if sum(1 for citation in citations if citation >= i) >= i:
                return i


# most optimized solution

class Solution:
    def hIndex(self, citations: list[int]) -> int:
        # Sort citations in ascending order
        citations.sort()
        n = len(citations)

        # Use binary search to find the h-index
        left, right = 0, n
        while left < right:
            mid = (left + right) // 2
            # Check if n - mid papers have citations >= citations[mid]
            if citations[mid] >= n - mid:
                right = mid  # Move left to find a smaller valid h-index
            else:
                left = mid + 1

        # The h-index is the number of papers with citations >= citations[left]
        return n - left
