# 42. Trapping Rain Water

# Google Tag

'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

'''
Use two array to track left max and right max.
Water for i is min(max_l, max_r) - n_i.
'''

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = [0 for i in range(len(height))]
        right = [0 for i in range(len(height))]

        m = 0
        for i in range(1, len(height)):
            m = max(height[i - 1], m)
            left[i] = m

        m = 0 
        for i in range(len(height) - 2, -1, -1):
            m = max(height[i + 1], m)
            right[i] = m

        res = 0
        for i in range(len(height)):
            res += max(0, min(left[i], right[i]) - height[i])

        return res
