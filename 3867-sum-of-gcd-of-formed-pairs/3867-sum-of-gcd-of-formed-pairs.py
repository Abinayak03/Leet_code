class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        max_i = 0
        prefix_GCD = []

        for i in range(len(nums)):
            max_i = max(max_i, nums[i])
            prefix_GCD.append(math.gcd(nums[i], max_i))

        left = 0
        right = len(prefix_GCD)-1
        sum_ = 0
        prefix_GCD.sort()
        while left< right:
            sum_ += math.gcd(prefix_GCD[left], prefix_GCD[right])
            left+=1
            right-=1
        return sum_
