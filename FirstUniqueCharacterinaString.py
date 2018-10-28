# 387. First Unique Character in a String

# Google Tag

'''
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''

# Be careful about edge cases.

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        d = {}
        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0) + 1

        for i in range(len(s)):
            if d[s[i]] == 1:
                return i
            
        return -1
