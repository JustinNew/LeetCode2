# 140. Word Break II

# Google Tag

'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
'''

class Solution:
    # Memory Limit Exceeded 
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        l = len(s)

        dp = [[] for i in range(l)]

        for i in range(l):
            for j in range(i):
                if s[i - j:i + 1] in wordDict:
                    for l in dp[i - j - 1]:
                        dp[i].append(l + " " + s[i - j:i + 1])
            if s[:i + 1] in wordDict:
                dp[i].append(s[:i + 1])

        return dp[-1]

    '''
    # Recursive + Dictionary == Top Down DP
    wordBreak('catsanddog') =
    wordBreak('catsanddo') + inDict('g') 
    U wordBreak('catsandd') + inDict('og')
    U wordBreak('catsand') + inDict('dog')
    U ...
    U wordBreak('c') + inDict('atsanddog')
    U inDict('catsanddog')
    '''
    # Memory Limit Exceeded.
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """

        def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        d = {}
        for w in wordDict:
            d[w] = 1

        bk = {}
        bk[''] = []

        def util(ss):

            if len(ss) == 0:
                return
            elif ss in bk:
                return 
            else:
                bk[ss] = []
                for i in range(len(ss) - 1, -1, -1):
                    util(ss[:i])
                    if i == 0 and ss[i:] in d:
                        bk[ss].append(ss[i:])
                    elif len(bk[ss[:i]]) != 0 and ss[i:] in d:
                        for l in bk[ss[:i]]:
                            bk[ss].append(l + ' ' + ss[i:])
            return

        util(s)                           
        return bk[s]

    # Same as last one, improve by only use bk[] is ss[i:] is in d.
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        d = {}
        for w in wordDict:
            d[w] = 1

        bk = {}
        bk[''] = []

        def util(ss):

            if len(ss) == 0:
                return
            elif ss in bk:
                return 
            else:
                bk[ss] = []
                for i in range(len(ss) - 1, -1, -1):
                    if ss[i:] in d:
                        util(ss[:i])
                        for l in bk[ss[:i]]:
                            bk[ss].append(l + ' ' + ss[i:])
                        if i == 0:
                            bk[ss].append(ss[i:])
            return

        util(s)                           
        return bk[s]
