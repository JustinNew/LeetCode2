# 23. Merge k Sorted Lists

# Google Tag

'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Merge one after another.
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        def mergeTwo(n1, n2):
            dummy = ListNode(0)
            cur = dummy

            while n1 and n2:
                if n1.val < n2.val:
                    next = n1.next
                    cur.next = n1
                    n1.next = None
                    n1 = next
                else:
                    next = n2.next
                    cur.next = n2
                    n2.next = None
                    n2 = next
                cur = cur.next

            if not n1:
                cur.next = n2
            elif not n2:
                cur.next = n1

            return dummy.next

        if len(lists) == 0:
            return None
        
        res = lists[0]
        for i in range(1, len(lists)):
            res = mergeTwo(res, lists[i])

        return res

    # Merge pair by pair.
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def mergeTwo(n1, n2):
            dummy = ListNode(0)
            cur = dummy

            while n1 and n2:
                if n1.val < n2.val:
                    next = n1.next
                    cur.next = n1
                    n1.next = None
                    n1 = next
                else:
                    next = n2.next
                    cur.next = n2
                    n2.next = None
                    n2 = next
                cur = cur.next

            if not n1:
                cur.next = n2
            elif not n2:
                cur.next = n1

            return dummy.next

        if len(lists) == 0:
            return None
        
        while len(lists) > 1:
            
            temp = []
            if len(lists) % 2 == 0:
                for i in range(0, len(lists), 2):
                    temp.append(mergeTwo(lists[i], lists[i + 1]))
            else:
                for i in range(0, len(lists) - 1, 2):
                    temp.append(mergeTwo(lists[i], lists[i + 1]))
                temp.append(lists[-1])
                
            lists = temp
            
        return lists[0]
