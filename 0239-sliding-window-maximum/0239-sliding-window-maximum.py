class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        result = []
        dq = deque()

        for right in range(len(nums)):
            while dq and dq[0]==right-k:
                dq.popleft()

            while dq and nums[dq[-1]] <= nums[right]:
                dq.pop()
            dq.append(right)

            if right+1>=k:
                result.append(nums[dq[0]])
        return result