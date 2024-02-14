from typing import List

class Solution:
    def first_palindrome(self, words: List[str]) -> str:
        for s in words:
            start, end = 0, len(s)-1
            while start <= end:
                if s[start] != s[end]:
                    break
                start += 1
                end -= 1
            if start > end:
                return s
        return ""
