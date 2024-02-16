# Given the head of a singly linked list , return true if it is a palindrome or false otherwise

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
		
# Palindrome check        
def isPalindrome(head):  # Time Complexity --- O(N) where N is length of arr
	if head is None: # for empty linked list
		return False
	num=0 # variable used to store the num from linked list
	iter_node=head  # used to iterate linked list
	while iter_node:
			num = num * 10 + iter_node.data
			iter_node=iter_node.next
	if str(num) == str(num)[::-1] : # checking for palindrome by converting into strings and comparing original string with reverse of a string
		return True
	return False

arr=[1,2]
ll=Linkedlist()
for i in arr:  # Time Complexity --- O(N) where N is length of arr 
	ll.insert(i)
print(isPalindrome(ll.head))

arr=[1,2,1]
ll=Linkedlist()
for i in arr:  # Time Complexity --- O(N) where N is length of arr 
	ll.insert(i)
print(isPalindrome(ll.head))
 # * Time Complexity --- O(N) where N is length of arr 
 #  * Space Complexity --- O(N) where N is length of arr 
