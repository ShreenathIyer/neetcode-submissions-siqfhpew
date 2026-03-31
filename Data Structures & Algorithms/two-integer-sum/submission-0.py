class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counts = dict()
        for i, num in enumerate(nums):
            req = target - num
            if req in counts:
                return [counts[req], i]
            counts[num] = i
        