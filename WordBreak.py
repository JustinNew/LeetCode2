# 139. Word Break

# Google Tag

'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
'''

# 1-D DP

class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """

        if s in wordDict:
            return True

        dp = [0 for i in range(len(s))]

        for i in range(len(s)):
            flag = 0
            
            if s[:i + 1] in wordDict:
                dp[i] = 1
                flag = 1
                
            if flag == 0:
                for j in range(i):
                    if s[i - j: i + 1] in wordDict and dp[i - j - 1] == 1:
                        dp[i] = 1
                        break

        return True if dp[-1] == 1 else False
