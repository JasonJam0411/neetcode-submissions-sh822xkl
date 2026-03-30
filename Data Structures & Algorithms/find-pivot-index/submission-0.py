class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # 1 8 11 17 23 29
        # 28 27 20 17 11 6
        # 2 3 2
        # 2 0 -1
        
        a = []
        b = []
        i = 0
        j = 0

        for num in nums:
            a.append(i+num)
            i+=num
        
        for k in range(len(nums)-1, -1,-1):
            b.append(j+nums[k])
            j+=nums[k]
        b.reverse()
        for l in range(len(a)):
            if a[l]==b[l] :
                return l
        
        return -1