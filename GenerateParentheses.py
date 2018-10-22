# 22. Generate Parentheses

# Google Tag

'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

'''
1. left == n and right == left, get one solution
2. left == n
3. left < n
   a. left == 0 or right == left
   b. right < left
'''

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def util(left, right, temp):

            if left == n:
                if right == left:
                    res.append(temp)
                else:
                    util(left, right + 1, temp + ')')
            else:
                if left == 0 or right == left:
                    util(left + 1, right, temp + '(')
                else:
                    util(left + 1, right, temp + '(')
                    util(left, right + 1, temp + ')')
            return         

        temp = ''
        res = []
        util(0, 0, temp)

        return res

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        left = ['(' for i in range(n)]
        right = []

        res = []

        def util(l, r, temp):

            if len(l) == 0 and len(r) == 0:
                res.append(temp)
            elif len(l) == 0:
                util(l, r[:-1], temp + ')')
            else:
                if len(r) == 0:
                    util(l[:-1], r + [')'], temp + '(')
                else:
                    util(l[:-1], r + [')'], temp + '(')
                    util(l, r[:-1], temp + ')')
            return

        util(left, right, '')
        return res
