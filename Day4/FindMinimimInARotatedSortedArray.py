class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            # left side is unsorted
            if nums[mid] >= nums[high]:
                low = mid + 1
            else:
                high = mid
        
        return nums[mid]