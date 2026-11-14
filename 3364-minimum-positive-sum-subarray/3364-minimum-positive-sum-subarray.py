class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = inf

        for i in range(len(nums)):
            sum = 0
            for j in range(i, len(nums)):
                sum+=nums[j]
                if sum>0 and (l<= j-i+1 <= r):
                    min_sum = min(min_sum, sum)
        return -1 if min_sum==inf else min_sum