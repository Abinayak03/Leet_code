class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if not nums:
            return nums
        
        min_val, max_val = min(nums), max(nums)
        count = [0] * (max_val - min_val + 1)
        
        for num in nums:
            count[num - min_val] += 1
        
        index = 0
        for i in range(len(count)):
            while count[i] > 0:
                nums[index] = i + min_val
                index += 1
                count[i] -= 1
        
        return nums
        
        '''self.quick_sort(nums, 0, len(nums)-1)
        return nums

    def quick_sort(self, nums, low, high):
        if low < high:
            p_index = self.partition(nums, low, high)
            self.quick_sort(nums, low, p_index-1)
            self.quick_sort(nums, p_index+1, high)

    def partition(self, nums, low, high):
        mid = (high - low) // 2 + low
        nums[low], nums[mid] = nums[mid], nums[low]
        pivot = nums[low]
        i = low
        j = high
        while i<j:
            while nums[i]<=pivot and i<=high-1:
                i+=1
            while nums[j]>pivot and j>=low+1:
                j-=1
            if i<j:
                nums[i], nums[j]  = nums[j], nums[i]

        nums[low], nums[j] = nums[j], nums[low]
        return j'''