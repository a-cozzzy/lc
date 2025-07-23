# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def length(self,count):
        n = 0
        while count:
            n+=1
            count=count.next
        return n

    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head
        length = self.length(head)
        cur = dummy
        for _ in range(length-n):
            cur = cur.next
        cur.next=cur.next.next

        return dummy.next

        