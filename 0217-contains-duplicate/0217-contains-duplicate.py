class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        lst=nums
        sets = set(nums)
        if len(sets) == len(lst):
            return False
        else:
            return True