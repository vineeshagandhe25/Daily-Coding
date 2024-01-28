# Given an array of integers, convert into linked list

class Node:  # This class is used for linkedlist to consists one is data field and another is next field
	def __init__(self, data):
		self.data = data   #  data container
		self.next = None   # next pointer
		
class Linkedlist:
	def __init__(self):
		self.head = None  # Head pointer  
		
	def insert(self,data): # Function to insert data at end of linked list
		new_node = Node(data) # Creating new node
		if self.head is None:
			self.head = new_node
			return

		current_node = self.head  # starting from head node and traversing through list using current_node
		while(current_node.next):  # Traverse till last node and inserting node there
			current_node = current_node.next

		current_node.next = new_node
			
	def printLinkedList(self):
		current_node = self.head # starting from head node and traversing through list using current_node
		while(current_node):
			print(current_node.data)
			current_node = current_node.next	

arr=[1,2,3]
ll=Linkedlist()
for i in arr:  # Time Complexity --- O(N) where N is length of arr
	ll.insert(i)
ll.printLinkedList()	# To print LinkedList

# *Time Complexity --- O(N) where N is length of arrr
# *Time Complexity ---O(1) constant no of variables used.
	
			
    
			
    
		