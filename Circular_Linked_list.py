#  Wrire program to implement circular Linked List.
class Node: # class to create a Node
    def __init__(self, data):
        self.data = data  # Data Container
        self.next = None  # Next Pointer

class CircularLinkedList:
    def __init__(self):
        self.head = None # Head Pointer to point First Node in Linked List
        self.tail = None # Tail Pointer to point Last Node in Linked List

    # Insertion Operations
    def insert_at_beginning(self, data): # Time Complexity -- O(1)
        new_node = Node(data)
        if not self.head:    # condition to check whether Linked List is empty or not
            self.head = new_node     # Assigning the new_node to head node
            self.tail=new_node       # Assigning the new_node to tail node
            self.tail.next=self.head  # Making the first node to ponits itself (To make it Circular)
        else:
            new_node.next=self.head   
            self.head=new_node
            self.tail.next=self.head  # Updating the tail 's next to ponits the new head node

    def insert_at_end(self, data): # Time Complexity -- O(1)
        new_node = Node(data)
        if not self.head:
            # code for empty Linked List
            self.head = new_node     
            self.tail=new_node     
            self.tail.next=self.head 
        else:
            self.tail.next=new_node
            self.tail=new_node
            self.tail.next=self.head  # Updating the tail 's next to ponits the new head node
 
            
    # Deletion Operations
    def delete_at_beginning(self): # Time Complexity -- O(1)
        if not self.head: # condition to check whether Linked List is empty or not
            print("List is empty")
            return
        temp = self.head
        if temp.next == self.head: # Condition for Single element Linked List
            self.head = None
        else:
            self.head=self.head.next # Making second node as head node 
            self.tail.next= self.head # Updating the tail 's next to ponits the new head node

    def delete_at_end(self): # Time Complexity -- O(M) where M is length of Linked List 
        if not self.head:
            # code for empty Linked List
            print("List is empty")
            return
        temp = self.head  
        prev = None # To point the previous node of tail node
        while temp.next != self.head:
            prev = temp
            temp = temp.next
        if prev:
            self.tail=prev
            self.tail.next= self.head # Updating the tail 's next to ponits the  head node
        else:
            self.head = self.tail = None

    # Print the elements in the list
    def print_list(self): # Time Complexity -- O(N) where N is length of Linked List 
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while True:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.head:
                break
        print()


circular_list = CircularLinkedList()
circular_list.insert_at_beginning(1)
circular_list.insert_at_end(3)
circular_list.insert_at_end(4)
circular_list.insert_at_beginning(0)
circular_list.print_list()
circular_list.delete_at_end()
circular_list.delete_at_beginning()
circular_list.print_list()


# * Time Complexity --- O(N) where N is the length of the Circular Linked List
# * Space  Complexity --- O(N) where N is the length of the Circular Linked List