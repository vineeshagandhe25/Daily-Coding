# Given a linkedlist, delete n nodes from kth position


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
		
	def remove_kth_ele(self,index,n):  # Function to remove eles
		if index < -1 or n <= 0:       # condition for negative inputs
			print("Invalid inputs")
			return  
		if self.head == None:    # condition for empty Linked List
			print("None")
			return
		size=self.sizeOfLL()  # calling sizeOfLL() to know the size of Linked List
		if index < size and ((size+1)-(index+1)) >= n :   # condition to check the inputs valid or not
			position=0    # position variable to points to the position of current_ptr
			if position == index :  # condition for index = 0
				while n > 0 :  # loop to remove eles from front
					self.head=self.head.next
					n -= 1
				return
			current_ptr=self.head # currnet_ptr is used to traverse through Linked List
			while  n > 0 :
				if position+1 >= index and n > 0 :
					if position+1 == size:  # condition to initialize last node's next to None
						current_ptr.next=None
						return
					current_ptr.next=current_ptr.next.next # removing the nodes
					n -= 1  # decrementing the n value
					position += 1  # incrementing yhe position value
					continue
				current_ptr=current_ptr.next 
				position += 1
		else:
			print("Invalid inputs")		
				
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
			print(current_node.data,end=" ")
			current_node = current_node.next
		print()				
        

arr=[]
ll=Linkedlist()
for i in arr:  # Time Complexity --- O(N) where N is length of arr 
	ll.insert(i)
	                       # Test cases  
#ll.remove_kth_ele(1,2)    # General input
#ll.printLinkedList()
#ll.remove_kth_ele(0,0)    # Invalid n where n is no of nodes to be removed
#ll.printLinkedList()
#ll.remove_kth_ele(6,3)    # Invalid index
#ll.printLinkedList()
#ll.remove_kth_ele(4,3)    # Invalid n
#ll.printLinkedList()	
#ll.remove_kth_ele(1,1)    # inputs to remove only one ele 
#ll.printLinkedList()
#ll.remove_kth_ele(2,3)    # inputs to remove all eles except first two eles 
#ll.printLinkedList()      
#ll.remove_kth_ele(0,5)    # inputs to remove all eles
#ll.printLinkedList()
ll.remove_kth_ele(0,1)    # inputs to remove first 3 eles 
ll.printLinkedList()
#ll.remove_kth_ele(-1,-1)  # negative inputs (Which are invalid)
#ll.printLinkedList()
	

# *Time Complexity --- O(N) where N is length of arrr (Dominated factor )
# *Time Complexity ---O(1) constant no of variables used.