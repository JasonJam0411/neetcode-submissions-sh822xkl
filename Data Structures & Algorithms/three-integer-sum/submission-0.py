class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)
        for i in range(len(nums)):
            
            if nums[i] > 0:
                break
            
            if i>0 and nums[i-1] == nums[i]:
                continue
            
            j = i+1
            k = len(nums)-1
            while j<k:
                cur_sum  = nums[i]+nums[j]+nums[k]
                
                if cur_sum > 0:
                    k-=1
                elif cur_sum < 0:
                    j+=1
                else:
                    ans.append([nums[i],nums[j],nums[k]])

                    while j<k and nums[j+1] == nums[j]:
                        j+=1
                    while j<k and nums[k-1] == nums[k]:
                        k-=1
                    
                    j+=1
                    k-=1
        
        return ans