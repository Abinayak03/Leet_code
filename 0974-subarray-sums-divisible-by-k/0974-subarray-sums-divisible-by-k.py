class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq = {0:1}
        count = 0
        prefix_sum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum%k in freq:
                count+= freq[prefix_sum%k]
            freq[prefix_sum%k] = freq.get(prefix_sum%k, 0)+1
        return count