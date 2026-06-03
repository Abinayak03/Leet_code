class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        from collections import defaultdict
        
        if k > len(nums):
            return 0
        
        freq = defaultdict(int)
        current_sum = 0
        
        # Initialize first window
        for i in range(k):
            freq[nums[i]] += 1
            current_sum += nums[i]
        
        max_sum = current_sum if len(freq) == k else 0
        
        # Slide window
        for i in range(k, len(nums)):
            # Add new element
            freq[nums[i]] += 1
            current_sum += nums[i]
            
            # Remove old element
            freq[nums[i-k]] -= 1
            current_sum -= nums[i-k]
            if freq[nums[i-k]] == 0:
                del freq[nums[i-k]]
            
            # Update max if valid
            if len(freq) == k:
                max_sum = max(max_sum, current_sum)
        
        return max_sum