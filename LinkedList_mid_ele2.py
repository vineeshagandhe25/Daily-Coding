# Qsn: Find the middle element without finding the size of the linkedlist.If even size, print the mean of middle elements

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
		if self.head == None: # This is the condition for empty Linked List
			print(self.head)
			return
		first_pointer=self.head    # First pointer whose speed is s
		second_pointer=self.head   # second pointer whose speed is s/2
		while first_pointer != None and first_pointer.next != None:
			first_pointer=first_pointer.next.next
			second_pointer=second_pointer.next
		print(second_pointer.data)

arr=[1,2,3,4]
ll=Linkedlist()
for i in arr:  # Time Complexity --- O(N) where N is length of arr (Dominated factor )
	ll.insert(i)
ll.midEle()        	

# *Time Complexity --- O(N) where N is length of arrr
# *Time Complexity ---O(1) constant no of variables used.
        	
        	
        	

			