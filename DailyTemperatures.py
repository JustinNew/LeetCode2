# 739. Daily Temperatures

# Google Tag

'''
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
'''

'''
Use a stack
From the end to beginning
Keep a decreasing stack
For each new element, pop out elements in stack that are not larger than itself.
1. 73, []
2. 76, [76]
3. 72, [76, 72]
4. 69, [76, 72, 69]
5. 71, [76, 72, 71]
6. ...
'''

class Solution:
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """

        if len(T) == 0:
            return []

        T.reverse()
        s = []
        res = []
        for i in range(len(T)):
            while len(s) != 0 and s[-1][0] <= T[i]:
                s.pop()

            if len(s) == 0:
                res.append(0)
            else:
                t, n = s[-1]
                res.append(i - n)

            s.append([T[i], i])

        return res[::-1]
