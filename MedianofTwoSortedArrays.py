# 4. Median of Two Sorted Arrays

# Google Tag

'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        l1 = len(nums1)
        l2 = len(nums2)

        if (l1 + l2) % 2 == 0:
            return (self.kth(int((l1 + l2) / 2), nums1, nums2) + self.kth(int((l1 + l2) / 2) - 1), nums1, nums2) / 2
        else:
            return self.kth(int((l1 + l2) / 2), nums1, nums2)

    # Kth is '0' based.
    def kth(self, k, arr1, arr2):

        if len(arr1) == 0:
            return arr2[k]
        elif len(arr2) == 0:
            return arr1[k]

        m1 = int(len(arr1) / 2)
        m2 = int(len(arr2) / 2)

        if m1 + m2 < k:
            if arr1[m1] < arr2[m2]:
                # arr1[m1] can not be medium.
                return self.kth(k - m1 - 1, arr1[m1 + 1:], arr2)
            else:
                return self.kth(k - m2 - 1, arr1, arr2[m2 + 1:])
        else:
            if arr1[m1] < arr2[m2]:
                # arr2[m2] can not be medium.
                return self.kth(k, arr1, arr2[:m2])
            else:
                return self.kth(k, arr1[:m1], arr2)
