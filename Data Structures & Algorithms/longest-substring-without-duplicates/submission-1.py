class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        visited = set()
        left = 0
        for right in range(len(s)):
            while len(visited) > 0 and s[right] in visited:
                visited.remove(s[left])
                left += 1
            visited.add(s[right])
            res = max(res, right - left + 1)
        return res