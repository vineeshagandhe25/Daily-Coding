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
		
	def midEle(self):  # Function to print mid ele
		mid=self.sizeOfLL()//2   # calling sizeOfLL() to know the size
		iter_node=self.head
		i=0
		if mid==i:
			print(self.head)
			return
		while iter_node:
			if i == mid:
				break
			iter_node=iter_node.next
			i += 1
		print(iter_node.data)	
						
	def sizeOfLL(self):   # Function to find the size of linkedlist
		size = 0    # Time Complexity --- O(M) where M is length of linked list
		if(self.head):
			current_node = self.head
			while(current_node):
				size = size+1
				current_node = current_node.next
			return size
		else:
			return 0			

		
	def printLinkedList(self): # Time Complexity --- O(M) where M is length of linked list
		current_node = self.head # starting from head node and traversing through list using current_node
		while(current_node):
			print(current_node.data)
			current_node = current_node.next			

arr=[1,2]
ll=Linkedlist()
for i in arr:  # Time Complexity --- O(N) where N is length of arr (Dominated factor )
	ll.insert(i)
ll.midEle()	

# *Time Complexity --- O(N) where N is length of arrr
# *Time Complexity ---O(1) constant no of variables used.