# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def get_length(self, head):
        count = 0
        while head:
            count += 1
            head = head.next
        return count

    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k == 0:
            return head

        n = self.get_length(head)
        k = k % n
        
        # Add this check to avoid errors when k == 0 after modulo
        if k == 0:
            return head

        # tail=head
        # prev=tail
        # k=n-k

        # while k!=0:
        #     if k==1:
        #         prev=tail

        #     tail=tail.next 
        #     k-=1
        
        # last=tail
        # while last.next is not None:
        #     last=last.next

        # last.next=head
        # prev.next=None
        # head=tail
        # return tail

        steps = n - k
        new_tail = head
        for _ in range(steps - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None

        tail = new_head
        while tail.next:
            tail = tail.next

        tail.next = head
        return new_head
