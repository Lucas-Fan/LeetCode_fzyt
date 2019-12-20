# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        a = head
        b = None
        while a != None:
            temp = a.next
            a.next = b
            b = a
            a = temp
        return b
