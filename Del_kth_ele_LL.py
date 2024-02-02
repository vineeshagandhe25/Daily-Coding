# Given an array of integers, convert into linked list

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
		
	def remove_kth_ele(self,index):  # Function to remove ele
		if self.head == None:    # condition for empty Linked List
			return
		current_node = self.head    
		position = 0
		if position == index:    # Condition to remove first ele
			self.head = self.head.next
			return
		else:
			while(current_node != None and position+1 != index):
				position = position+1
				current_node = current_node.next

			if current_node != None:
				current_node.next = current_node.next.next
			else:
				print("Index not present")	
						
		
	def printLinkedList(self): # Time Complexity --- O(M) where M is length of linked list
		current_node = self.head # starting from head node and traversing through list using current_node
		while(current_node):
			print(current_node.data,end=" ")
			current_node = current_node.next			

arr=[1,2,3]
ll=Linkedlist()
for i in arr:  # Time Complexity --- O(N) where N is length of arr 
	ll.insert(i)
ll.remove_kth_ele(2)
ll.printLinkedList()

# *Time Complexity --- O(N) where N is length of arrr (Dominated factor )
# *Time Complexity ---O(1) constant no of variables used.