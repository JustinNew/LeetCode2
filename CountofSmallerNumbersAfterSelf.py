# 315. Count of Smaller Numbers After Self

# Google Tag

'''
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
'''

class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        import bisect

        l = len(nums)
        if l == 0:
            return []
        elif l == 1:
            return [0]

        nums.reverse()
        s = []
        res = []
        for v in nums:
            i = bisect.bisect_left(s, v)
            res.append(i)
            bisect.insort(s, v)

        return res[::-1]
