class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prehas = set()
        for i in nums:
            if i in prehas:
                return True
            prehas.add(i)
        return False