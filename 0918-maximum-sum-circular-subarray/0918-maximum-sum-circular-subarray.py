class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_min, curr_max = 0, 0
        glob_min, glob_max = nums[0], nums[0]
        total = 0
        for i in range (len(nums)):
            total+=nums[i]

            curr_min = min(nums[i], curr_min+nums[i])
            glob_min = min(curr_min, glob_min)

            curr_max = max(nums[i], curr_max+nums[i])
            glob_max = max(curr_max, glob_max)
        return glob_max if glob_max<0 else max(glob_max, total - glob_min) 
