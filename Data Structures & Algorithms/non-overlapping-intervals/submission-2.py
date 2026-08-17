class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        res = 0
        print(intervals)

        for i in range(1,len(intervals)):
            if intervals[i][0] < intervals[i - 1][1]:
                res += 1
                intervals[i][0] = intervals[i - 1][0]
                intervals[i][1] = intervals[i - 1][1]
        return res