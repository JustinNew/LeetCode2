# 270. Closest Binary Search Tree Value

'''
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.

Examples:
Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """

        '''
        DFS or BFS and record the closest so far.
        '''

        diff = float('inf')
        res = float('inf')
        s = [root]

        while 1:

            temp = []
            for n in s:
                if abs(n.val - target) < diff:
                    diff = abs(n.val - target)
                    res = n.val
                if n.left:
                    temp.append(n.left)
                if n.right:
                    temp.append(n.right)

            if len(temp) == 0:
                return res

            s = temp
