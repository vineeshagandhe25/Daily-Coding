# Given a linked list , swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes.
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
	def __init__(self):
		self.head = None  # Head pointer  
		self.tail=None    # Tail pointer
		
	def insert(self,data): # Time Complexity -- O(1)
		new_node = Node(data) # Creating new node
		if self.head is None:
			self.head = new_node # Initially making new node as head and tail node
			self.tail= new_node
			return
		self.tail.next=new_node
		self.tail=new_node  # Making new node as tail node

	# swapping Function	
	def swap(self):  # Time complexity -- O(N) where N is length of Linked List
		if self.head is None :  # for empty linked list
			return self.head
		if self.head.next is None:  # for single node 
			return self.head.data
		#code to swap first two nodes
		node1=self.head
		node2=self.head.next
		node1.next=self.head.next.next
		node2.next=self.head
		self.head=node2
		iter_node=node1.next
		# code to swap next pair of nodes
		while iter_node and iter_node.next:
			temp=iter_node.next
			iter_node.next=temp.next
			temp.next=iter_node
			node1.next=temp
			node1=iter_node
			iter_node=iter_node.next

		return self.head.data
	
	# function to print linked list
	def printll(self):  # Time complexity -- O(N) where N is length of Linked List
		if self.head is None:
			return None
		iter_node=self.head
		while iter_node:
			print(iter_node.data,end=' ')
			iter_node=iter_node.next
		    
		
ll=Linkedlist()
for i in [1,2,3,4,5,6]:
     ll.insert(i) 
print(ll.swap())	
ll.printll() 
	 
# * Time complexity -- O(N) where N is length of Linked List	        
# * Space complexity -- O(N) where N is length of Linked List	        