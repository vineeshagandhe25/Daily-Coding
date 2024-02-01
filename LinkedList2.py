# Given a linked list of size > k, find the kth element from the last. 

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
			
	def printKEle(self,k):  #  To Print k th ele of K sized Linked List 
		if k <= 0:
			print("K value must be greater then 0")
			return
		iter_pointer=self.head  # iter_pointer to iterate through Linked List
		k_pointer=self.head     # K_pointer to ponit K th element
		index=0
		while iter_pointer:
			if index >= k:  # if index meets k value ,k_pointer ponits starts iterating 
				k_pointer=k_pointer.next
			iter_pointer=iter_pointer.next
			index += 1	        
		print(k_pointer.data) # printing kth place data 	

arr=[1,2,3,4,5]
ll=Linkedlist()
for i in arr:  # Time Complexity --- O(N) where N is length of arr (Dominated factor )
	ll.insert(i)

ll.printKEle(-1)
ll.printKEle(0)  
ll.printKEle(1) 
ll.printKEle(2)
ll.printKEle(3)
ll.printKEle(4)   

# *Time Complexity --- O(N) where N is length of arrr
# *Time Complexity ---O(1) constant no of variables used.