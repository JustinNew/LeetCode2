# 301. Remove Invalid Parentheses

# Facebook Tag

'''
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
'''

'''
# Forming valid parentheses bottom up.

1. Get the maximum total '()' pairs using stack, n
2. Get the total number of '(', n1
3. Get the total number of ')', n2
We can skip '(' is n1 > n, and the same if n2 > n we can skip ')'.
Change 'remove invalid parentheses' into 'Form parentheses' problem.
'''

class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        l = len(s)
        if l == 0:
            return ['']

        candidate = []
        pair = 0
        n1 = 0
        n2 = 0
        for i in s:
            if i == '(':
                n1 += 1
                candidate.append(i)
            elif i == ')':
                n2 += 1
                if len(candidate) != 0 and candidate[-1] == '(':
                    pair += 1
                    candidate.pop()

        def util(arr, toselect, t_n1, t_n2, cur_n1, cur_n2):
            if len(arr) == 0 and cur_n1 == cur_n2:
                res[toselect] = 1
                return
            elif len(arr) == 0:
                return

            i = arr[0]
            if i == '(':
                if t_n1 > pair:
                    # Skip this '('
                    util(arr[1:], toselect, t_n1 - 1, t_n2, cur_n1, cur_n2)

                # Adding this one.
                util(arr[1:], toselect + '(', t_n1, t_n2, cur_n1 + 1, cur_n2)
            elif i == ')':
                if t_n2 > pair:
                    # Skip this ')'
                    util(arr[1:], toselect, t_n1, t_n2 - 1, cur_n1, cur_n2)

                # Adding this one.                
                if cur_n2 < cur_n1:
                    util(arr[1:], toselect + ')', t_n1, t_n2, cur_n1, cur_n2 + 1)
            else:
                util(arr[1:], toselect + i, t_n1, t_n2, cur_n1, cur_n2)

            return

        res = {}
        util(s, '', n1, n2, 0, 0)

        return [i for i in res.keys()]
