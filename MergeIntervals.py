# 56. Merge Intervals

# Google Tag

'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
'''

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
 
    ############################################################################################################
    # Use flag and sort all together.

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        l = len(intervals)
        if l <= 1:
            return intervals

        s = []

        for i in intervals:
            s.append((i.start, 1))
            s.append((i.end, -1))

        s.sort(key=lambda x: (x[0], -1 * x[1]))

        res = []
        flag = 0
        start = float('-inf')
        for i in s:
            if start == float('-inf'):
                start = i[0]
                flag = 1
            else:
                flag += i[1]
                if flag == 0:
                    res.append([start, i[0]])
                    start = float('-inf')

        return res

    #############################################################################################################
    # Sort start, extend end if next interval has overlap with the last interval in result.

    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0: return []
        
        intervals = sorted(intervals, key = lambda x: x.start)
        
        res = [intervals[0]]
        for n in intervals[1:]:
            if n.start <= res[-1].end: res[-1].end = max(n.end, res[-1].end)
            else: res.append(n)
                
        return res        
