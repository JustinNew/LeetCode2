# 336. Palindrome Pairs

# Google Tag

'''
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:

Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]] 
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]] 
Explanation: The palindromes are ["battab","tabbat"]
'''

'''
1. Need to do 1-on-1 pair
2. How to simplify the 1-on-1 pair
   Do a sort for original string
   Do a sort for reversed string
   1-on-1 pair
'''

class Solution:
    # Time Limit Exceeded.
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """

        if len(words) == 0:
            return []

        org = [(words[i], i) for i in range(len(words))]
        rev = [(words[i][::-1], i) for i in range(len(words))]
        org.sort(key=lambda x: x[0])
        rev.sort(key=lambda x: x[0])
        
        res = []
        for i in range(len(words)):
            (w_o, i_o) = org[i]
            for j in range(len(words)):
                (w_r, i_r) = rev[j]
                if not w_o:
                    if w_r == w_r[::-1] and i_o != i_r:
                        res.append([i_o, i_r])
                if not w_r:
                    if w_o == w_o[::-1] and i_o != i_r:
                        res.append([i_o, i_r])
                elif w_o and w_r and w_o[0] == w_r[0]:
                    t1 = w_o
                    t2 = w_r
                    if len(t1) > len(t2):
                        t1, t2 = t2, t1
                    t3 = t2[len(t1):]
                    if t1 == t2[:len(t1)] and t3 == t3[::-1] and i_o != i_r:
                        res.append([i_o, i_r])

        return res

'''
https://leetcode.com/problems/palindrome-pairs/discuss/79209/Accepted-Python-Solution-With-Explanation

The basic idea is to check each word for prefixes (and suffixes) that are themselves palindromes. If you find a prefix that is a valid palindrome, then the suffix reversed can be paired with the word in order to make a palindrome. It's better explained with an example.

words = ["bot", "t", "to"]
Starting with the string "bot". We start checking all prefixes. If "", "b", "bo", "bot" are themselves palindromes. The empty string and "b" are palindromes. We work with the corresponding suffixes ("bot", "ot") and check to see if their reverses ("tob", "to") are present in our initial word list. If so (like the word to"to"), we have found a valid pairing where the reversed suffix can be prepended to the current word in order to form "to" + "bot" = "tobot".

You can do the same thing by checking all suffixes to see if they are palindromes. If so, then finding all reversed prefixes will give you the words that can be appended to the current word to form a palindrome.

The process is then repeated for every word in the list. Note that when considering suffixes, we explicitly leave out the empty string to avoid counting duplicates. That is, if a palindrome can be created by appending an entire other word to the current word, then we will already consider such a palindrome when considering the empty string as prefix for the other word.
'''

'''
1. Check all prefix to see whether it is palindrome, if it is, then check whether suffix is in words. '' counted in prefix.
2. Check all suffix to see whether it is palindrome, if it is, then check whether prefix is in words. '' not counted in suffix.
'''

    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """

        if len(words) == 0:
            return []

        res = []
        d = {}
        for i in range(len(words)):
            d[words[i]] = i

        for i in range(len(words)):
            # For prefix
            for j in range(len(words[i]) + 1): # Be careful about the range.
                suffix_rev = words[i][j:][::-1]
                if words[i][:j] == words[i][:j][::-1] and suffix_rev in d:
                    if d[suffix_rev] != i:
                        res.append([d[suffix_rev], i])

            # For suffix
            for j in range(len(words[i]) - 1, -1, -1): # Be careful about the range.
                prefix_rev = words[i][:j][::-1]
                if words[i][j:] == words[i][j:][::-1] and prefix_rev in d:
                    res.append([i, d[prefix_rev]])

        return res
