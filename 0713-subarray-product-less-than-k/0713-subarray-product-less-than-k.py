class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1:
            return 0
        product = 1
        count = 0
        left = 0
        for r in range(len(nums)):
            product *= nums[r]
            while product>=k:
                product//=nums[left]
                left+=1
            count+= (r-left+1)
        return count