# Given a linked list print true if it is circular, false other wise.
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

class CircularLinkedList:
    def __init__(self):
        self.head = None # Head Pointer to point First Node in Linked List
        self.tail = None # Tail Pointer to point Last Node in Linked List

    def insert(self, data): # Time Complexity -- O(1)
        new_node = Node(data)
        if not self.head:    # condition to check whether Linked List is empty or not
            self.head = new_node     # Assigning the new_node to head node
            self.tail=new_node       # Assigning the new_node to tail node
            self.tail.next=self.head  # Making the first node to ponits itself (To make it Circular)
        else:
            new_node.next=self.head   
            self.head=new_node
            self.tail.next=self.head  # Updating the tail 's next to ponits the new head node

# Function to check the linked list is circular or not.            
def isCircular(object):  # Time Complexity -- O(N) where N is length of linked list
    if object.head is None:
          print("Empty list")
          return
     
    else: 
         iter_node=object.head
         while iter_node.next != object.head and iter_node.next != None:
              iter_node=iter_node.next

         if iter_node.next == object.head:
              print("True")

         else:
              print("False")

ll=Linkedlist()
for i in [1,2,3]:
     ll.insert(i)
cll=CircularLinkedList()
for i in [1,2,3]:
     cll.insert(i)
isCircular(ll)
isCircular(cll)              