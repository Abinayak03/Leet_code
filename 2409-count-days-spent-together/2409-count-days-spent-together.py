class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        dates = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        start = max(arriveAlice, arriveBob)
        end = min(leaveAlice, leaveBob)
        if start>end:
            return 0
        
        def count_days(date):
            month, day = map(int, date.split("-"))
            return sum(dates[:month-1])+day
        return count_days(end)-count_days(start)+1