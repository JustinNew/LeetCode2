# 272. Closest Binary Search Tree Value II

'''
Given a non-empty binary search tree and a target value, find k values in the BST that are closest to the target.

Note:

Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in the BST that are closest to the target.

Example:
Input: root = [4,2,5,1,3], target = 3.714286, and k = 2

    4
   / \
  2   5
 / \
1   3

Output: [4,3]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
   
    # DFS or BFS 
    # Time Limit Exceedede.
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
 
        res = []
        s = [root]

        while 1:

            temp = []
            for n in s:
                if len(res) < k:
                    res.append((n.val, abs(n.val - target)))
                    res.sort(key=lambda x: x[1])
                elif abs(n.val - target) < res[-1][1]:
                    res.pop()
                    res.append((n.val, abs(n.val - target)))
                    res.sort(key=lambda x: x[1])

                if n.left:
                    temp.append(n.left)
                if n.right:
                    temp.append(n.right)

            if len(temp) == 0:
                return [i[0] for i in res]

            s = temp

    ##############################################################################################################
    # Use heapq to make it faster
    def closestKValues(self, root, target, k):

        import heapq

        res = []
        s = [root]

        while 1:

            temp = []
            for n in s:
                if len(res) < k:
                    heapq.heappush(res, (-1 * abs(n.val - target), n.val))
                elif -1 * abs(n.val - target) > res[0][0]:
                    heapq.heappop(res)
                    heapq.heappush(res, (-1 * abs(n.val - target), n.val))

                if n.left:
                    temp.append(n.left)
                if n.right:
                    temp.append(n.right)

            if len(temp) == 0:
                return [i[1] for i in res]

            s = temp
