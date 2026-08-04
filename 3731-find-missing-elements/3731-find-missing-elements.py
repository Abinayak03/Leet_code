class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        minimum = maximum = nums[0]
        for x in nums[1:]:
            if x < minimum:
                minimum = x
            elif x > maximum:
                maximum = x
        ans = []

        for i in range(minimum, maximum+1):
            if i not in nums:
                ans.append(i)
        return ans