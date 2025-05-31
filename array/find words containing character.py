"""
My solution for https://leetcode.com/problems/find-words-containing-character/
"""


class Solution:
    def findWordsContaining(self, words: list[str], x: str) -> list[int]:
        return [i for i, e in enumerate(words) if x in e]
