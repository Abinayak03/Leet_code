class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_len = 0
        increasing = 1
        for n in range(1, len(nums)):
            if nums[n] > nums[n-1]:
                increasing+=1
            else:
                max_len = max(max_len, increasing)
                increasing = 1
        max_len = max(max_len, increasing)

        decreasing = 1
        for n in range(1, len(nums)):
            if nums[n] < nums[n-1]:
                decreasing+=1
            else:
                max_len = max(max_len, decreasing)
                decreasing = 1
        max_len = max(max_len, decreasing)
        return max_len