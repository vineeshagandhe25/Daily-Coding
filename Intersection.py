# Q: Given two lists sorted in increasing order , create and return a new list representing the intersection of two lists.

# To create Nodes
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

# To create Linked List
class LinkedList:
    def __init__(self):
        self.head=self.tail=None
    def insert(self,data):  # To insert Nodes
        if self.head is None:
            self.head=self.tail=Node(data)
            return
        else:
            newnode=Node(data)
            self.tail.next= newnode
            self.tail=newnode
    def printLL(self):  # To print Nodes
        if self.head is None:
            print("empty linked list")
            return
        iter_node=self.head
        while iter_node:
            print(iter_node.data)
            iter_node=iter_node.next

# Intersection function
def intersection(ll1,ll2):
    iter_node1=ll1.head  # Head node of linked list 1
    iter_node2=ll2.head  # Head node of linked list 2
    res_ll=LinkedList()  # resultant linked list
    while iter_node1:
        while iter_node2 and iter_node2.data <= iter_node1.data:
            if iter_node1.data == iter_node2.data:
                res_ll.insert(iter_node1.data)
            iter_node2=iter_node2.next    
        iter_node1=iter_node1.next  
    return res_ll

# Input
ll1=LinkedList()
data1=[1,2,3,4,5]
for i in data1:
    ll1.insert(i)
ll2=LinkedList()
data2=[2,3,4]
for i in data2:
    ll2.insert(i)   
res_ll=intersection(ll1,ll2)
res_ll.printLL()     

# Time complexity for Intersection function --- O(N) where N is length of Linkedlist 1 (ll1)
# Space complexity for Intersection function --- O(M) where M is length of res_ll


