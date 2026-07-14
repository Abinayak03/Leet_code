class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [self.searchFirst(nums, target), self.searchLast(nums, target)]

    def searchFirst(self, nums, target):
        ans = -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid]<target:
                left = mid+1
            elif nums[mid] == target:
                ans = mid
                right = mid-1
            else:
                right = mid-1
        return ans

    def searchLast(self, nums, target):
        ans = -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right-left)//2
            if nums[mid]<target:
                left = mid+1
            elif nums[mid] == target:
                ans = mid
                left = mid+1
            else:
                right = mid-1
        return ans