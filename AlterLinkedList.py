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
		
	def swap(self):
		if self.head is None:
			return None
		if self.head.next is None:
			return self.head.data
		self.head,self.head.next=self.head.next,self.head
		iter_node=self.head.next.next
		while iter_node.next != None:
			iter_node,iter_node.next=iter_node.next,iter_node
			iter_node=iter_node.next.next
		return self.head.data
		
		
			
			
    
	    
		
ll=Linkedlist()
for i in [1,2,3]:
     ll.insert(i) 
print(ll.swap())	 
	 
	        