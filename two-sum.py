from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i, num in enumerate(nums):
            difference = target - nums[i]
            if difference in indices:
                return [indices[difference], i]
            indices[num] = i
        
        return []