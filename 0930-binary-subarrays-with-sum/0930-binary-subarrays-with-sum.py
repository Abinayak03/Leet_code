class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        count = 0
        total = 0
        l = 0
        zeros = 0
        n = len(nums)

        for r in range(n):
            if nums[r] == 1:
                total+=1
            while l<r and total>goal:
                if nums[l] == 1:
                    total-=1
                l+=1
                zeros = 0
            while l<r and nums[l]==0 and total == goal:
                zeros+=1
                l+=1
            if total == goal:
                count+=1+zeros
        return count