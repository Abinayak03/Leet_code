class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_min, curr_max = nums[0], nums[0]
        ans = nums[0]
        for i in range (1, len(nums)):
            temp = curr_min
            curr_min = min(nums[i], curr_min*nums[i], curr_max*nums[i])

            curr_max = max(nums[i], curr_max*nums[i], temp*nums[i])
            ans = max(ans, curr_max)
        return ans
        '''prefix = 1
        suffix = 1
        ans = -float('inf')

        for i in range(len(nums)):
            prefix *= nums[i]
            suffix *= nums[len(nums)-i-1]
            ans = max(ans, prefix, suffix)
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
        return ans'''