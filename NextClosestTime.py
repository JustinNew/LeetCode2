# 681. Next Closest Time

# Google Tag

'''
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.
Example 2:

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may be assumed that the returned time is next day's time since it is smaller than the input time numerically.
'''

class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
       
        import re
        digits = re.findall(r'[0-9]', time)
        digits = set(digits)

        m = re.search(r'(\d\d):(\d\d)', time)
        hour = int(m.group(1))
        min = int(m.group(2))

        while 1:

            min += 1

            if min == 60:
                min = 0
                hour += 1
                if hour == 24:
                    hour = 0

            if min < 10 or hour < 10:
                t = set('0' + str(min) + str(hour))
            else:
                t = set(str(min) + str(hour))

            
            if len([i for i in t if i in digits]) == len(t):
                min = '0' + str(min) if min < 10 else str(min)
                hour = '0' + str(hour) if hour < 10 else str(hour)
                return hour + ':' + min 
