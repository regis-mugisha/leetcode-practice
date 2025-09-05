from typing import List


# my solution - brute force
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if(len(nums) < 2):
            return []
        res = []
        for i,curr in enumerate(nums):
            product= 1
            elements_before = nums[:i]
            elements_after= nums[i+1:]

            other_elements = elements_before + elements_after

            for element in other_elements:
                product *=element
            res.append(product)
            
        return res
