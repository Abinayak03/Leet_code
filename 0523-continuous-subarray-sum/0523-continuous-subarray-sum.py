class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        freq = {0:-1}
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum%k in freq and i-freq[prefix_sum%k] >=2:
                return True
            if prefix_sum % k not in freq:
                freq[prefix_sum % k] = i
        return False

        '''for i in range(len(nums)-1):
            sum = nums[i]
            for j in range(i+1, len(nums)):
                sum += nums[j]

                if sum % k == 0:
                    return True
                    break

        return False'''