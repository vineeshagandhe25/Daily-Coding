# Write a program to implement Doubly Linked List
 
# Node of Doubly Linked List
class Node:  
    def __init__(self,data):
        self.data=data
        self.previous=None  # reference to previous node in linked list
        self.next=None      # reference to next node in linked list

# Doubly Linked list
class DoublyLinkedList:
    def __init__(self):
        self.head=None  # reference to fisrt node in linked list
        self.tail=None  # reference to last node in linked list   

    # Inserting node at beginning 
    def insert_at_begin(self,data):  # Time Complexity -- O(1)
        # code for empty linked list  
        if self.head is None:
            self.head=self.tail=Node(data)  
            return
        # code for non-empty linked list
        else:
            new_node=Node(data)  # creating new node
            self.head.previous=new_node  # updating the previous of head node to point new node
            new_node.next=self.head  # updating  the next of new node to point head node
            self.head=new_node  # updating new node as head node
            return
        
    # Inserting node at last    
    def insert_at_end(self,data):  # Time Complexity -- O(1)
         # code for empty linked list  
        if self.head is None:
            self.head=self.tail=Node(data)  
            return
        # code for non-empty linked list
        else:
            new_node=Node(data)  # creating new node
            self.tail.next=new_node  # updating the next of tail node to point new node
            new_node.previous=self.tail  # updating  the previous of new node to point tail node
            self.tail=new_node  # updating new node as tail node
            return
        
    # Deleting the fisrt node
    def delete_at_first(self):  # Time Complexity -- O(1)
         # code for empty linked list  
        if self.head is None:
            print("The list is empty") 
            return
        # code for non-empty linked list
        else:
            if self.head.next is None:
                self.head=self.tail= None
                return 
            self.head=self.head.next  # updating next node as head node
            self.head.previous=None  # updating the previous of head node to None 
            return 
        
    # Deleting the last node
    def delete_at_last(self):  # Time Complexity -- O(1)
        # code for empty linked list  
        if self.head is None:
            print("The list is empty") 
            return
        # code for non-empty linked list
        else:
            # code execute when linked list size is 1
            if self.tail.previous is None:
                self.head=self.tail= None
                return 
            self.tail=self.tail.previous  # updating previous node as tail node
            self.tail.next=None  # updating the next of tail node to None
            return  

    # Printing Linked List
    def show(self):  # Time Complexity -- O(N) where N is length of linked list 
        # code for empty linked list  
        if self.head is None:
            print("The list is empty") 
            return
        # code for non-empty linked list
        else:
            iter_node=self.head  # to traverse through linked list
            while iter_node:
                print(iter_node.data,end=" ")
                iter_node=iter_node.next
            print()    

    # Printing Linked List in reverse order
    def show_reverse(self):  # Time Complexity -- O(N) where N is length of linked list 
        # code for empty linked list  
        if self.tail is None:
            print("The list is empty") 
            return
        # code for non-empty linked list
        else:
            iter_node=self.tail  # to traverse through linked list
            while iter_node:
                print(iter_node.data,end=" ")
                iter_node=iter_node.previous
            print()    

# TEST CASES
doublyLinkedList=DoublyLinkedList()
doublyLinkedList.show()  # printing empty list
doublyLinkedList.show_reverse()  # printing empty list
doublyLinkedList.delete_at_first()  # deleting node form empty linked list
doublyLinkedList.insert_at_begin(1)  # inserting node at beginning
doublyLinkedList.delete_at_last()   # deleting node from linked list size of 1
doublyLinkedList.show()
doublyLinkedList.insert_at_end(1)    # inserting node at last
doublyLinkedList.delete_at_first()  # deleting node from linked list size of 1
doublyLinkedList.show()
# General input
doublyLinkedList.insert_at_begin(1)
doublyLinkedList.insert_at_end(2)
doublyLinkedList.insert_at_begin(0)
doublyLinkedList.insert_at_end(3)
doublyLinkedList.show()
doublyLinkedList.show_reverse()
doublyLinkedList.delete_at_first()
doublyLinkedList.delete_at_last()
doublyLinkedList.show()
doublyLinkedList.show_reverse()

# Time Complexity --  O(N) where N is length of linked list 
# Space Complexity --  O(N) where N is length of linked list 
            
