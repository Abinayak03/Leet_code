class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = {}
        for i in range(n):
            freq[nums[i]] = freq.get(nums[i], 0) + 1
        
        if n==k:
            return max(nums)
        if k==1:    
            max_ans = -1
            for i in range(n):
                if freq[nums[i]] ==1 and nums[i]>max_ans:
                    max_ans = nums[i]
            return max_ans

        if nums[0] == nums[n-1]:
            return -1

        if freq[nums[0]] == 1 and freq[nums[n-1]] == 1:
            return max(nums[0], nums[n-1])

        if freq[nums[0]] == 1 and freq[nums[n-1]] > 1:
            return nums[0]

        if freq[nums[n-1]] == 1 and freq[nums[0]] > 1:
            return nums[n-1]

        return -1