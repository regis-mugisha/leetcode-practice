from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for item in nums:
            if item in seen:
                return True
            else:
                seen.add(item)

        return False