class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        XOR = 0
        for n in nums:
            XOR = XOR ^ n
        return XOR