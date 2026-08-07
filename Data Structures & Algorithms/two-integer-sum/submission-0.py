class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prehash = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prehash:
                return[prehash[diff],i]
            prehash[n] = i
        return 

        