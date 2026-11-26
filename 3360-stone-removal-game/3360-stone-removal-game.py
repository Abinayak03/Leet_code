class Solution:
    def canAliceWin(self, n: int) -> bool:
        turn = 10
        flag = True

        while n>=turn:
            n-=turn
            turn-=1
            flag = not flag
        return not flag