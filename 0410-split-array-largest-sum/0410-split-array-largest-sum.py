class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        ans = high
        
        if k>len(nums):
            return -1
        
        while low <= high:
            mid = (low+high)//2
            if self.can_split(nums, k, mid):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans
        
    def can_split(self, nums, k, max_sum):
        page_sum = 0
        subarray = 1
        for pages in nums:
            if page_sum + pages <= max_sum:
                page_sum += pages
            
            else:
                subarray += 1
                page_sum = pages
        return subarray<=k