class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        return self.atmost(nums,k)-self.atmost(nums,k-1)

    def atmost(self,nums, k):
        k_sub = defaultdict(int)
        output = 0
        left = 0

        for right in range(len(nums)):
            k_sub[nums[right]]+=1

            while len(k_sub)>k:
                k_sub[nums[left]] -= 1

                if k_sub[nums[left]] == 0:
                    del k_sub[nums[left]]

                left+=1
            output += (right-left+1)
        return output