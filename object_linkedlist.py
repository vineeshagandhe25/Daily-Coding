# Student class which holds student details like name, roll number, and status
class Student:
    def __init__(self, name, roll, status):
        self.name = name          # Name of the student
        self.roll = roll          # Roll number of the student
        self.status = status      # Status of the student (e.g., Running or PassedOut)

    def display(self):
        print("Name: ", self.name)
        print("Roll No: ", self.roll)
        print("Status: ", self.status)

# Node class for linked list structure where each node contains a Student object
class Node:
    def __init__(self, obj):
        self.data = obj       
        self.next = None      


# ClassList class implements a singly linked list to manage the student list
class classlist:
    def __init__(self):
        self.head = None      # Head node

    # Method to add a new student to the list
    def add(self, newdata):
        newnode = Node(newdata)  # Create a new node 
        # If the list is empty set the new node as the head
        if self.head is None:
            self.head = newnode
            return
        # If the list is not empty traverse to the end of the list and add the new node
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = newnode

   
    def printd(self):
        temp = self.head
        
        while temp is not None:
            print(temp.data.display())  # Calls the display method of the Student class
            temp = temp.next


s = Student("vineesha", 308, "Running")
s2 = Student("vinni", 803, "PassedOut")

l = classlist()
l.add(s)
l.add(s2)

l.printd()

# Time Complexity --- O(n) where n is the number of nodes
# Space Complexity --- O(n) where n is the number of nodes