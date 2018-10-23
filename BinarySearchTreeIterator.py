# 173. Binary Search Tree Iterator

# Google Tag

'''
Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
'''

# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
Inorder travesal problem
'''

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.l = []
        if root:
            while root.left:
                self.l.append(root)
                root = root.left
            self.l.append(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.l) != 0:
            return True
        else:
            return False

    def next(self):
        """
        :rtype: int
        """
 
        n = self.l.pop()
        root = n.right
        if root:
            while root.left:
                self.l.append(root)
                root = root.left
            self.l.append(root)

        return n.val
