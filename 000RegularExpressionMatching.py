# 10. Regular Expression Matching

# Google Tag

'''
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
'''

# Dynamic programming, 2-D table
'''
1, If p.charAt(j) == s.charAt(i) :  dp[i][j] = dp[i-1][j-1];
2, If p.charAt(j) == '.' : dp[i][j] = dp[i-1][j-1];
3, If p.charAt(j) == '*': 
   here are two sub conditions:
               1   if p.charAt(j-1) != s.charAt(i) : dp[i][j] = dp[i][j-2]  //in this case, a* only counts as empty
               2   if p.charAt(i-1) == s.charAt(i) or p.charAt(i-1) == '.':
                              dp[i][j] = dp[i-1][j]    //in this case, a* counts as multiple a 
                           or dp[i][j] = dp[i][j-1]   // in this case, a* counts as single a
                           or dp[i][j] = dp[i][j-2]   // in this case, a* counts as empty
'''
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        if '.' not in p and '*' not in p and len(s) != len(p):
            return False

        t = ''
        i = 0
        while i < len(p):
            if p[i] != '*':
                t += p[i]
                i += 1
            else:
                if i + 1 < len(p) and p[i + 1] == '*':
                    i += 1
                else:
                    t += p[i]
                    i += 1

        p = t
        dp = [[0 for i in range(len(s) + 1)] for j in range(len(p) + 1)]
        dp[0][0] = 1

        a_z = 'abcdefghijklmnopqrstuvwxyz'

        for j in range(1, len(p) + 1):
            if p[j - 1] in a_z:
                for i in range(len(s), 0, -1):
                    if s[i - 1] == p[j - 1] and dp[j - 1][i - 1] == 1:
                        dp[j][i] = 1
            elif p[j - 1] == '.':
                for i in range(len(s), 0, -1):
                    if dp[j - 1][i - 1] == 1:
                        dp[j][i] = 1
            else:
                # Zero of the previous one.
                for i in range(len(s) + 1):
                    if dp[j - 2][i] == 1:
                        dp[j][i] = 1
                        
                if p[j - 2] == '.':
                    flag = 0
                    for i in range(1, len(s) + 1):
                        if dp[j - 1][i] == 1:
                            flag = 1 
                            break
                    if flag == 1:
                        for l in range(i + 1, len(s) + 1):
                            dp[j][l] = 1
                elif p[j - 2] in a_z:
                    flag = 0
                    for i in range(1, len(s) + 1):
                        if dp[j - 1][i] == 1:
                            flag = 1
                            break
                    if flag == 1:
                        for l in range(i + 1, len(s) + 1):
                            if s[l - 1] == p[j - 2]:
                                dp[j][l] = 1
                            else:
                                break

        return True if dp[-1][-1] else False
