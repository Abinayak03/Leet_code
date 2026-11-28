class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        '''XOR = 0
        for n in nums:
            XOR = XOR ^ n
        return XOR'''
        store = {}
        for num in nums:
            store[num] = 1 + store.get(num, 0)
        for key, value in store.items():
            if value==1:
                return key