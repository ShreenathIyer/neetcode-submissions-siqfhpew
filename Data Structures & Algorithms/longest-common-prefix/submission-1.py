class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root = Node("")
        minLen = float("inf")
        for word in strs:
            curr = root
            minLen = min(minLen, len(word))
            for c in word:
                if c not in curr.children:
                    curr.children[c] = Node(c)
                curr = curr.children[c]
        res = ""
        curr = root
        currLen = 0
        while len(curr.children) == 1 and currLen < minLen:
            for key, val in curr.children.items():
                nextkey = key
            res = res + nextkey
            currLen += 1
            curr = curr.children[nextkey]

        return res


class Node:
    def __init__(self, val):
        self.children = dict() # char -> [children]
        self.val = val