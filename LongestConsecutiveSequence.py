# 128. Longest Consecutive Sequence

# Google Tag

'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''

'''
Use dictionary
Key is the number, value is the length of the sequence.

1. i, no i - 1 or no i + 1
2. i, yes i - 1 but no i + 1
3. i, no i - 1 but yes i + 1
4. i, yes i - 1 and yes i + 1

# Pay attention to check whether i in d, and insert every i.
'''

class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <= 1:
            return len(nums)
        
        d = {}
        res = 0
        for i in nums:
            if i not in d:
                if i - 1 in d and i + 1 in d:
                    left = d[i - 1]
                    right = d[i + 1]
                    d[i - left] = left + 1 + right
                    d[i] = left + 1 + right
                    d[i + right] = left + 1 + right
                    if d[i - left] > res:
                        res = d[i - left]
                elif i - 1 in d: 
                    left = d[i - 1]
                    d[i] = left + 1
                    d[i - left] = left + 1
                    if d[i] > res:
                        res = d[i]
                elif i + 1 in d:
                    right = d[i + 1]
                    d[i] = right + 1
                    d[i + right] = right + 1
                    if d[i] > res:
                        res = d[i]
                else:
                    d[i] = 1
                    if d[i] > res:
                        res = d[i]

        return res
