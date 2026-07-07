class Solution:
    def findMin(self, nums: List[int]) -> int:
        ans = inf
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid] >= nums[left]:
                ans = min(ans, nums[left])
                left = mid+1
            else:
                ans = min(ans, nums[mid])
                right = mid-1
        return ans