class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        check = {}
        for i in range(n):
            rem = target - nums[i]
            if rem in check:
                return [i, check[rem]]
            check[nums[i]] = i
        
        '''for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return([i,j])'''