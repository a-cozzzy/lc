class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode()
        current = head 
        
        while list1 and list2: 
            if list1.val < list2.val:
                current.next = list1  
                list1 = list1.next  
            else:
                current.next = list2  # Attach the smaller node
                list2 = list2.next  # Move the pointer on list2
            current = current.next  # Move to the next node

        current.next = list1 or list2
        
        return head.next 
