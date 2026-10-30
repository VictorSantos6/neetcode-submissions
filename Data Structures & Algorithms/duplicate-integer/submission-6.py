class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        duplicates = set()
        for i in range(len(nums)):
            if nums[i] in duplicates:
                return True
            else:
                duplicates.add(nums[i])

        return False
            
            
        