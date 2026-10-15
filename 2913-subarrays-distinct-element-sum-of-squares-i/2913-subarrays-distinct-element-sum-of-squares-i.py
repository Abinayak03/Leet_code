class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        squares = 0
        for i in range(n):
            my_set = set()
            for j in range(i, n):
                my_set.add(nums[j])
                squares+=len(my_set)**2
        return squares