class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        area = float("-inf")
        while left < right:
            # area = dist between 2 points * min(height1, height2)
            curr = abs(right - left) * min(heights[left], heights[right])
            area = max(curr, area) 
            if left < right:
                left += 1
            else:
                right -= 1
        return area