class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        current = 0
        ans = float('inf')
        count = 0
        left = 0
        for r in range(len(nums)):
            count += 1
            current += nums[r]

            while current >= target:
                ans = min(count, ans)
                current -= nums[left]
                count-=1
                left+=1

        return 0 if ans == float('inf') else ans