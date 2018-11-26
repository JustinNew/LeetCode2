# 297. Serialize and Deserialize Binary Tree

# Facebook Tag

'''
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return str([None])

        res = []
        s = [root]
        while 1:
            temp = []
            flag = 0
            for n in s:
                if not n:
                    res.append(None)
                    temp.append(None)
                    temp.append(None)
                else:
                    res.append(n.val)
                    temp.append(n.left)
                    temp.append(n.right)
                    if flag == 0 and (n.left or n.right):
                        flag = 1

            if flag:
                s = temp
            else:
                return str(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        import re

        data = data[1:-1]
        data = re.split(', ', data)

        if len(data) == 1 and data[0] == None:
            return None

        l = len(data)
        used = 0
        level = 0
        nodes = [None for i in range(l)]
        while used < l:
            for i in range(used, min(used + 2 ** level, l)):
                if data[i] != None:
                    n = TreeNode(data[i])
                    nodes[i] = n
                    if i != 0:
                        t = i - used
                        p = used - 2 ** (level - 1) + int(t / 2)
                        if t % 2 == 0:
                            nodes[p].left = n
                        else:
                            nodes[p].right = n
            used += 2 ** level
            level += 1

        return nodes[0]
