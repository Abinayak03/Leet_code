class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x//2
        if x<2:
            return x
        while left<=right:
            mid = left + (right-left)//2
            square = mid*mid

            if square == x:
                return mid

            elif square < x:
                left = mid+1

            else:
                right = mid-1

        return right
