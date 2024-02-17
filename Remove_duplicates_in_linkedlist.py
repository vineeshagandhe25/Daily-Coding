# Given the head of a sorted linked list , delete all duplictes such that each element appears only once.Return the linked list sorted as well.

class Node:  # This class is used for linkedlist to consists one is data field and another is next field
	def __init__(self, data):
		self.data = data   #  data container
		self.next = None   # next pointer
		
class Linkedlist:
	def __init__(self):
		self.head = None  # Head pointer  
		self.tail=None    # Tail pointer
		
	def insert(self,data): # Function to insert data at end of linked list
		new_node = Node(data) # Creating new node
		if self.head is None:
			self.head = new_node # Initially making new node as head and tail node
			self.tail= new_node
			return
		self.tail.next=new_node
		self.tail=new_node  # Making new node as tail node  
		 
		
# removing duplicates         
def removeDuplicates(head):  # Time Complexity --- O(N) where N is length of arr
	if head is None: # for empty linked list
		return False
	iter_node=head  # used to iterate linked list
	while iter_node.next: 
		if iter_node.data==iter_node.next.data:  # if adjacent elements are same then next pointer gets updated 
			iter_node.next=iter_node.next.next
		else:
			iter_node=iter_node.next	
	# printing linked list after removing thenduplicates	
	iter_node=head
	while iter_node:
		print(iter_node.data,end=' ')	
		iter_node=iter_node.next
    
arr=[1,1,2,3,3]
ll=Linkedlist()
for i in arr:  # Time Complexity --- O(N) where N is length of arr 
	ll.insert(i)
removeDuplicates(ll.head)

 # * Time Complexity --- O(N) where N is length of arr 
 #  * Space Complexity --- O(N) where N is length of arr 
