# 49. Group Anagrams

# Facebook Tag

'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        l = len(strs)
        if l == 0:
            return []

        d = {}
        for s in strs:
            k = tuple(sorted(s))
            d[k] = d.get(k, []) + [s]

        return [i for i in d.values()]
