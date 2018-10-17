# 20. Valid Parentheses

# Google Tag

'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
'''

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if len(s) == 0:
            return True

        pair = []
        for i in s:
            if i in ['(', '[', '{']:
                pair.append(i)
            else:
                if len(pair) == 0:
                    return False
                elif i == ')' and pair[-1] == '(':
                    pair.pop()
                elif i == ']' and pair[-1] == '[':
                    pair.pop()
                elif i == '}' and pair[-1] == '{':
                    pair.pop()
                else:
                    pair.append(i)

        if len(pair) == 0:
            return True
        else:
            return False
