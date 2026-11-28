class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        subsets = 1<<n
        ans = []

        for s in range(subsets):
            list_ = []
            for i in range(n):
                if s & (1<<i):
                    list_.append(nums[i])
            ans.append(list_)
        return ans