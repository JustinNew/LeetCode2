# 239. Sliding Window Maximum

# Google Tag

'''
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Note: 
You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
'''

class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        import bisect

        if len(nums) == 0:
            return []

        res = []
        s = nums[:k]
        s.sort()

        for i in range(k, len(nums)):
            res.append(s[-1])
            s.remove(nums[i - k])
            bisect.insort(s, nums[i])

        res.append(s[-1])

        return res

    '''
    1. Use deque
    2. Keep the index of decreasing max
    '''
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        from collections import deque

        s = deque()
        l = len(nums)
        if l == 0:
            return []

        res = []
        for i in range(l): 
            # Pop out from left out of range index.
            while len(s) > 0 and s[0] <= i - k:
                s.popleft()
            
            # Pop out from right the ones not large than current one.
            while len(s) > 0 and nums[s[-1]] <= nums[i]:
                s.pop()
                
            s.append(i)
                
            if i >= k - 1:
                res.append(nums[s[0]])

        return res
