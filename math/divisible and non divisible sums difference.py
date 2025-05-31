"""
My solution for https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/submissions/1649921789/
"""


# Default programmer way
class Solution:
    def differenceOfSums(self, n, m):
        not_divisible_sum = 0
        divisible_sum = 0

        for i in range(1, n + 1):
            if i % m == 0:
                divisible_sum += i
            else:
                not_divisible_sum += i

        return not_divisible_sum - divisible_sum


# A bit of math involved way
class Solution:
    def differenceOfSums(self, n, m):
        totalSum = n * (n + 1) // 2
        divisibleSum = m * (n // m) * (n // m + 1)
        return totalSum - divisibleSum
