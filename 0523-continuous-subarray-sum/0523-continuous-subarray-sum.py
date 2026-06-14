class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        first = {0: -1}
        prefix = 0

        for i, num in enumerate(nums):
            prefix += num
            rem = prefix % k

            if rem in first:
                if i - first[rem] >= 2:
                    return True
            else:
                first[rem] = i

        return False

        '''for i in range(len(nums)-1):
            sum = nums[i]
            for j in range(i+1, len(nums)):
                sum += nums[j]

                if sum % k == 0:
                    return True
                    break

        return False'''