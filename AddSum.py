# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        dummy = ListNode()  
        cur_node = dummy
        
        while l1 or l2 or carry:
            # Get values from the current nodes
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Compute the sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            new_val = total % 10
            
            # Create a new node with the computed value
            cur_node.next = ListNode(new_val)
            cur_node = cur_node.next
            
            # Move to the next nodes if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next 

# Time Complexity --- O(max(n,m)) where n is no of nodes in l1 and m is no of nodes in l2.
# Space Complexity --- O(max(n,m)) where n is no of nodes in l1 and m is no of nodes in l2.


# Here in above code the linked list contains only single digit as its value . Here in this code just we travelling through each node and adding for resultant.