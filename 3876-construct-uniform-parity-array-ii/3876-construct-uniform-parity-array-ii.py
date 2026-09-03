class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        nums_even = []
        nums_odd = []
        n = len(nums1)

        for i in range(n):
            if nums1[i] % 2 == 0:
                nums_even.append(i)
            else:
                nums_odd.append(i)
        if len(nums_even) == n or len(nums_odd) == n:
            return True
        elif min(nums1) % 2 !=0:
            return True
        else: 
            return False