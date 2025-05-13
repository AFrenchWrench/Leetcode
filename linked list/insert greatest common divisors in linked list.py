"""
My solution for https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/submissions/1632715648/
"""

from math import gcd


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: ListNode) -> ListNode:
        curr = head
        while curr and curr.next:
            g = gcd(curr.val, curr.next.val)
            curr.next = ListNode(g, curr.next)
            curr = curr.next.next
        return head
