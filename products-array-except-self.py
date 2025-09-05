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


# optimized solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [0]*n
        suff = [0]*n
        res = [0]*n

        pref[0] = 1
        suff[n-1] = 1

        for i in range(1,n):
            pref[i] = pref[i-1]*nums[i-1]

        for i in range(n-2, -1, -1):
            suff[i] = suff[i+1] * nums[i+1]

        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res