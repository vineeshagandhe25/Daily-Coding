# Given a linkedlist, insert three more nodes at an index k


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
		
	def insertAtIndex(self, data1,data2,data3, index):  # Function to insert elements
		new_node = Node(data1)   # 1 st node
		second_node=Node(data2)  # 2 nd node
		third_node=Node(data3)   # 3 rd node
		current_node = self.head # current_node used to traverse through LinkedList to find specific index
		position = 0
		if position == index:   # condition when index is 0
			new_node.next=second_node
			second_node.next=third_node
			third_node.next=self.head
			self.head=new_node
			return
		else:
			while(current_node != None and position+1 != index):
				position = position+1
				current_node = current_node.next

			if current_node != None:
                
				new_node.next = second_node
				second_node.next=third_node
				third_node.next=current_node.next
				current_node.next = new_node
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
#ll.insertAtIndex(7,8,9,5)
#ll.printLinkedList()
#ll.insertAtIndex(7,8,9,1)
#ll.printLinkedList()
#ll.insertAtIndex(7,8,9,0)
#ll.printLinkedList()
ll.insertAtIndex(7,8,9,2)
ll.printLinkedList()

# *Time Complexity --- O(N) where N is length of arrr (Dominated factor )
# *Time Complexity ---O(1) constant no of variables used.