class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_min = curr_max = ans = nums[0]
        for i in range (1, len(nums)):
            temp = curr_min
            curr_min = min(nums[i], curr_min*nums[i], curr_max*nums[i])
            curr_max = max(nums[i], curr_max*nums[i], temp*nums[i])
            ans = max(ans, curr_max)
        return ans
        