# 31. Next Permutation

# Google Tag

'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

'''
1. Find the first decreasing one.
2. Find the least larger one to be exchanged to its right. 
3. Exchange the two
4. Rearrange the remaining
'''

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if len(nums) <= 1:
            return
        
        # Find the first decreasing one.
        right = -1
        left = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                right = i - 1
                left = i
                break
   
        if right == -1:
            nums.sort()
            return

        # Find the least larger one to be exchanged to its right.
        for i in range(right + 1, len(nums)):
            if nums[i] > nums[right] and nums[i] < nums[left]:
                left = i

        # Exchange the two
        nums[right], nums[left] = nums[left], nums[right]

        # Rearrange the remaining
        nums[right + 1:] = sorted(nums[right + 1:])

        return 
