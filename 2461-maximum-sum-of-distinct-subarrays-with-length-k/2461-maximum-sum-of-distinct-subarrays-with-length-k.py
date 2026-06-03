class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        left = 0
        freq = defaultdict(int)
        max_sum = 0
        count = 0

        for right in range(len(nums)):
            freq[nums[right]] += 1
            count += nums[right]

            if right-left+1 == k:
                if len(freq) == k:
                    max_sum = max(max_sum, count)
                count -= nums[left]
                freq[nums[left]]-=1
                if freq[nums[left]]==0:
                    del freq[nums[left]]
                left+=1
                
        return max_sum
        