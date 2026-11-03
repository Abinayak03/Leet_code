class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_num = max(nums)
        count = 0
        for num in nums:
            count+=(max_num-num)
        return count