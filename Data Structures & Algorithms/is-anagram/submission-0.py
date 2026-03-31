class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_chars = defaultdict(int)
        t_chars = defaultdict(int)
        for i in range(len(s)):
            s_chars[s[i]] += 1
            t_chars[t[i]] += 1
        
        for key, val in s_chars.items():
            if key not in t_chars:
                return False
            if s_chars[key] != t_chars[key]:
                return False
        
        return True
            