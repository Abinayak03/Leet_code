class Solution:
    def findGCD(self, nums: List[int]) -> int:
        max_ = max(nums)
        min_ = min(nums)
        return math.gcd(max_, min_)