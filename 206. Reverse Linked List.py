# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if not head or not head.next:
            return head
        
        curr = head
        prev = None

        while curr is not None:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex

        head = prev
        return head

        