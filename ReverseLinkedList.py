# 206. Reverse Linked List

# Facebook Tag

'''
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Iterative
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        cur = head

        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next

        head.next = None

        return prev

    # Recursive
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def util(n):

            if not n:
                return (None, None)

            cur = n
            if not cur.next:
                return (cur, cur)
            else:
                tail, head = util(cur.next)
                cur.next = None
                tail.next = cur
                return (cur, head)

        t, h = util(head)
        return h
