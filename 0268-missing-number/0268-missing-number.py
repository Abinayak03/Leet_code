class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sorted_list = sorted(nums)
        if sorted_list[0]!=0:
            return 0
        for i in range(0,len(sorted_list)-1):
            if sorted_list[i]!=sorted_list[i+1] - 1:
                return int(sorted_list[i]+1)

        return int(sorted_list[-1]+1)
            
