class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            if i==0:
                result.append(1)
            else:
                result.append(nums[i-1]*result[i-1])
        right_prod = 1
        for j in range(len(nums)-1, -1, -1):
            result[j]*=right_prod
            right_prod *= nums[j]
        return result