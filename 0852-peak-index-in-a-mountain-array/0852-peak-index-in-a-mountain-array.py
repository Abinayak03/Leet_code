class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        n = len(arr)
        if n==1:
            return 0
        if arr[0]>arr[1]:
            return 0
        if arr[n-1]>arr[n-2]:
            return n-1
        left = 1
        right = n-2
        while left<=right:
            mid = (left+right)//2
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid] < arr[mid+1]:
                left = mid+1
            else: right = mid-1
        return 0