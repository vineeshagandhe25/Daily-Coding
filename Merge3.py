# Merging two sorted linked lists into sorted single list .
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
    
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()   # creating dummy(head node) for resultant

        current = dummy # used for next iteration of resultant
        
        while list1 and list2:
            # comparing and assigning values to resultant
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
    
            current = current.next
        
        # assigning remaining values
        if list1:
            current.next = list1

        if list2:
            current.next = list2
        
        return dummy.next

# Time Complexity --- O(N) where N is length of min(list1,list2).
# Space Complexity --- O(L) where L is length(list1)+length(list2).
        