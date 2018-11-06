# 162. Find Peak Element

# Google Tag

'''
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
'''

'''
Binary search.
Compare nums[mid] with the neighboring elements.
  1. Larger than both, return
  2. larger than left and small than right, then peak must be right, not including mid element.
  3. Otherwise, the peak must be left and can include the mid element.
'''

class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        l = len(nums)
        if l == 0:
            return None
        elif l == 1:
            return 0
        elif l == 2:
            return 0 if nums[0] > nums[1] else 1

        low = 0 
        high = l - 1
        while low < high:
            mid = int((low + high) / 2)
            if mid == 0 or mid == l - 1:
                return mid
            elif nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] > nums[mid - 1] and nums[mid] < nums[mid + 1]:
                low = mid + 1
            else:
                high = mid

        return low

    # More simpler.
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return None
        elif l == 1:
            return 0
        elif l == 2:
            return 0 if nums[0] > nums[1] else 1

        low = 0 
        high = l - 1
        while low < high:
            mid = int((low + high) / 2)
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] > nums[mid - 1] and nums[mid] < nums[mid + 1]:
                low = mid + 1
            else:
                high = mid

        return low
