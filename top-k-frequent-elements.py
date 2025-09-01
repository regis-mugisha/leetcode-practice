from operator import itemgetter
from typing import List


# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         count = {}
#         for num in nums:
#             count[num] = count.get(num, 0) + 1

#         sorted_items = sorted(count.items(), key=itemgetter(1), reverse=True)
#         result = []

#         for i in range(k):
#             result.append(sorted_items[i][0])

#         return result


# optimized solution using bucket sort
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
