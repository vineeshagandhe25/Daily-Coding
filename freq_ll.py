'''Qsn : 

Given a linkedlist, which consists of integers ranging from 1 to 50, count the frequency of each digit. Linkedlist-can contain duplicate integers. 

example
linkedlist - 1122456667
output
occurrence of 1 - 2
occurrence of 2 - 2
occurrence of 4 - 1
occurrence of 5 - 1
occurrence of 6 - 3
occurrence of 7 - 1'''

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
			
	def printLinkedList(self):
		current_node = self.head # starting from head node and traversing through list using current_node
		while(current_node):
			print(current_node.data)
			current_node = current_node.next	

arr=[1,1,2,2,4,5,6,6,6,7]
ll=Linkedlist()
for i in arr:  # Time Complexity --- O(N) where N is length of arr
	ll.insert(i)
ll.printLinkedList()