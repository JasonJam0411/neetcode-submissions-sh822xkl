class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 初始化左右指標
        left, right = 0, len(nums) - 1
        
        while left <= right:
            # 取得中間索引，使用 // 進行整數除法
            # (left + right) // 2 在極大值時可能會溢位，
            # 雖然 Python 會自動處理大數，但寫成 left + (right - left) // 2 是更專業的習慣
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid  # 找到了，回傳索引
            elif nums[mid] < target:
                left = mid + 1  # 目標在右半部，縮小左邊界
            else:
                right = mid - 1 # 目標在左半部，縮小右邊界
                
        return -1  # 遍歷完都沒找到，回傳 -1