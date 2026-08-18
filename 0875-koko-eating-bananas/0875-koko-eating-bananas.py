class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high
        while low<=high:
            mid = (low+high)//2
            if self.speed(piles, mid)<=h:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans


    def speed(self, piles, s):
        time = 0
        for pile in piles:
            time+= (pile+s-1)//s
        return time