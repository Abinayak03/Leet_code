class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        curr_min = curr_max = 0
        ans = nums[0]
        for i in range (len(nums)):
            temp = curr_min+nums[i]
            curr_min = min(nums[i], temp, curr_max+nums[i])
            curr_max = max(nums[i], curr_max+nums[i], temp)
            ans = max(ans, curr_max, abs(curr_min))
        return ans

        '''curr_min, curr_max = 0, 0
        glob_min, glob_max = nums[0], nums[0]

        for i in range (len(nums)):

            curr_min = min(nums[i], curr_min+nums[i])
            glob_min = min(curr_min, glob_min)

            curr_max = max(nums[i], curr_max+nums[i])
            glob_max = max(curr_max, glob_max)
        return max(glob_max, abs(glob_min))'''