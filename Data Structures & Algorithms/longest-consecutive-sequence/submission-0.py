class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        nums_set = set(nums)
        ans = 0

        for num in nums:
            if num-1  not in nums_set:
                current_cnt = 1
                current_num = num
                while current_num+1 in nums_set:
                    current_cnt+=1
                    current_num+=1
                
                ans = max(ans, current_cnt)
        
        return ans