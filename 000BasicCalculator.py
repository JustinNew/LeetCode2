# 224. Basic Calculator

# Google Tag

'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:

Input: "1 + 1"
Output: 2
Example 2:

Input: " 2-1 + 2 "
Output: 3
Example 3:

Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23
Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
'''

# Always valid, then the '()' does not matter.

class Solution:
    def calculate(self, s):
        """
        :type s: str
        :rtype: int

        import re

        s = re.findall(r'[0-9\+\-\(\)]', s)
        s = ''.join(s)

        start = 0
        i = 0
        expr = []
        while i < len(s):
            if s[i] in ['+', '-', '(', ')']:
                if start != i:
                    expr.append(int(s[start:i]))
                expr.append(s[i])
                start = i + 1
            i += 1
        if start != len(s):
            expr.append(int(s[start:]))

        def util(arr):

            res = arr[-1]
            for i in range(len(arr) - 2, 0, -2):
                e, v = arr[i], arr[i - 1]
                if e == '+':
                    res += v
                elif e == '-':
                    res -= v
            return res

        s = []
        for i in expr:
            if i != ')':
                s.append(i)
            else:
                temp = []
                while s[-1] != '(':
                    temp.append(s.pop())
                s.pop()
                s.append(util(temp))
        
        if len(s) != 1:
            s = s[::-1]
            return util(s)
        else:
            return s[0]

'''
Keep a global running total and a stack of signs (+1 or -1), one for each open scope. The "global" outermost sign is +1.

Each number consumes a sign.
Each + and - causes a new sign.
Each ( duplicates the current sign so it can be used for the first term inside the new scope. That's also why I start with [1, 1] - the global sign 1 and a duplicate to be used for the first term, since expressions start like 3... or (..., not like +3... or +(....
Each ) closes the current scope and thus drops the current sign.
Also see the example trace below my programs.

https://leetcode.com/problems/basic-calculator/discuss/62344/Easy-18-lines-C++-16-lines-Python
'''

def calculate(self, s):
    total = 0
    i, signs = 0, [1, 1]
    while i < len(s):
        c = s[i]
        if c.isdigit():
            start = i
            while i < len(s) and s[i].isdigit():
                i += 1
            total += signs.pop() * int(s[start:i])
            continue
        if c in '+-(':
            signs += signs[-1] * (1, -1)[c == '-'],
        elif c == ')':
            signs.pop()
        i += 1
    return total
