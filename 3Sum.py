# 15. 3Sum

# Facebook Tag

'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution:

    # Time Limit Exceeded.
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()

        res = []
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                low = i + 1
                high = len(nums) - 1
                target = -1 * nums[i]
                while low < high:
                    if nums[low] + nums[high] == target:
                        res.append([nums[i], nums[low], nums[high]])
                        low += 1
                        while low < len(nums) and nums[low] == nums[low - 1]:
                            low += 1
                        high -= 1
                        while high > 0 and nums[high] == nums[high + 1]:
                            high -= 1
                    elif nums[low] + nums[high] > target:
                        high -= 1
                        while high > 0 and nums[high] == nums[high + 1]:
                            high -= 1
                    else:
                        low += 1
                        while low < len(nums) and nums[low] == nums[low - 1]:
                            low += 1

        return res

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()

        res = []
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                d = {}
                temp = {}
                target = -1 * nums[i]
                for e in nums[i + 1:]:
                    if target - e in d and target - e not in temp:
                        res.append([nums[i], e, target - e])
                        temp[target - e] = 1
                    else:
                        d[e] = 1

        return res
