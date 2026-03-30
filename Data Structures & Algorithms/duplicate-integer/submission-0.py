class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = set()
        for num in nums:
            if num not in temp:
                temp.add(num)
            else:
                return True
        
        if len(temp) == len(nums):
            return False
        else:
            return True