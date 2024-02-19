# You are given two non empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contians a single digit 
# Add the two nums and return the sum as a linked list

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
			
	def printEle(self): 
		iter_node=self.head
		while iter_node:
			print(iter_node.data,end=' ') 
			iter_node=iter_node.next   
		   
# adding the numbers		
def Add(head1,head2):  # Time Complexity --- O(N) where N is len(max(ll1,ll2))
	res_ll=Linkedlist() # resultant linked list
	iter_node1=head1  # used to iterate through linked list 1 (ll1)
	iter_node2=head2  # used to iterate through linked list 2 (ll2)
	carry=0  
	while iter_node1 or iter_node2 or carry:
		data1=iter_node1.data if iter_node1 else 0  # if linked list1 is empty then data1=0 
		data2=iter_node2.data if iter_node2 else 0  # if linked list2 is empty then data2=0 
		sum=data1 + data2+carry
		carry=sum//10
		sum %= 10
		res_ll.insert(sum)
		iter_node1=iter_node1.next if iter_node1 else None  # if linked list1 reaches end then iter_node1 is None 
		iter_node2=iter_node2.next if iter_node2 else None  # if linked list2 reaches end then iter_node2 is None 
	
	res_ll.printEle()  # printing 	esultant linked list
		
ll1=Node(2)
ll1.next=Node(4)			
ll1.next.next=Node(3)

ll2=Node(5)
ll2.next=Node(6)
ll2.next.next=Node(4)

Add(ll1,ll2)

# * Time Complexity --- O(N) where N is len(max(ll1,ll2))
# * Space Complexity --- O(M) where M is len(ll1+ll2)